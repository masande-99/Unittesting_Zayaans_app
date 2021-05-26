<<<<<<< HEAD
from tests.base_test import BaseTest
from flask import request
from flask_login import current_user, AnonymousUserMixin
from website.models import User
from tests.base_test import db


class TestLogIn(BaseTest):

    def test_sign_in(self):
        with self.app:
            with self.app_context:
                response = self.app.post('/sign-up',
                                         data=dict(email="meh@gmail.com", firstName="Username", password1="1234yyy", password2="1234yyy"), follow_redirects=True)

                user = db.session.query(User).filter_by(email="meh@gmail.com").first()

                self.assertTrue(user)

                self.assertIn(b'Account created', response.data)

                res = self.app.post('/log-in',
                                    data=dict(email="meh@gmail.com", password="1234yyy"), follow_redirects=True)

                self.assertIn(b'Logged in successfully', res.data)

                self.assertEqual(res.status_code, 200)

    def test_email_unknown(self):
        with self.app:
            with self.app_context:
                response = self.app.post('/sign-up',
                                         data=dict(email="meh@gmail.com", firstName="Username", password1="1234yyy", password2="1234yyy"), follow_redirects=True)

                user = db.session.query(User).filter_by(email="meh@gmail.com").first()

                self.assertTrue(user)

                res = self.app.post('/log-in',
                                    data=dict(email="mehi@gmail.com", password="1234yyy"), follow_redirects=True)

                self.assertIn(b'Email does not exist', res.data)

                self.assertEqual(res.status_code, 200)

                self.assertEqual('http://localhost/log-in', request.url)

    def test_invalid_password(self):
        with self.app:
            with self.app_context:
                response = self.app.post('/sign-up',
                                         data=dict(email="meh@gmail.com", firstName="Username", password1="1234yyy", password2="1234yyy"), follow_redirects=True)

                res = self.app.post('/log-in',
                                    data=dict(email="meh@gmail.com", password="123yy"))

                self.assertIn(b'alert', res.data)
=======
from tests.base_test import BaseTest
from flask import request
from flask_login import current_user, AnonymousUserMixin
from website.models import User
from tests.base_test import db


class TestLogIn(BaseTest):

    def test_sign_in(self):
        with self.app:
            with self.app_context:
                user = User(id=1, email="blabla@gmail.com", password="Test", first_name="joe", team_id=1, )
                db.session.add(user)

                user1 = User.query.filter_by(email="blabla@gmail.com").first()

                self.assertTrue(user1)

                res = self.app.post('/sign-in',
                                    data=dict(email="blabla@gmail.com", password="Test"))

                self.assertIn(b'<title>\nSign In\n</title>', res.data)
                print(res)

                # print(res)
                # self.assertIn(b'Logged in successfully', res.data)
>>>>>>> bb724ce9c88a0dfdc7dbd10307f9616a7e8a412c
