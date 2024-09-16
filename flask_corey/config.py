import os

class Config:
    SECRET_KEY = '72f77406a88101afe69ae3520daa7468'

    # The below line is giving error. It is not able to
    # access the key from environment variables.
    # SECRET_KEY = os.environ.get('SECRET_KEY_FLASK_DB')
    
    # The below code did not create database in the current directory.
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    db_path = os.path.join(os.path.dirname(__file__), 'site.db')
    db_uri = 'sqlite:///{}'.format(db_path)
    SQLALCHEMY_DATABASE_URI = db_uri
    
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = '587'
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')