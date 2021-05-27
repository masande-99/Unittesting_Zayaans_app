from tests.base_test import BaseTest
from website.models import User, Note
from tests.base_test import db


class TestDeleteNote(BaseTest):

    def test_delete_note(self):
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

                risponce = self.app.get('/delete-note', follow_redirects=True)

                expected = {}

                notee = db.session.query(Note).filter_by(data="")

                self.assertTrue(notee)
                self.assertDictEqual({},expected)


