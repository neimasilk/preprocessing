import urllib.request as urllib2
import googletrans


def findproxy():
    with open('proxies.txt', "r") as f:
        array = []
        for line in f:
            array.append(line)
        proxies = []
    for alamat in array:
        proxies.append('http://'+alamat.split()[-1].replace('>',''))

    del array
    for proxy in proxies:

        try:
            translator = googletrans.Translator(service_urls=[
                'translate.google.cn',
                'translate.google.co.kr',
                'translate.google.com'
            ], proxies=prox_dict)
            item = "ini adalah percobaan"
            translation = translator.translate(item, 'en', 'id').text

        except:
            print(proxy)
            prox_dict = {"http" : proxy}
            continue
        else:
            print(translation)
            return prox_dict
            break
    return False


def translate_proxy(text,source,target,proxy):
    translator = googletrans.Translator(service_urls=[
        'translate.google.cn',
        'translate.google.co.kr',
        'translate.google.com'
    ], proxies=proxy)
    item = text
    translation = translator.translate(item, target, source).text
    return translation

kata = "ini yang akan diterjemahkan dengan proxy"

proksi = findproxy()
belum = True

while belum:
    try:
        print(translate_proxy(kata,'id','en',proksi))
    except:
        proksi = findproxy()
    else:
        belum = False


# for proxy in proxies:
    # try:

    #     proxy_handler = urllib2.ProxyHandler({"http" : proxy})
    #     proxy_opener = urllib2.build_opener(urllib2.HTTPHandler(proxy_handler),
    #                                     urllib2.HTTPSHandler(proxy_handler))
    #     urllib2.install_opener(proxy_opener)
    #     gs_with_proxy = goslate.Goslate(opener=proxy_opener)
    #     translation = gs_with_proxy.translate("hello world", "de")
    # except:
    #     print(proxy)
    #     continue
    # else:
    #     print(translation)
    #     break
