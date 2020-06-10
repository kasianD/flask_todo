import os 


class Configuration:
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
	SECRET_KEY = os.getenv('SECRET_KEY')
	# SQLALCHEMY_TRACK_MODIFICATIONS = True

