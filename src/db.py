from sqlalchemy import create_engine,  Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Solutions(Base):
  __tablename__ = 'solutions'

  id = Column(Integer, primary_key=True)
  solve = Column(String)

  def __repr__(self):
     return "<Solutions(id='%s', solve='%s')>" % (self.id, self.solutions)

engine = create_engine('postgresql+psycopg2://postgres:1234@db:5432/nqueen-db')
Session = sessionmaker(bind=engine)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
session = Session()