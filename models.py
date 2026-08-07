from sqlalchemy import Column, Integer, String, ForeignKey, Double
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    email = Column(String(254), index=True)
    password = Column(String(255), index=True)
    record = Column(Double)

class Friend(Base):
    __tablename__ = "Friends"

    id = Column(Integer, primary_key=True, index=True)
    user_id_1 = Column(Integer, ForeignKey("Users.id"))
    user_id_2 = Column(Integer, ForeignKey("Users.id"))

    # Отношение к первому пользователю
    user_1 = relationship("User", foreign_keys=[user_id_1])

    # Отношение ко второму пользователю
    user_2 = relationship("User", foreign_keys=[user_id_2])