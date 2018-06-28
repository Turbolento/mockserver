# mockserver
支持微服务consul架构的mockserver服务
## 部署到生产环境 ##
>需开启xsrf防护，用户session，需要nginx做转发,保证前后端cookie一致  

  
1. 进入到`/web`目录下：`cd web`  
1.1. 执行`npm install`，安装node依赖包  
1.2. 执行`npm run build`，编译生成dist文件夹

2. 进入`/server`目录下：`cd server`  
2.1. 修改mysql数据库配置：`config.yml`  
2.2. 初始化数据库：`python initDB.py`  
2.3. 初始化必须数据： `python apps/main/tests.py`
2.4. 运行服务器：`python server.py`

3. 安装Nginx  
3.1. 替换默认`nginx.conf`文件为`/nginx/nginx.conf`  
3.2. 修改nginx.conf中的dist目录为第1步中生成dist实际目录
3.3. 运行nginx  

4. 访问mockserver:  
4.1 地址为：[http://localhost/mockserver/](http://localhost/mockserver/)  
4.2 用户名/密码： admin/abc123456

## 开发环境调试 ##
>关闭后端服务器用户session验证、以及xsrf防护  

1. 进入`web`目录下，运行前端`npm run dev`  

2. 进入`server`目录下，  
2.1. 注释掉文件`apps/api/handlers.py`中的`BaseHandler`类中的`prepare`函数；  
2.2. 注释掉上述文件中的所有`@tornado.web.authenticated`
2.3. 运行服务器：`python server.py`

3. 访问mockserver:  
3.1. 地址为：[http://localhost:8080/mockserver/](http://localhost:8080/mockserver/)  
3.2. 用户名/密码： admin/abc123456