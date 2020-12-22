# read and write mysql
import pymysql
import Sql

LOCAL_HOST = ''
USER = ''
PASSWORD = ''
DB = ''


def __connect_mysql() -> pymysql.Connection:
    """
    链接数据库
    :return:
    """

    cnx = None
    try:
        cnx = pymysql.connect(
            host='localhost',
            user='root',
            password='123456',
            db='mini',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
    except pymysql.Error as err:
        cnx.close()
        assert False, err
        pass
    return cnx


def get_all_table() -> []:
    """
    获取所有数据表根据库
    :return:
    """
    table_name_list = []
    cnx = __connect_mysql()
    with cnx.cursor() as cursor:
        cursor.execute('show tables')
        cursor.fetchall()
        pass
    cnx.close()
    return table_name_list


def get_table_by_table_name(table_name: str):
    """
    获取 表数据 根据 table_name
    :param table_name:
    :return:
    """
    assert table_name != '', 'table name is empty.'
    cnx = __connect_mysql()
    with cnx.cursor() as cursor:
        cursor.execute(Sql.SELECT_TABLE % table_name)

        pass
    cursor.close()
    pass


def get_table_by_table_name_and_uid(table_name: str, uid: str) -> [dict]:
    """
    获取 表数据 根据 table name 和 uid
    :param table_name:
    :param uid:
    :return:
    """
    result = None
    assert table_name != '' and uid != '', 'table name or uid is empty'
    cnx = __connect_mysql()
    with cnx.cursor() as cursor:
        cursor.execute(Sql.SELECT_TABLE_WHERE_UID % (table_name, uid))
        result = cursor.fetchall()
    cnx.close()
    return result




