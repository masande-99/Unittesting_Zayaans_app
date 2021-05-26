<<<<<<< HEAD
from tests.base_test import BaseTest


class TestLogOut(BaseTest):

    def test_logout(self):
        with self.app_context as c:
            c = self.app.get('/log-out', follow_redirects=True)

            self.assertEqual(c.status_code, 200)
=======
from tests.base_test import BaseTest


class TestLogOut(BaseTest):

    def test_logout(self):
        with self.app_context as c:
            c = self.app.get('/log-out', follow_redirects=True)

            self.assertEqual(c.status_code, 200)
>>>>>>> bb724ce9c88a0dfdc7dbd10307f9616a7e8a412c
