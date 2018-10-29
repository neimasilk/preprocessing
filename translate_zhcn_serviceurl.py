# import goslate
from translasi import  translate_service
import sqlite3
import urllib
from collections import deque
import subprocess
import shlex

# def translate_service(text, source, target, service=''):
#     item = text
#     if service=='':
#         a = 'http://translate.google.cn'
#         translator = goslate.Goslate(service_urls=(a,))
#     else:
#         translator = goslate.Goslate(service_urls=(service,))
#     translation = translator.translate(item, target, source)
#     return translation


filepath = 'mandarin_sentences_1000000.db'
try:
    db_connection = sqlite3.connect(filepath)
    db_cur = db_connection.cursor()
except Exception as e:
    print(e)

sentences = []
db_cur.execute(
    "select id, text_id, text_en_id, text_zhcn from id_zhcn where (text_en_id is NULL) or (text_id is NULL) ")
textnya = db_cur.fetchall()

sql = ''' UPDATE id_zhcn
          SET text_en_id = ?, text_id=?
          WHERE id = ? '''

wservice = deque()
with open('googledomain.txt', "r") as f:
    for gdomain in f:
        line = 'http://translate.'+gdomain
        wservice.append(line.strip())


servis = wservice[0]
print(translate_service('ini adalah kata yang akan diterjemahkan tanpa servis', 'id', 'en'))
# print(str(servis))

while True:
    try:
        print(translate_service('ini adalah kata yang akan diterjemahkan dengan servis', 'id', 'en', servis))
    except Exception as e:
        print(str(e))
        wservice.rotate(1)
        servis = wservice[0]
        continue
    break


for id in textnya:
    if (id[2] == None) or (id[3] == None):
        idnya = id[0]
        teks = id[3]
        while True:
            try:
                if (id[2] == None):
                    artinya = translate_service(teks, 'zh-CN', 'en', servis)
                else:
                    artinya = id[2]

                if (id[1] == None):
                    artiid = translate_service(artinya, 'en', 'id', servis)
                else:
                    artiid = id[1]
            except Exception as e:
                print(str(e))
                print(wservice[0])
                wservice.rotate(1)
                continue
            break
        wservice.rotate(1)
        db_cur.execute(sql, [artinya, artiid, idnya])
        db_connection.commit()
        print(idnya)

db_connection.close()
