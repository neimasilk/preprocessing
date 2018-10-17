import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/mukhlis/seq2seq-e71dee1db5ca.json"
import urllib.request as urllib2
import goslate

proxy_handler = urllib2.ProxyHandler({"http" : "http://173.161.17.93:44251"})
proxy_opener = urllib2.build_opener(urllib2.HTTPHandler(proxy_handler),
                                    urllib2.HTTPSHandler(proxy_handler))

gs_with_proxy = goslate.Goslate(opener=proxy_opener)
translation = gs_with_proxy.translate("hello world", "de")
