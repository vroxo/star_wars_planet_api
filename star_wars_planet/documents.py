from .app import db


class Planet(db.Document):
    name = db.StringField()
    climate = db.StringField()
    terrain = db.StringField()
