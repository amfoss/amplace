from dataclasses import dataclass
from datetime import datetime

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    SmallInteger,
    String,
    Table,
    create_engine,
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

from config import config, curr_env

engine = create_engine(config["SQL_URI"])
Session = sessionmaker(bind=engine)
Base = declarative_base()


@dataclass
class Pixel(Base):
    __tablename__ = "pixel"
    pid = Column(Integer, primary_key=True, autoincrement=True)
    x: int = Column(SmallInteger, default=None)
    y: int = Column(SmallInteger, default=None)
    color_hex: str = Column(String(30), default="#ffffff")
    user_id: str = Column(String(50), ForeignKey("user.username"), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user = relationship("User", back_populates="pixels")

@dataclass
class User(Base):
    __tablename__ = "user"
    username: str = Column(String(50), primary_key=True)
    count: int = Column(Integer, default=0)

    pixels = relationship("Pixel", back_populates="user")

Base.metadata.create_all(engine)

