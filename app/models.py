from . import db
from datetime import datetime

class Group(db.Model):
    __tablename__ = 'group'

    group_id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String, unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    invite_code = db.Column(db.String)

    users = db.relationship('User', backref='group', lazy=True)
    chores = db.relationship('Chore', backref='group', lazy=True)

class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password_hash = db.Column(db.String)
    is_admin = db.Column(db.Boolean)
    group_id = db.Column(db.Integer, db.ForeignKey('group.group_id'))

    assignments = db.relationship('Assignment', backref='user', lazy=True)
    created_chores = db.relationship('Chore', backref='creator', foreign_keys='Chore.created_by_user_id')

class Chore(db.Model):
    __tablename__ = 'chore'

    chore_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    due_date = db.Column(db.Date)
    group_id = db.Column(db.Integer, db.ForeignKey('group.group_id'))
    created_by_user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    is_recurring = db.Column(db.Boolean)
    recurrence_pattern = db.Column(db.String)
    completed = db.Column(db.Boolean, default=False)
    completed_at = db.Column(db.DateTime)

    assignments = db.relationship('Assignment', backref='chore', lazy=True)

class Assignment(db.Model):
    __tablename__ = 'assignment'

    assignment_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    chore_id = db.Column(db.Integer, db.ForeignKey('chore.chore_id'))
    assigned_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_by_user = db.Column(db.Boolean, default=False)
