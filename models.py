from sqlalchemy import Column, Integer, String
from database import Base

#定义数据表格式
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    platform = Column(String(32), unique=True, index=True)
    userName = Column(String(30), nullable=False)
    companyName = Column(String(30), nullable=False)
    intro = Column(String(30), nullable=False)
    phone = Column(String(30), nullable=False)
    mobile = Column(String(30), nullable=False)
    address = Column(String(30), nullable=False)
    expiredTime = Column(String(30), nullable=False)
    follows = Column(String(30), nullable=False)
    followers = Column(String(30), nullable=False)
    source = Column(String(30), nullable=False)
    sourceDesc = Column(String(30), nullable=False)
    createTime = Column(String(30), nullable=False)
