from unittest import TestCase
from website.models import Note, Work, User, Team


class TestModel(TestCase):
    def test_create_note(self):
        note = Note(id=1, data="Test", date=2021/5/20, user_id=1)

        self.assertEqual(note.data, "Test")
        self.assertEqual(note.user_id, 1)
        self.assertEqual(note.date, 2021/5/20)
        self.assertEqual(note.id, 1)

    def test_work_model(self):
        work = Work(id=1, title="Test client", description="Test description", date=2021/5/20, user_id=1, status="Test status", points=3)

        self.assertEqual(work.id, 1)
        self.assertEqual(work.title, "Test client")
        self.assertEqual(work.description, "Test description")
        self.assertEqual(work.date, 2021/5/20)
        self.assertEqual(work.user_id, 1)
        self.assertEqual(work.status, "Test status")
        self.assertEqual(work.points, 3)

    def test_user_model(self):
        user = User(id=1, email="blabla@gmail.com", password="Test", first_name="joe", team_id=1, )

        self.assertEqual(user.id, 1)
        self.assertEqual(user.email, "blabla@gmail.com")
        self.assertEqual(user.password, "Test")
        self.assertEqual(user.first_name, "joe")
        self.assertEqual(user.team_id, 1)

    def test_team_model(self):
        team = Team(id=1, name="Test")

        self.assertEqual(team.id, 1)
        self.assertEqual(team.name, "Test")
