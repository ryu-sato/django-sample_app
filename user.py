from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from setting import Base
from setting import ENGINE
import sys

class User(Base):
  __tablename__ = 'users'
  
  id = Column('id', Integer, primary_key = True)
  name = Column('name', String(200))
  version_id = Column(BigInteger, nullable=False)

  __mapper_args__ = {
    'version_id_col': version_id
  }

def main(args):
  Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
  main(sys.argv)
