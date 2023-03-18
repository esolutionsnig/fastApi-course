from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, String, text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("User")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    # first_name = Column(String, nullable=False)
    # last_name = Column(String, nullable=False)
    # phone_number = Column(String, nullable=False)
    # account_type = Column(String, nullable=True)
    # account_active = Column(Boolean, server_default='FALSE', nullable=True)
    # image_url = Column(String, nullable=True)
    # wallet_balance = Column(Integer, nullable=True, server_default='0')
    # pin = Column(Integer, nullable=True)
    # otp = Column(Integer, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))


class Vote(Base):
    __tablename__ = "votes"

    user_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey(
        "posts.id", ondelete="CASCADE"), primary_key=True)
