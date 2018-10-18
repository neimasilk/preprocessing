import goslate
import sqlite3
import urllib
from collections import deque


# def findproxy():
#     with open('proxies.txt', "r") as f:
#         array = []
#         for line in f:
#             array.append(line)
#         proxies = []
#     for alamat in array:
#         proxies.append('http://' + alamat.split()[-1].replace('>', ''))
#
#     del array
#     for proks in proxies:
#         prox_dict = {"http": proks}
#         proxy = urllib.request.ProxyHandler(prox_dict)
#         opener = urllib.request.build_opener(proxy)
#         urllib.request.install_opener(opener)
#         try:
#             translator = goslate.Goslate(opener=opener)
#             item = "ini adalah percobaan"
#             translation = translator.translate(item, "en", 'id')
#
#         except:
#             print(proks)
#             continue
#
#         print(translation)
#         return prox_dict


def translate_proxy(text, source, target, proxy):
    proxy = urllib.request.ProxyHandler(proxy)
    opener = urllib.request.build_opener(proxy)
    urllib.request.install_opener(opener)
    translator = goslate.Goslate(opener=opener)
    item = text
    translation = translator.translate(item, target, source)
    return translation


filepath = 'indonesia_sentences_1000000.db'
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

wproxies = deque()
with open('working_proxy.txt', "r") as f:
    for line in f:
        wproxies.append(line)

def extract_proxy(alamat):
    # print(alamat)
    a = {"http": 'http://' + alamat.split()[-1].replace('>', '')}
    return a

proksi = extract_proxy(wproxies[0])
print(proksi)
print("ini adalah proxynya : {}".format(proksi))
wproxies.rotate(1)
proksi = extract_proxy(wproxies[0])
print(proksi)
# # print(translate_proxy('ini adalah kata yang akan diterjemahkan', 'id', 'en', proksi))
#
# for id in textnya:
#     if (id[2] == None) or (id[3] == None):
#         idnya = id[0]
#         teks = id[1]
#         while True:
#             try:
#                 if (id[2] == None):
#                     artinya = translate_proxy(teks, 'id', 'en', proksi)
#                 else:
#                     artinya = id[2]
#
#                 if (id[3] == None):
#                     articn = translate_proxy(artinya, 'en', 'zh-CN', proksi)
#                 else:
#                     articn = id[3]
#             except Exception as e:
#                 print(str(e))
#                 wproxies.rotate(1)
#                 proksi = extract_proxy(wproxies[0])
#                 print(proksi)
#                 continue
#             break
#         wproxies.rotate(1)
#         proksi = extract_proxy(wproxies[0])
#         db_cur.execute(sql, [artinya, articn, idnya])
#         db_connection.commit()
#         print(idnya)
#
# db_connection.close()
