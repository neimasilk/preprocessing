import sys
import re
import sqlite3

if (sys.version_info[0] < 3):
    import urllib2
    import urllib
    import HTMLParser
else:
    import html.parser
    import urllib.request
    import urllib.parse

agent = {'User-Agent':
"Mozilla/4.0 (\
compatible;\
MSIE 6.0;\
Windows NT 5.1;\
SV1;\
.NET CLR 1.1.4322;\
.NET CLR 2.0.50727;\
.NET CLR 3.0.04506.30\
)"}


def unescape(text):
    if (sys.version_info[0] < 3):
        parser = HTMLParser.HTMLParser()
    else:
        parser = html.parser.HTMLParser()
    return (parser.unescape(text))


def translate_proxy(to_translate, from_language="auto", to_language="auto", proxes={}):
    """Returns the translation using google translate
    you must shortcut the language you define
    (French = fr, English = en, Spanish = es, etc...)
    if not defined it will detect it or use english by default
    Example:
    print(translate("salut tu vas bien?", "en"))
    hello you alright?
    """
    if proxes!={}:
        proxy = urllib.request.ProxyHandler(proxes)
        opener = urllib.request.build_opener(proxy)
        urllib.request.install_opener(opener)
    base_link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s"
    if (sys.version_info[0] < 3):
        to_translate = urllib.quote_plus(to_translate)
        link = base_link % (to_language, from_language, to_translate)
        request = urllib2.Request(link, headers=agent)
        raw_data = urllib2.urlopen(request).read()
    else:
        to_translate = urllib.parse.quote(to_translate)
        link = base_link % (to_language, from_language, to_translate)
        request = urllib.request.Request(link, headers=agent)
        raw_data = urllib.request.urlopen(request).read()
    data = raw_data.decode("utf-8")
    expr = r'class="t0">(.*?)<'
    re_result = re.findall(expr, data)
    if (len(re_result) == 0):
        result = ""
    else:
        result = unescape(re_result[0])
    return (result)

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
            translate_proxy("percobaan",'id','en',prox_dict)

        except:
            print(proxy)
            continue

        # print(translation)
        return prox_dict

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
        if (id[2] == None) or (id[3] == None):
            idnya = id[0]
            teks = id[1]
            while True:
                try:
                    if (id[2] == None):
                        artinya = translate_proxy(teks, 'id', 'en', proksi)
                    else:
                        artinya = id[2]

                    if (id[3] == None):
                        articn = translate_proxy(artinya, 'en', 'zh-CN', proksi)
                    else:
                        articn = id[3]
                except:
                    proksi = findproxy()
                    continue
                break
                db_cur.execute(sql, [artinya, articn, idnya])
            db_connection.commit()
            print(idnya)

    db_connection.close()

if __name__ == '__main__':
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
        if (id[2] == None) or (id[3] == None):
            idnya = id[0]
            teks = id[1]
            while True:
                try:
                    if (id[2] == None):
                        artinya = translate_proxy(teks, 'en', 'id', proksi)
                    else:
                        artinya = id[2]

                    if (id[3] == None):
                        articn = translate_proxy(artinya, 'en', 'zh-CN', proksi)
                    else:
                        articn = id[3]
                except:
                    proksi = findproxy()
                    continue
                break
            db_cur.execute(sql, [artinya, articn, idnya])
            db_connection.commit()
            print(idnya)

    db_connection.close()