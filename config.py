import os

basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'admin123'
OPENID_PROVIDERS = [
    {'name': 'viktor', 'password': 'viktor'},
]

SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/medserve'
