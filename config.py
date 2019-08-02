import os 
basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
	MAIL_SERVER = 'smtp.qq.com'
	MAIL_PORT = 25
	# MAIL_USE_TLS = True
	MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
	FLASKY_MAIL_SENDER = '1257699625@qq.com'
	FLASKY_ADMIN = os.environ.get('FLASK_ADMIN')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	@staticmethod
	def init_app(app):
		pass
class DevelopmentConfig(Config):
	DEBUG=True
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' +os.path.join(basedir, 'data-dev.sqlite')

class TestginConfig(Config):
	Testing=True
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEST_DATABASE_URL') or 'sqlite://' 

class ProductionConfig(Config):
		SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' +os.path.join(basedir, 'data.sqlite')

config = {
	'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
}