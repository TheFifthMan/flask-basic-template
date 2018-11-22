import os

# 在这里设置你的变量
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you never guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or "mysql+pymysql://root:qwe123@127.0.0.1/microblog"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('TOKEN')
    ADMINS = [os.environ.get('ADMIN_LIST')]
    PAGINATE_PER_PAGE = 5
    LANGUAGES = ['en','es','zh']


Configuration = {
    'dev':Config,
    'default':Config
}