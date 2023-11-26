import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)      #id de las tablas tiene que ser verdader
    name = Column(String(50), nullable=False)  #no puede ser null obligatorio
    email = Column(String(50), nullable=False) #(50) caracteres restringidos
    password = Column(String(250), nullable=False) #(250) para que cueste hackear
    
class Follower(Base):
    __tablename__ = 'follower'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    photo = Column(String(250))
    comment = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Post(Base):           #en mayuscula
    __tablename__ = 'post'  # en minuscula
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    photo = Column(String(250))
    comment = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Media(Base):           #en mayuscula
    __tablename__ = 'media'  # en minuscula
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    photo = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

class Comment(Base):           #en mayuscula
    __tablename__ = 'comment'  # en minuscula
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
