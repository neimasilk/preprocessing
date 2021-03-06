from translasi import translate_service
import sqlite3
from collections import deque


def translate_en(filepath):
    db_connection = sqlite3.connect(filepath)
    db_cur = db_connection.cursor()
    db_cur.execute(
        "select id, text_id, text_en_id, text_zhcn from id_zhcn where (text_zhcn is NULL) or (text_id is NULL) ")
    textnya = db_cur.fetchall()

    sql = ''' UPDATE id_zhcn
              SET text_zhcn = ?, text_id=?
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
        if (id[1] == None) or (id[3] == None):
            idnya = id[0]
            teks = id[2]
            while True:
                try:
                    if (id[1] == None):
                        arti_id = translate_service(teks, 'en', 'id', servis)
                    else:
                        arti_id = id[1]

                    if (id[3] == None):
                        arti_zhcn = translate_service(arti_id, 'en', 'zh-CN', servis)
                    else:
                        arti_zhcn = id[3]
                except Exception as e:
                    print(str(e))
                    print(wservice[0])
                    wservice.rotate(1)
                    # continue
                break
            wservice.rotate(1)
            servis = wservice[0]
            db_cur.execute(sql, [arti_zhcn, arti_id, idnya])
            db_connection.commit()
            print(idnya)

    db_connection.close()

if __name__ == '__main__':
    filedb = 'casict.db'
    translate_en(filedb)