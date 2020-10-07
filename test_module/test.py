# -*- coding:utf-8 -*-
# @Time : 2020/10/07 21:04
# @Author: WinterCat
# @File : test.py
# @Email:summersnowwintercat@gmail.com
from database_service.database_pool import get_connection, DataBaseConnectionPool


def create_table():
    sql = '''
    CREATE TABLE IF NOT EXISTS sys(ID INT PRIMARY KEY AUTO_INCREMENT,message VARCHAR(50))
    '''

    return get_connection().add_data(sql=sql)


if __name__ == '__main__':
    print(create_table())
