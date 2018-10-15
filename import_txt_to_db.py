# buka file wiki indo

import sqlite3
import os

root_dir= '.'
sqlite_file = 'parallelcorpusdata'
table_name = 'id_zhcn'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()


# def input_data(namafile):
#     list_data =[]
#     dokumen = bs(buka_file_teks(namafile), 'lxml')
#     for link in dokumen.find_all('doc'):
#         id = link.get('id')
#         situs = link.get('url')
#         judul = link.get('title')
#         dokumen = link.text
#         ukuran = len(dokumen)
#         # print(perintah)
#         try:
#             c.execute("INSERT INTO wiki_id(situs, judul, dokumen, ukuran) VALUES (?,?,?,?)",(situs,judul,dokumen,ukuran))
#         except sqlite3.IntegrityError:
#             print('ERROR: ID already exists in PRIMARY KEY column {}')

def file_len(fname):
    with open(fname) as f:
        for i,l in enumerate(f):
            pass
        return i+1

def buka_file_teks(namafile):
    panjang = file_len(namafile)
    f=open(namafile,'r')
    teks=[]
    for baris in f:
        teks.append(baris)
    return teks, panjang

id_text, panjang_id = buka_file_teks("id_text.txt")
en_text, panjang_en = buka_file_teks("en_text.txt")
zhcn_text, panjang_zhcn = buka_file_teks("zhcn_text.txt")

if panjang_en==panjang_id==panjang_zhcn:
    for baris in range(panjang_id):
        print(id_text[baris],en_text[baris],zhcn_text[baris])
#     loop panjang masukkan kedalam database dengan insert into
        try:
            c.execute("INSERT INTO id_zhcn(text_id, text_en_id, text_en_zhcn, text_zhcn) VALUES (?,?,?,?)",(id_text[baris],en_text[baris],en_text[baris],zhcn_text[baris]))
        except sqlite3.IntegrityError:
            print('ERROR: ID already exists in PRIMARY KEY column {}')

else:
    print("tidak sama")
    print(panjang_zhcn,panjang_id,panjang_en)

conn.commit()
conn.close()
