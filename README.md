# Data_Project

## 数据爬取项目

# 一.项目介绍

实现数据爬取后数据简单判断分析以及写入数据库，接口是restful风格的API，后期会不定期更新新的API和前段数据抓取代码

### python环境为3.8.11

目前实现两个接口：

接口1:获取条目中用户id，与数据库对比，返回是否存在条目

接口2:写入json文件到mysql数据库中


# 二.部署

1.下载代码到本地

```
git clone git@github.com:OsLeon/Data_Project.git
```

2.安装数据库连接组件pymysql，其他依赖包根据代码要求安装

```
pip install pymysql -y
```
3.部署前需要提前创建好mysql数据库，设置好账号密码等连接信息，并在database.py中修改数据库连接信息

```
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:xxxxxxx@127.0.0.1:3306/xxx"
```

4.启动服务：

在主目录下运行以下代码启动后端：

```
uvicorn main:app --reload
```






