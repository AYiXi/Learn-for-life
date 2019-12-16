import pymysql
import time

from settings_patent import (
    MYSQL_DBS
)

format_str_ = '{host:^30} | {category:^5} | {detail:^5} | {account:^20}'


class Mysql:
    def __init__(self, **kwargs):
        self.kwargs = kwargs or MYSQL_DBS['LOCAL_IPYJ']

        while True:
            try:
                self.db = pymysql.connect(
                    host=self.kwargs['HOST'],
                    port=self.kwargs['PORT'],
                    user=self.kwargs['USER'],
                    password=self.kwargs['PASSWORD'],
                    database=self.kwargs['DATABASE'],
                )
                self.cursor = self.db.cursor()
                break

            except pymysql.err.OperationalError:
                print(f'{self.kwargs["HOST"]} Database connection failed, try again.')

    def __repr__(self):
        return self.kwargs['HOST']

    def get_agency(self, account):
        # get agency by account
        sql_query_agency = f'''
            SELECT dept_name 
            FROM t_dept
            INNER JOIN t_ip_cpaccount_excel
            WHERE t_ip_cpaccount_excel.dept_id=t_dept.dept_id 
            AND t_ip_cpaccount_excel.account='{account}';'''

        self.cursor.execute(sql_query_agency)

        try:
            dept_agency = self.cursor.fetchone()[0]
        except:
            dept_agency = '天津市尚文知识产权代理有限公司'

        return dept_agency

    def get_user(self):
        self.cursor.execute('SELECT account, password, dept_id From `t_ip_cpaccount_excel`')
        data = self.cursor.fetchall()  # ((name, pwd, index),(name, pwd, index))
        users = [{'account': i[0],
                  'password': i[1],
                  'dept_id': i[2],
                  'index': str(index + 1)}
                 for index, i in enumerate(data)]

        return users

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db.close()

    def close(self):
        self.db.close()


if __name__ == '__main__':
    with Mysql(**MYSQL_DBS['YWSTWSB_33320']) as mysql:
        sql = '''SELECT * FROM t_ip_fee LIMIT  10'''

        mysql.cursor.execute(sql)
        datas = mysql.cursor.fetchall()
        print(datas[:10])
