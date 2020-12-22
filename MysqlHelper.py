# read and write mysql
import pymysql
import Sql





def __connect_mysql():
    """
    链接数据库
    :return:
    """
    return pymysql.connect(
        host='localhost',
        user='root',
        password='123456',
        db='mini',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )


def get_all_table():
    cnx = __connect_mysql()
    with cnx.cursor() as cursor:
        cursor.execute('show tables')

        for t in cursor.fetchall():
            print(t)
        pass
    pymysql.err
    cnx.close()


pass
