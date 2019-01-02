import os
# python-dotenv 的用法
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

# 在这里设置你的变量
class Config(object):
    # 数据库相关
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you never guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or "mysql+pymysql://root:qwe123@127.0.0.1/microblog"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 邮件相关
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('TOKEN')
    ADMINS = [os.environ.get('ADMIN_LIST')]
    # celery 相关
    CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
    CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND')
    # 分页
    PAGINATE_PER_PAGE = 5


Configuration = {
    'dev':Config,
    'default':Config
}