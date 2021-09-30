from pydantic import BaseModel
from sqlalchemy.sql.elements import BinaryExpression
from sqlalchemy.sql.schema import ColumnDefault
from starlette.types import Message

#定义请求返回schmas
class User(BaseModel):
    id: int
    platform: str
    userName: str
    companyName: str 
    intro: str 
    phone: str 
    mobile: str 
    address: str 
    expiredTime: str 
    follows: str 
    followers: str 
    source: str 
    sourceDesc: str 
    createTime: str 
    class Config:
        orm_mode = True
