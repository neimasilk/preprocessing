import goslate
import sqlite3
import urllib
from collections import deque
import subprocess
import shlex

def translate_proxy(text, source, target, proxy=''):
    item = text
    if proxy=='':
        translator = goslate.Goslate(service_urls=('http://translate.google.com.hk',))
    else:
        proxy = urllib.request.ProxyHandler(proxy)
        opener = urllib.request.build_opener(proxy)
        urllib.request.install_opener(opener)
        translator = goslate.Goslate(opener=opener)
    translation = translator.translate(item, target, source)
    return translation


filepath = 'mandarin_sentences_10.db'
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
while True:
    try:
        print(translate_proxy('ini adalah kata yang akan diterjemahkan', 'id', 'en', proksi))
    except Exception as e:
        print(str(e))
        wproxies.popleft()
        if len(wproxies) == 0:
            print("proxy habis!")
            exit()
        proksi = extract_proxy(wproxies[0])
        continue
    break


for id in textnya:
    if (id[2] == None) or (id[3] == None):
        idnya = id[0]
        teks = id[3]
        while True:
            try:
                if (id[2] == None):
                    artinya = translate_proxy(teks, 'zh-CN', 'en', proksi)
                else:
                    artinya = id[2]

                if (id[1] == None):
                    artiid = translate_proxy(artinya, 'en', 'id', proksi)
                else:
                    artiid = id[1]
            except Exception as e:
                print(str(e))
                wproxies.popleft()
                if len(wproxies)==0:
                    print("proxy habis!")
                    subprocess.call(shlex.split("proxybroker find --types HTTP --lvl High --countries US CA FR GB DE SG --strict -l 300 -o ./proxies.txt"))
                    subprocess.call(shlex.split("mv working_proxy.txt working_proxy%s.txt" % idnya))
                    subprocess.call(shlex.split("python proxy_finder.py"))
                    # exit()
                    with open('working_proxy.txt', "r") as f:
                        for line in f:
                            wproxies.append(line)
                proksi = extract_proxy(wproxies[0])
                print(proksi)

                continue
            break
        # wproxies.rotate(1)
        # proksi = extract_proxy(wproxies[0])
        db_cur.execute(sql, [artinya, artiid, idnya])
        db_connection.commit()
        print(idnya)

db_connection.close()