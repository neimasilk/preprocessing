import goslate
# import sqlite3
import urllib

def extract_proxy(alamat):
    return 'http://' + alamat.split()[-1].replace('>', '')

def find_translate_proxy(proxy_file='proxies.txt'):
    with open(proxy_file, "r") as f:  # file proxynya: proxies.txt
        array = []
        working_proxy = []
        for line in f:
            array.append(line)

    for alamat in array:
        proks = extract_proxy(alamat)
        prox_dict = {"http": proks}
        proxy = urllib.request.ProxyHandler(prox_dict)
        opener = urllib.request.build_opener(proxy)
        urllib.request.install_opener(opener)
        try:
            translator = goslate.Goslate(opener=opener)
            item = "ini adalah percobaan"
            translation = translator.translate(item, "en", 'id')
            working_proxy.append(alamat)

        except:
            print(alamat)
            continue

        print(translation)
        return working_proxy

list_working_proxy = find_translate_proxy()
with open('working_proxy.txt', 'w') as f:
    for item in list_working_proxy:
        f.write("%s\n" % item)