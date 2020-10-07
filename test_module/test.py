# -*- coding:utf-8 -*-
# @Time : 2020/10/07 21:04
# @Author: WinterCat
# @File : test.py
# @Email:summersnowwintercat@gmail.com
from database_service.database_pool import get_connection, DataBaseConnectionPool


def insert_some_thing():
    connection = get_connection()
    sql = '''
    CREATE TABLE IF NOT EXISTS sys(ID INT PRIMARY KEY AUTO_INCREMENT,message VARCHAR(50))
    '''

    return connection.insert_or_create(sql)


if __name__ == '__main__':
    print(insert_some_thing())
