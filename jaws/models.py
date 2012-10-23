from sqlalchemy import Column, Integer, String, Text
from jaws.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    description = Column(Text())
    blocks = relationship("Block", backref="user")

    def __init__(self, title=None, description=None):
        self.title = title
        self.description = description

    def __repr__(self):
        return '<Post %r>' % (self.title)


class Block(Base):
    __tablename__ = 'blocks'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    content = Column(Text())
    image = Column(String(255))
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship("Post", primaryjoin=post_id == Post.id)

    def __init__(self, title=None, content=None, image=None):
        self.title = title
        self.content = content
        self.image = image

    def __repr__(self):
        return '<Block %r>' % (self.title)
