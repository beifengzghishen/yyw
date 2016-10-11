#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/9/27 0027 20:00
# @Author  : zzs
# @Site    :
# @File    : user_modle.py
# @Software: PyCharm

from flask import Flask,request,render_template,flash
from user_modle import User  #导入User类
#  引入模块render_template，这个主要是返回模板要用的方法
#  模块flash，是异常处理要用的模板

app = Flask(__name__)
app.secret_key="123"


@app.route('/')
def hello_world():
    content="hello word!"
    return render_template('index.html',content=content)
"""
引入rander_template，即把jinjia2这个模板引入到py文件中，
rander_template，括号里第一个是html文件，后面是键值对，表示要替换的文件
index.html文件中，用{{}}，双花括号表示要替换的文件
"""
@app.route('/ff')
def hell_ff():
    flash(u"你好，周")
    return render_template('index1.html')


@app.route("/user")
def user_index():
    user=User(1,u"学习Flask")    #一定要加上u，否则中文字符引起乱码，返回500错误。
    return render_template("user_index.html", user=user)







@app.route('/user0' )
def hello_user():
    return "hello user"

#设置发送模式为POST

@app.route('/user1/<id>')
def user_id(id):
    return  "hello user"+id

@app.route('/query_user/<user_id>')
def query_user(user_id):
    user=None
    if int(user_id)==1:
        user=User(1,u"这是什么东西，到底有什么用？")
    return render_template("user_id.html",user=user)

"""
这一段的作用是，判断，如果我这里有1这个用户，返回有这个用户的名字，
如果没有，返回没有

"""

@app.route('/users')
def user_list():
    users=[]
    for i in range(1,62000):
        user=User(i,u"名字"+str(i))
        users.append(user)

    return render_template("user_list.html",users=users)
"""
这里演示模板中循环的用法
"""

@app.route("/one")
def base_onr():
    return  render_template("base_one.html")

@app.route("/two")
def base_two():
    return  render_template("base_two.html")

if __name__ == '__main__':
    app.run()
