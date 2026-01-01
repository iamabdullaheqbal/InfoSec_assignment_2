from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    """
    User model for storing password hashes
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    password_hash = Column(String, nullable=False, index=True)
    
    def __repr__(self):
        return f"<User(id={self.id}, hash={self.password_hash[:10]}...)>"
