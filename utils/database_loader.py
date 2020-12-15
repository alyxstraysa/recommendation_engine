import psycopg2 as pg


class DB_Loader():
    db_conn = None
    db_curs = None

    def connectDB(self):
        self.conn = pg.connect(
            host = 'ec2-54-205-248-255.compute-1.amazonaws.com',
            dbname = 'd2a6ovipdc1kil',
            user = 'syaiorwmvigslx' ,
            password = '260b5b87a450bcbeb6d122e875c6d9e83fba60e670a56964d89d8a4d2c492f88',
            port = '5432')
        self.db_curs = self.conn.cursor()

    def createTables(self):
        self.db_curs.execute('CREATE TABLE animes (anime_id INTEGER PRIMARY KEY);')
        self.db_curs.execute('CREATE TABLE users (user_id INTEGER PRIMARY KEY);')

    def showTables(self):
        self.db_curs.execute('SELECT * FROM pg_catalog.pg_tables;')

    def closeConnect(self):
        self.db_curs.close()

if __name__ == '__main__':
    db_loader = DB_Loader()
    db_loader.connectDB()
    #db_loader.createTables()
    db_loader.showTables()
    db_loader.closeConnect()
