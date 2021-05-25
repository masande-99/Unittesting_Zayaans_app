from tests.base_test import BaseTest


class TestLogOut(BaseTest):

    def test_logout(self):
        with self.app_context as c:
            c = self.app.get('/log-out', follow_redirects=True)

            self.assertEqual(c.status_code, 200)
