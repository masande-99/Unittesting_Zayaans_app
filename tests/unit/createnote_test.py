from unittest import TestCase
from website.views import home
from website import db
import main
from flask import current_app
import flask


class NoteTest(TestCase):
    def test_create_note(self):
        with flask.app.test_client as client:
            with current_app._get_current_object():
                new_note = home("Test")
                db.session.add(new_note)
                db.session.commit()
                self.assertIsNotNone(home.find_by_name("Test"))
