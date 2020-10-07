# -*- coding:utf-8 -*-
# @Time : 2020/10/07 20:24
# @Author: WinterCat
# @File : database_pool.py
# @Email:summersnowwintercat@gmail.com

import pymysql

from dbutils.pooled_db import PooledDB
import config


class DataBaseConnectionPool:
    try:
        __pool = None

        def __init__(self):
            self.conn = DataBaseConnectionPool.get_connection().connection()
            self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

        @staticmethod
        def get_connection():
            if DataBaseConnectionPool.__pool is None:
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

        def __exit__(self, exc_type, exc_val, exc_tb):
            self.conn.close()
            self.cur.close()

        # create add update delete
        def add_data(self, sql):
            count = self.cur.execute(sql)
            self.conn.commit()
            return count

        # search table data
        def search_data(self, sql):
            self.cur.execute(sql)
            return self.cur.fetchall()
    except Exception:
        print('ERROR')


# connection get
def get_connection():
    return DataBaseConnectionPool()
