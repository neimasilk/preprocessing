import urllib.request as urllib2
import goslate


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
        proxy_handler = urllib2.ProxyHandler({"http" : proxy})
        proxy_opener = urllib2.build_opener(urllib2.HTTPHandler(proxy_handler),
                                        urllib2.HTTPSHandler(proxy_handler))
        gs_with_proxy = goslate.Goslate(opener=proxy_opener)
        translation = gs_with_proxy.translate("hello world", "de")
    except:
        print(proxy)
        continue
    else:
        print(translation)
        break
