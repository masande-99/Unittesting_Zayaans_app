from tests.base_test import BaseTest
from flask import request
from flask_login import current_user, AnonymousUserMixin
from website.models import User
from tests.base_test import db


class TestLogIn(BaseTest):
    def test_sign_up_success(self):
        with self.app:
            response = self.app.post('/sign-up',
                                     data=dict(email="meh@gmail.com", firstName="Username", password1="1234yyy", password2="1234yyy"), follow_redirects=True)

            user = db.session.query(User).filter_by(email="meh@gmail.com").first()

            self.assertTrue(user)

            self.assertIn(b'Account created', response.data)
