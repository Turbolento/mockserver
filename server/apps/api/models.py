#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from sqlalchemy import Table
from sqlalchemy import Column,String,Integer,Text,ForeignKey,Boolean
#常用字段类型有String,Integer，Text，Boolean，SmallInteger，DateTime
from sqlalchemy.orm import relationship
from setting import Base

##在下面创建你的数据对象模型
