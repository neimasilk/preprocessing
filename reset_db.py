import sqlite3
from sqlite3 import Error

class ResetDb(object):

    sql_create_id_zhcn_table = """ CREATE TABLE IF NOT EXISTS "id_zhcn" (
        `id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        `text_id`	TEXT,
        `text_zhcn`	TEXT,
        `text_en_id`	TEXT,
        `text_en_zhcn`	TEXT,
        `tok_id`	TEXT,
        `tok_zhcn`	TEXT,
        `tok_en_id`	TEXT,
        `tok_en_zhcn`	TEXT
    ); """

    def __init__(self,f_data ="test_db.db"):
        self.filepath= f_data
        try:
            self._db_connection = sqlite3.connect(self.filepath)
            self._db_cur = self._db_connection.cursor()
        except Error as e:
            print(e)

    def query(self, query, params=""):
        return self._db_cur.execute(query, params)


    def create_id_zhcn(self):
        try:
            self._db_connection = sqlite3.connect(self.filepath)
            self._db_cur = self._db_connection.cursor()
            self.query(self.sql_create_id_zhcn_table)
        except Error as e:
            print(e)

    def clear_id_zhcn(self):
        sql_count = "SELECT count(*) FROM sqlite_master WHERE type='table' AND name='id_zhcn';"
        self.query(sql_count)
        hasil = self._db_cur.fetchone()
        if (hasil[0]==1):
            sql = 'DELETE FROM id_zhcn'
            self.query(sql)
        else:
            self.create_id_zhcn()

    def delete_db(self):
        import os
        myfile = self.filepath
        ## If file exists, delete it ##
        if os.path.isfile(myfile):
            os.remove(myfile)
        else:  ## Show an error ##
            print("Error: %s file not found" % myfile)


    def __del__(self):
        self._db_connection.close()


if __name__ == '__main__':
    reset_db = ResetDb('coba')
    reset_db.delete_db()