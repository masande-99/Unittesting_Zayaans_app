from tests.base_test import BaseTest
from flask import request
from website.models import User
from tests.base_test import db


class TestSetting(BaseTest):
    def test_route_is_eccessible(self):
        with self.app:
            with self.app_context:

                response = self.app.post('/sign-up',
                                         data=dict(email="meh@gmail.com", firstName="Username", password1="1234yyy",
                                                   password2="1234yyy"), follow_redirects=True)

                user = db.session.query(User).filter_by(email="meh@gmail.com").first()

                self.assertTrue(user)

                self.assertIn(b'Account created', response.data)

                resp = self.app.post('/log-in',
                                     data=dict(email="meh@gmail.com", password="1234yyy"), follow_redirects=True)

                self.assertIn(b'Logged in successfully', resp.data)

                setting = self.app.get('/setting', follow_redirects=True)

                # Asserting that you are redirected to the setting page
                self.assertEqual('http://localhost/setting', request.url)


