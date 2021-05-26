<<<<<<< HEAD
from tests.base_test import BaseTest, db, app
from website.models import Note, Work, User, Team


class TestModelIsCrud(BaseTest):
    def test_note_crud(self):
        with self.app_context:
            note = Note(data="Test")

            results = db.session.query(Note).filter_by(data="Test").first()
            self.assertIsNone(results)

            db.session.add(note)
            db.session.commit()

            self.assertIsNotNone(db.session.query(Note).filter_by(data="Test").first())

            db.session.delete(note)
            db.session.commit()

            self.assertIsNone(db.session.query(Note).filter_by(data="Test").first())

    def test_work_crud(self):
        with self.app_context:
            work = Work(title="Test title")

            self.assertIsNone(db.session.query(Work).filter_by(title="Test title").first())

            db.session.add(work)
            db.session.commit()

            self.assertIsNotNone(db.session.query(Work).filter_by(title="Test title").first())

            db.session.delete(work)

            self.assertIsNone(db.session.query(Work).filter_by(title="Test title").first())

    def test_user_crud(self):
        with self.app_context:
            user = User(email="blabla@gmail.com")

            self.assertIsNone(db.session.query(User).filter_by(email="blabla@gmail.com").first())

            db.session.add(user)
            db.session.commit()

            self.assertIsNotNone(db.session.query(User).filter_by(email="blabla@gmail.com").first())

            db.session.delete(user)
            db.session.commit()

            self.assertIsNone(db.session.query(User).filter_by(email="blabla@gmail.com").first())

    def test_team_crud(self):
        with self.app_context:
            team = Team(name="My team")

            self.assertIsNone(db.session.query(Team).filter_by(name="My team").first())

            db.session.add(team)
            db.session.commit()

            self.assertIsNotNone(db.session.query(Team).filter_by(name="My team").first())

            db.session.delete(team)
            db.session.commit()

            self.assertIsNone(db.session.query(Team).filter_by(name="My team").first())
=======
from tests.base_test import BaseTest, db, app
from website.models import Note, Work, User, Team


class TestModelIsCrud(BaseTest):
    def test_note_crud(self):
        with self.app_context:
            note = Note(data="Test")

            results = db.session.query(Note).filter_by(data="Test").first()
            self.assertIsNone(results)

            db.session.add(note)
            db.session.commit()

            self.assertIsNotNone(db.session.query(Note).filter_by(data="Test").first())

            db.session.delete(note)
            db.session.commit()

            self.assertIsNone(db.session.query(Note).filter_by(data="Test").first())

    def test_work_crud(self):
        with self.app_context:
            work = Work(title="Test title")

            self.assertIsNone(db.session.query(Work).filter_by(title="Test title").first())

            db.session.add(work)
            db.session.commit()

            self.assertIsNotNone(db.session.query(Work).filter_by(title="Test title").first())

            db.session.delete(work)

            self.assertIsNone(db.session.query(Work).filter_by(title="Test title").first())

    def test_user_crud(self):
        with self.app_context:
            user = User(email="blabla@gmail.com")

            self.assertIsNone(db.session.query(User).filter_by(email="blabla@gmail.com").first())

            db.session.add(user)
            db.session.commit()

            self.assertIsNotNone(db.session.query(User).filter_by(email="blabla@gmail.com").first())

            db.session.delete(user)
            db.session.commit()

            self.assertIsNone(db.session.query(User).filter_by(email="blabla@gmail.com").first())

    def test_team_crud(self):
        with self.app_context:
            team = Team(name="My team")

            self.assertIsNone(db.session.query(Team).filter_by(name="My team").first())

            db.session.add(team)
            db.session.commit()

            self.assertIsNotNone(db.session.query(Team).filter_by(name="My team").first())

            db.session.delete(team)
            db.session.commit()

            self.assertIsNone(db.session.query(Team).filter_by(name="My team").first())
>>>>>>> bb724ce9c88a0dfdc7dbd10307f9616a7e8a412c
