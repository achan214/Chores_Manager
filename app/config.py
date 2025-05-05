import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://localhost/chores_manager')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
