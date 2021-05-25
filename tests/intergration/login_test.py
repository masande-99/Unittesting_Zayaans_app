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
