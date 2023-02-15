#!/usr/bin/env python
# encoding: utf-8
'''
@Time: 2023/2/15 11:36
@Project: R_jyyx 
@File: run.py
@Author: R_记忆犹新
@Software: pycharm
@Desc:
'''
from main import app

if __name__ == "__main__":
    app.debug = app.config['DEBUG']
    app.run()