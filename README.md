# 这是一个基于VUE2+DRF搭建的框架

## 说明

目前笔者基于的css框架仅为element-ui，没有使用预处理语言（诸如less，scss等）以及其他的css框架（诸如bootstrap等），当然也不是从纯html底层开始进行的书写；


## 这个框架能做什么

并不能做什么，因为这只是一个已经配置好vue2和drf基本需求的一个开源项目，其中已经配置并且简单应用了vuex，router等知识，同时已经解决了前后端跨域的问题，基本上可以说，在这个项目中你只需要执行如下的几个命令

后端文件夹——backproject

```
python manange.py runserver
python manage.py makemigrations
python manage.py migrate
```

前端文件夹——frontproject

```
npm run serve
```

而后在浏览器中输入 ``127.0.0.1:8080``回车即可进入到网站呈现页面，注意，不能输入 ``localhost:8080``尽管二者理论上等价，由于DRF近乎变态的要求您并不能如此做除非您手动修改了后端项目中settings.py中的跨域配置项。


## 框架功能说明

在这里，您将首先看到一个简单地认证登录系统，进行注册登录后即可看到管理面板；在管理面板内，提供了可以测试DRF内部用户数据库以及自定义创建的用户数据库的相关接口，以及一个基于FBV实现的比较没用的API接口，您可以尝试使用它们进行前后端交互的微型实验。
