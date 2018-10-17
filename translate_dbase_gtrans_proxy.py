import googletrans
import sqlite3


def findproxy():
    with open('proxies.txt', "r") as f:
        array = []
        for line in f:
            array.append(line)
        proxies = []
    for alamat in array:
        proxies.append('http://' + alamat.split()[-1].replace('>', ''))

    del array
    for proxy in proxies:
        prox_dict = {"http": proxy}
        try:
            translator = googletrans.Translator(proxies=prox_dict)  # type: string
            item = "ini adalah percobaan"
            translation = translator.translate(item, "en", 'id').text

        except:
            print(proxy)
            continue

        print(translation)
        return prox_dict
        



def translate_proxy(text, source, target, proxy):
    translator = googletrans.Translator(proxies=proxy)
    item = text
    translation = translator.translate(item, target, source).text
    return translation


filepath = 'indonesia_sentences_10.db'
try:
    db_connection = sqlite3.connect(filepath)
    db_cur = db_connection.cursor()
except Error as e:
    print(e)

sentences = []
db_cur.execute(
    "select id, text_id, text_en_id, text_zhcn from id_zhcn where (text_en_id is NULL) or (text_zhcn is NULL) ")
textnya = db_cur.fetchall()

sql = ''' UPDATE id_zhcn
          SET text_en_id = ?, text_zhcn=?
          WHERE id = ? '''

proksi = findproxy()
print("ini adalah proxynya : {}".format(proksi))
print(translate_proxy('ini adalah kata yang akan diterjemahkan', 'id', 'en', proksi))

for id in textnya:
    if (id[2] == None) or (id[3]==None):
        idnya = id[0]
        teks = id[1]
        while True:
            try:
                if (id[2]==None):
                    artinya=translate_proxy(teks,'id','en',proksi)
                else:
                    artinya = id[2]

                if (id[3]==None):
                    articn = translate_proxy(artinya,'en','zh-CN',proksi)
                else:
                    articn = id[3]
            except:
                proksi = findproxy()
                continue
            break
        db_cur.execute(sql,[artinya,articn,idnya])
        db_connection.commit()
        print(idnya)

db_connection.close()
