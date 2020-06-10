from app import db


class BaseModel:
    id = db.Column(db.Integer, primary_key=True)


class User(db.Model, BaseModel):
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'


class Task(db.Model, BaseModel):
    title = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(256), nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)
    is_accomplished = db.Column(db.Boolean, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Task {self.title}>'
