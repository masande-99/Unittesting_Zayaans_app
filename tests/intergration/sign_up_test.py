from tests.base_test import BaseTest
from flask import request
from flask_login import current_user, AnonymousUserMixin
from website.models import User
from tests.base_test import db


class TestSignUp(BaseTest):
    def test_get_sign_up(self):
        with self.app_context as c:
            c = self.app.get('/sign-up', follow_redirects=True)

            self.assertEqual(c.status_code, 200)

    def test_sign_up_two(self):
        with self.app:
            response = self.app.get('/sign-up', follow_redirects=True)

            self.assertEqual(current_user.get_id(), AnonymousUserMixin.get_id(self))

            self.assertIn('/sign-up', request.url)

            self.assertIn(b'<title>\nSign Up\n</title>', response.data)

            self.assertEqual(response.status_code, 200)

    def test_post_email_handling(self):
        with self.app:
            response = self.app.post('/sign-up',
                                     data=dict(email="meh", first_name="Username",password1="1234yyy", password2="1234yyy"), follow_redirects=True)

            self.assertIn(b'Email must be greater than 3 characters', response.data)

            self.assertEqual(response.status_code, 200)

            user = db.session.query(User).filter_by(email="meh").first()

            self.assertFalse(user)

            self.assertIsNone(current_user.get_id())



    def test_sign_up_post_short_name(self):
        with self.app:
            response = self.app.post('/sign-up',
                                     data=dict(email="meh@gmail.com", firstName="U", password1="1234yyy", password2="1234yyy"), follow_redirects=True)
            self.assertIn(b'First name must be greater than 1 character', response.data)

    def test_password_dont_match_post(self):
        with self.app:
            response = self.app.post('/sign-up',
                                     data=dict(email="meh@gmail.com", firstName="Username", password1="1234yyy", password2="1234yy"), follow_redirects=True)
            self.assertIn(b'Passwords don&#39;t match', response.data)

    def test_sign_up_success(self):
        with self.app:
            response = self.app.post('/sign-up',
                                     data=dict(email="meh@gmail.com", firstName="Username", password1="1234yyy", password2="1234yyy"), follow_redirects=True)

            user = db.session.query(User).filter_by(email="meh@gmail.com").first()

            self.assertTrue(user)

            self.assertIn(b'Account created', response.data)

    # Added this test
    def test_password_seven_characters(self):
        with self.app:
            response = self.app.post('/sign-up',
                                     data=dict(email="meh@gmail.com", firstName="Username", password1="1234yy", password2="1234yy"), follow_redirects=True)
            self.assertIn(b'Password must be at least 7 characters', response.data)
            self.assertEqual(response.status_code, 200)

    # Added this test too
    def test_user_already_exists(self):
        with self.app:
            respons = self.app.post('/sign-up',
                                    data=dict(email="meh@gmail.com", firstName="Username", password1="1234yyy", password2="1234yyy"), follow_redirects=True)

            user = db.session.query(User).filter_by(email="meh@gmail.com")

            self.assertTrue(user)

            response = self.app.post('/sign-up',
                                     data=dict(email="meh@gmail.com", firstName="Username", password1="1234yyy", password2="1234yyy"), follow_redirects=True)

            self.assertIn(b'Email already in use', response.data)
