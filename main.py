from fastapi import FastAPI, Depends, HTTPException
import crud, schemas
from database import SessionLocal, engine, Base
from sqlalchemy.orm import Session
import uvicorn

#数据库初始化，如果没有库或者表，会自动创建
Base.metadata.create_all(bind=engine) 

#声明FastAPI实例
app = FastAPI()


# 数据库连接初始化
def get_db():
    """
    每一个请求处理完毕后会关闭当前连接，不同的请求使用不同的连接
    :return:
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 接口1:获取条目中用户id，与数据库对比，返回是否存在条目
@app.get("/user/{user_id}", response_model=schemas.User)
def read_id(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_id(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404,detail="User not found")
    return db_user



# 接口2:写入json文件到mysql数据库中
@app.post("/users/", response_model=schemas.User)
def wirte_data(user: schemas.User, db: Session = Depends(get_db)):
    return crud.wirte_data(db=db, user=user)



if __name__ == '__main__':
    uvicorn.run(app=app, host="127.0.0.1", port=8000)

