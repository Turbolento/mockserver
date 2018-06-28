#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from setting import engine
from sqlalchemy.orm import sessionmaker
from apps.main.xx_models import *

Session = sessionmaker(bind=engine)
session = Session()

usera = User(username='a',password='b',email='ab@c.com')
userb = User(username='a2',password='b2',email='ab2@c.com')
userlist = [usera,userb]


############增加数据#########
#单条
session.add(usera)
#多条
session.add_all(userlist)
#提交
session.commit()


############查询数据#########
#根据id查询
uid = 1    #要查询用户ID
session.query(User).get(uid)
#指定字段查询,first()返回第一条结果
#单字段查询
session.query(User).filter_by(User.username=='a').first()
#多字段联合查询,filter后面一定要加上all()或者first(),不然只返回SQL查询语句
session.query(User).filter(username='a',id='1').all()
#查询所有结果
session.query(User).all()


############更新数据#########
a = session.query(Article).get(10)
#以下操作根据需要修改
a.title = 'new title'
a.tags.append(Tag(name='python'))    #一对多或者多对多中添加新值

session.add(a)
session.commit()

############删除数据############
a = session.query(Article).get(10)
session.delete(a)
session.commit()


####################################
#            修改表结构
####################################
#使用Alembic 或者 SQLAlchemy-Migrate
