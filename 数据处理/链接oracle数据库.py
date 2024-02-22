import cx_Oracle as cx


class OracleConnection(object):
    def __init__(self,config):
        self.connection=cx.connect(config)
        self.cursor=self.connection.cursor()


    def queryAll(self,sql):
        self.cursor.execute(sql)
        values=self.cursor.fetchall()
        return type(values),values,values[0][0]

    def queryMany(self,sql,n):
        self.cursor.execute(sql)
        return self.cursor.fetchmany(n)


if __name__=='__main__':
    config="ACPBOOT/ACPBOOT@192.168.99.105:1521/ORCL"
    # config = {'dsn': '192.168.99.105:1521/ORCL','user': 'ACPBOOT', 'port': 'ACPBOOT'}

    osc=OracleConnection(config)
    sql="SELECT * FROM t_pa_product WHERE fname LIKE '319回归测试%'"
    print(osc.queryAll(sql))





