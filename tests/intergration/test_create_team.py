from tests.base_test import BaseTest
from flask import request
from flask_login import current_user, AnonymousUserMixin
from website.models import User, Note, Work, Team
from tests.base_test import db


class TestMyTeam(BaseTest):

    def test_my_team(self):
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

                self.assertEqual(resp.status_code, 200)

                team = self.app.post('/my-team', data=dict(teamName="Team name"), follow_redirects=True)

                self.assertIn(b'Team added', team.data)

                # Asserting that you are redirected to the my team.html
                self.assertEqual('http://localhost/my-team', request.url)

                # testing team already in use
                team1 = self.app.post('/my-team', data=dict(teamName="Team name"), follow_redirects=True)

                self.assertIn(b'Team name is already in use', team1.data)

    def test_short_team_name(self):
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

                self.assertEqual(resp.status_code, 200)

                team = self.app.post('/my-team', data=dict(teamName="Te"), follow_redirects=True)

                self.assertIn(b'Please enter a longer name', team.data)

