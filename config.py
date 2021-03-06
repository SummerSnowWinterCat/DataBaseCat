# -*- coding:utf-8 -*-
# @Time : 2020/10/07 20:36
# @Author: WinterCat
# @File : config.py
# @Email:summersnowwintercat@gmail.com

DB_CREATOR = 'pymysql'
DB_HOST = 'IP ADDRESS'
DB_POST = 3306
DB_NAME = 'DB_NAME'
DB_USER = 'USERNAME'
DB_PASSWORD = 'PASSWORD'

# encode
DB_CHARSET = 'utf8mb4'
# free cached min
DB_MIN_CACHED = 10
# free cached max
DB_MAX_CACHED = 22
#  pools create max
DB_MAX_CONNECTIONS = 100
#  share pool max
DB_MAX_SHARED = 20
# max pool block
DB_BLOCKING = True
#  connection use again
DB_MAX_USAGE = 0
# session
DB_SET_SESSION = []
# ping
DB_PING = 0
