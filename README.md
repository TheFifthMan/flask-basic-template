# Flask项目基本骨架
1. 配置文件： config.py 配置你的数据库，邮箱，分页等等
2. 启动文件: run.py 在这里引入各模块的models，设置上下文配置，初始化项目所需要的操作都可以在这里写函数完成
3. app/index 是蓝图，可以根据需求划分蓝图，一般有两种划分方法，一种是根据业务需求划分，比如这块是卖牙科保险，这块是卖老年保险。 一种是根据程序功能划分，这个是登陆认证模块，这个是用户操作模块等等
4. app/errors 是错误页面，错误返回处理的蓝图，可以在这里定义404/500/401等等状态的返回内容
5. 使用app.logger(e)即可记录log，这里设置了如果程序不是debug的形式即可进行记录log
6. .flaskenv 是flask的环境变量，这样每次运行的时候，你只需要 flask run 即可运行应用
7. requirements.txt 是依赖保存，按照下面做法即可按照所有需要的依赖。
```
python -m venv venv 
.\venv\Scripts\active
pip install -r requirements.txt
``` 

