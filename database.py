from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#数据库连接地址信息，格式为：“mysql+pymysql://数据库用户名:密码@地址:端口/数据库名”
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:no996no996@127.0.0.1:3306/db"

# echo=True表示引擎将用repr()函数记录所有语句及其参数列表到日志
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, encoding='utf8', echo=True
)

# SQLAlchemy中，CRUD是通过会话进行管理的，所以需要先创建会话，
# 每一个SessionLocal实例就是一个数据库session
# flush指发送到数据库语句到数据库，但数据库不一定执行写入磁盘
# commit是指提交事务，将变更保存到数据库文件中
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建基本映射类
Base = declarative_base()