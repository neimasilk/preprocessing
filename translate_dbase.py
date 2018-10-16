import sqlite3
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/mukhlis/seq2seq-e71dee1db5ca.json"

from google.cloud import translate

translate_client = translate.Client()

filepath = 'indonesia_sentences_10.db'
try:
    db_connection = sqlite3.connect(filepath)
    db_cur = db_connection.cursor()
except Error as e:
    print(e)


sentences = []
db_cur.execute("select id, text_id, text_en_id, text_zhcn from id_zhcn where (text_en_id is NULL) or (text_zhcn is NULL) ")
textnya = db_cur.fetchall()

sql = ''' UPDATE id_zhcn
          SET text_en_id = ?, text_zhcn=?
          WHERE id = ? '''
for id in textnya:
    if (id[2] == None) or (id[3]==None):
        idnya = id[0]
        teks = id[1]
        if (id[2]==None):
            translation = translate_client.translate(
                teks,
                target_language='en', source_language='id')
            artinya = translation['translatedText']
        else:
            artinya = id[2]

        if (id[3]==None):
            translation = translate_client.translate(
                artinya,
                target_language='zh-CN', source_language='en')
            articn=translation['translatedText']
        else:
            articn = id[3]
        db_cur.execute(sql,[artinya,articn,idnya])
        db_connection.commit()
        print(idnya)



db_connection.close()