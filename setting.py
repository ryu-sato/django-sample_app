from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

# mysqlのDBの設定
DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8' % (
    "root", # user_name
    "vagrant", # password
    "localhost", # host_ip
    "django_sample_app", # db_name
)
ENGINE = create_engine(
    DATABASE,
    encoding = "utf-8",
    echo=True # Trueだと実行のたびにSQLが出力される
)

# Sessionの作成
Session = scoped_session(
  # ORM実行時の設定。自動コミットするか、自動反映するなど。
  sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = ENGINE
  )
)
session = Session()

# modelで使用する
Base = declarative_base()
Base.query = Session.query_property()
