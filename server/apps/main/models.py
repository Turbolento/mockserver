#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from sqlalchemy import Table
from sqlalchemy import Column,String,Integer,Text,ForeignKey,Boolean,DateTime
#常用字段类型有String,Integer，Text，Boolean，SmallInteger，DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from setting import Base

class Project(Base):
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False, index=True)
    description = Column(String(64))
    modules = relationship('Module', backref='project')                                         #一对多
    owner_id = Column(Integer, ForeignKey('user.id'))                                            #多对一
    members = relationship('User', secondary='project_user', backref='authorized_projects')      #多对多
    createtime = Column(DateTime, default=datetime.now)
    apis = relationship('Api', backref='project')  # 一对多


class Module(Base):
    __tablename__ = 'module'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False, index=True)
    project_id = Column(Integer, ForeignKey('project.id'))              #多对一
    apis = relationship('Api', backref='module')                         #一对多


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    account = Column(String(64), nullable=False, index=True)
    name = Column(String(64), index=True)
    passwd = Column(String(1024), nullable=False)
    email = Column(String(64))
    role = Column(Integer, nullable=False)  # 管理员：100    普通用户：900    游客：999
    status = Column(Boolean(), default=True)
    own_projects = relationship('Project', backref='owner')

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.account)

project_user = Table(
    'project_user', Base.metadata,
    Column('project_id', Integer, ForeignKey('project.id')),
    Column('user_id', Integer, ForeignKey('user.id'))
)

class Api(Base):
    __tablename__ = 'api'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    service_name = Column(String(128))
    uri = Column(String(256))
    request_content_type = Column(String(64))
    request_method = Column(String(64))
    description = Column(String(128))
    paras = relationship('RequestPara', backref='api')            #一对多
    responseheader = relationship('ResponseHeader', backref='api')      # 一对多
    module_id = Column(Integer, ForeignKey('module.id'))              #多对一
    project_id = Column(Integer, ForeignKey('project.id'))              #多对一,
    response_set = relationship('Response', backref='api')     #一对多,响应集

class RequestPara(Base):
    __tablename__ = 'requestpara'
    id = Column(Integer, primary_key=True)
    order = Column(Integer,nullable=False)
    name = Column(String(64))                   #参数名称
    match = Column(Integer,default=0)             #值匹配条件：["等于","包含","大于","小于","开始于","结束于","任意值"]  对应该数组中的下标值
    value = Column(String(256))
    position = Column(String(10))                    #参数所在位置：header/body
    response_id = Column(Integer, ForeignKey('response.id'))               #多对一
    api_id = Column(Integer, ForeignKey('api.id'))               #多对一

class ResponseType(Base):
    __tablename__ = 'responsetype'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)
    value = Column(String(64), nullable=False)
    responses = relationship('Response', backref='type')        #一对多

class Response(Base):
    __tablename__ = 'response'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, index=True)
    description = Column(String(128))
    status_code = Column(Integer, default=200)
    response_content = Column(Text(10000), nullable=False)
    type_id = Column(Integer, ForeignKey('responsetype.id'))
    paras = relationship('ResponseType', backref='response')  # 一对多
    api_id = Column(Integer, ForeignKey('api.id'))      # 多对一

class ResponseHeader(Base):
    __tablename__ = 'responseheader'
    id = Column(Integer, primary_key=True)
    key = Column(String(64), nullable=False)
    value = Column(String(256), nullable=False)
    description = Column(String(128))
    api_id = Column(Integer, ForeignKey('api.id'))  # 多对一


class Consul(Base):
    __tablename__ = 'consul'
    id = Column(Integer, primary_key=True)
    ip = Column(String(64), nullable=False)
    port = Column(Integer,default=8500)
    desc = Column(String(128))


class RequestService(Base):
    __tablename__ = 'requestService'
    id = Column(Integer, primary_key=True)
    serviceName = Column(String(128), nullable=False)
    consul_ip = Column(String(128), nullable=False)
    consul_port = Column(String(128), nullable=False)