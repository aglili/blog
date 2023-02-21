from sqlalchemy import Column,Integer,String
import database

class Blog(database.Base):
    __tablename__ = 'blog'
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    content = Column(String)