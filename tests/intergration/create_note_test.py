from tests.base_test import BaseTest
from flask import request
from website.models import User, Note
from tests.base_test import db


class TestHome(BaseTest):

    def test_home_eccessebility(self):
        with self.app:
            with self.app_context:
                res = self.app.get('/', follow_redirects=True)

                self.assertEqual(res.status_code, 200)

    def test_create_note(self):
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

                res = self.app.post('/', data=dict(note="this is a test note"), follow_redirects=True)

                note = db.session.query(Note).filter_by(data="this is a test note")

                self.assertTrue(note)

                self.assertIn(b'Note added', res.data)

                # Asserting that you are redirected to the home page
                self.assertEqual('http://localhost/', request.url)

    def test_home_eccessebility_if_not_logged_in(self):
        with self.app:
            with self.app_context:
                res = self.app.get('/', data=dict(note="this is a test note"), follow_redirects=True)

                self.assertIn(b'Please log in to access this page', res.data)

                self.assertEqual(res.status_code, 200)

    def test_note_too_short(self):
        with self.app:
            with self.app_context:

                response = self.app.post('/sign-up',
                                         data=dict(email="meh@gmail.com", firstName="Username", password1="1234yyy",
                                                   password2="1234yyy"), follow_redirects=True)

                user = db.session.query(User).filter_by(email="meh@gmail.com").first()

                self.assertTrue(user)

                self.assertIn(b'Account created', response.data)

                resp = self.app.post('/log-in',
                                     data=dict(email="meh@gmail.com", password="1234yyy"),
                                     follow_redirects=True)

                self.assertIn(b'Logged in successfully', resp.data)

                self.assertEqual(resp.status_code, 200)

                res = self.app.post('/', data=dict(note=""),
                                    follow_redirects=True)

                note = db.session.query(Note).filter_by(data="")

                self.assertTrue(note)

                self.assertIn(b'Note is too short', res.data)



