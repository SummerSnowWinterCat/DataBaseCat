# -*- coding:utf-8 -*-
# @Time : 2020/10/07 20:24
# @Author: WinterCat
# @File : database_pool.py
# @Email:summersnowwintercat@gmail.com

import pymysql
from dbutils.pooled_db import PooledDB
import config


# pools
class DataBaseConnectionPool:
    __pool = None

    # init database connection
    def __init__(self):
        self.conn = self.get_connection().connection()
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)

    # connection create and create config from config.py
    def get_connection(self):
        if self.__pool is None:
            __pool = PooledDB(
                creator=pymysql,
                maxconnections=config.DB_MAX_CONNECTIONS,
                mincached=config.DB_MIN_CACHED,
                maxcached=config.DB_MAX_CACHED,
                maxshared=config.DB_MAX_SHARED,
                blocking=config.DB_BLOCKING,
                maxusage=config.DB_MAX_USAGE,
                setsession=config.DB_SET_SESSION,
                ping=config.DB_PING,
                host=config.DB_HOST,
                user=config.DB_USER,
                password=config.DB_PASSWORD,
                database=config.DB_NAME,
                charset=config.DB_CHARSET
            )
        return __pool

    # connection auto close
    def __del__(self):
        self.cur.close()
        self.conn.close()


# search database by query
def search_data(query):
    connection = DataBaseConnectionPool()
    connection.cur.execute(query)
    return connection.cur.fetchall()


# insert data by query
def update_data(query):
    connection = DataBaseConnectionPool()
    connection.cur.execute(query)
    return connection.conn.commit()
