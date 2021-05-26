from tests.base_test import BaseTest
from flask import request
from flask_login import current_user, AnonymousUserMixin
from website.models import User
from tests.base_test import db


class TestLogOut(BaseTest):

    def test_logout_status_code(self):
        with self.app_context as c:
            c = self.app.get('/log-out', follow_redirects=True)

            self.assertEqual(c.status_code, 200)


    def test_logout_eccessed_user_if_logged_in(self):
        with self.app:
            with self.app_context:
                # singing up the user in order to log in

                response = self.app.post('/sign-up',
                                         data=dict(email="meh@gmail.com", firstName="Username", password1="1234yyy", password2="1234yyy"), follow_redirects=True)

                user = db.session.query(User).filter_by(email="meh@gmail.com").first()

                self.assertTrue(user)

                self.assertIn(b'Account created', response.data)
                # logging in as the user

                res = self.app.post('/log-in',
                                    data=dict(email="meh@gmail.com", password="1234yyy"), follow_redirects=True)

                self.assertIn(b'Logged in successfully', res.data)

                self.assertEqual(res.status_code, 200)

                # logging out as the user

                c = self.app.get('/log-out', follow_redirects=True)

                self.assertEqual(c.status_code, 200)

                # asserting that the user is redirected to login after logging out

                self.assertEqual('http://localhost/log-in', request.url)

                # assert that current user is none after logging out

                self.assertEqual(current_user.get_id(), AnonymousUserMixin.get_id(self))

                print(AnonymousUserMixin.get_id(self))

                print(current_user.get_id())

                # logging out if user already logged out

                s = self.app.get('/log-out', follow_redirects=False)

                self.assertEqual(s.status_code, 302)

    def test_logout_not_eccessed_if_not_logged_in(self):
        with self.app_context as c:

            c = self.app.get('/log-out', follow_redirects=False)

            self.assertEqual(c.status_code, 302)


