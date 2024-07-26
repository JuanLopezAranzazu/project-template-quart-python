# from sqlalchemy import Column, Integer, String
# import db.db_config as db_config

# Base = db_config.Base

# # Modelo de usuario
# class User(Base):
#   __tablename__ = 'user'
#   id = Column(Integer, primary_key=True, autoincrement=True)
#   username = Column(String(50), unique=True)
#   email = Column(String(50), unique=True)

#   def __init__(self, username, email):
#     self.username = username
#     self.email = email

#   def __repr__(self):
#     return f'<User {self.username}>'
  

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer
import models.base_model as base_model

Base = base_model.Base

class User(Base):
  __tablename__ = 'user'
  id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
  username: Mapped[str] = mapped_column(String(length=50), unique=True, nullable=False)
  email: Mapped[str] = mapped_column(String(length=120), unique=True, nullable=False)

  def __init__(self, username: str, email: str):
    self.username = username
    self.email = email

  def __repr__(self):
    return f'<User {self.username}>'


