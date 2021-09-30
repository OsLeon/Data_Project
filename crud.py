from sqlalchemy.orm import Session
import models, schemas


# 通过id查询用户
def get_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# 写数据到数据库
def wirte_data(db: Session, user: schemas.User):
    db_user = models.User(id=user.id, platform=user.platform,userName=user.userName,companyName=user.companyName,intro=user.intro,phone=user.phone,mobile=user.phone,address=user.address,expiredTime=user.expiredTime,follows=user.follows,followers=user.followers,source=user.source,sourceDesc=user.sourceDesc,createTime=user.createTime)
    db.add(db_user)
    db.commit()  # 提交保存到数据库中
    db.refresh(db_user)  #刷新
    return db_user
