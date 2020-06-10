from app import db
from sqlalchemy.sql import expression

class BaseModel:
    id = db.Column(db.Integer, primary_key=True)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def save(self):
        db.session.commit()
        return self


class User(db.Model, BaseModel):
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'


class Task(db.Model, BaseModel):
    title = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(256), nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)
    is_accomplished = db.Column(db.Boolean)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Task {self.title}>'

    def delete(self):
        db.session.delete(self)
        db.session.commit()