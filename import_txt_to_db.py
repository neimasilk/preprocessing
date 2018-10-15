# buka file wiki indo

import sqlite3
import os

# root_dir= '.'
# sqlite_file = 'parallelcorpusdata'
# table_name = 'id_zhcn'
# conn = sqlite3.connect(sqlite_file)
# c = conn.cursor()

class ImportTxttoDB(object):
    def __init__(self, sqfile='parallelcorpusdata',tablename='id_zhcn',file_text1='id_text.txt',file_text2='en_text.txt',file_text3='zhcn_text.txt'):
        self.sqlite_file = sqfile
        self.table_name = tablename
        self.filetext1=file_text1
        self.filetext2=file_text2
        self.filetext3=file_text3
        try:
            self._db_connection = sqlite3.connect(sqfile)
            self._db_cur = self._db_connection.cursor()
        except Error as e:
            print(e)

    def file_len(self, fname):
        with open(fname) as f:
            for i,l in enumerate(f):
                pass
            return i+1

    def buka_file_teks(self, namafile):
        panjang = self.file_len(namafile)
        f=open(namafile,'r')
        teks=[]
        for baris in f:
            teks.append(baris)
        return teks, panjang

    def import_txt_to_db(self):
        id_text, panjang_id = self.buka_file_teks(self.filetext1)
        en_text, panjang_en = self.buka_file_teks(self.filetext2)
        zhcn_text, panjang_zhcn = self.buka_file_teks(self.filetext3)

        if panjang_en==panjang_id==panjang_zhcn:
            for baris in range(panjang_id):
                print(id_text[baris],en_text[baris],zhcn_text[baris])
                #     loop panjang masukkan kedalam database dengan insert into
                try:
                    self._db_cur.execute("INSERT INTO id_zhcn(text_id, text_en_id, text_en_zhcn, text_zhcn) VALUES (?,?,?,?)",(id_text[baris],en_text[baris],en_text[baris],zhcn_text[baris]))
                except self._db_connection.IntegrityError:
                    print("primary key error")
        else:
            print("tidak sama")
            print(panjang_zhcn,panjang_id,panjang_en)

    def __del__(self):
        self._db_connection.commit()
        self._db_connection.close()


if __name__ == '__main__':
    from reset_db import ResetDb
    reset_db=ResetDb('testparallel.db')
    reset_db.create_id_zhcn()
    import_text = ImportTxttoDB('testparallel.db')
    import_text.import_txt_to_db()