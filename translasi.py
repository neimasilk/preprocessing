import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/mukhlis/seq2seq-e71dee1db5ca.json"

from google.cloud import translate
import goslate

translate_client = translate.Client()

def translasi_googkey(text,source,target):
    translation = translate_client.translate(
        text,
        target_language=target, source_language=source)
    return translation['translatedText']

def translasi_proxy(text,source,target,proxy='',service='https://translate.google.com'):
    gs = goslate.Goslate(service_urls=[service])
    # gs = goslate.Goslate()
    if proxy=='':
        hasil = gs.translate(text,target,source)
    return hasil

if __name__ == '__main__':
    # print(translasi_googkey('percobaan','id','en'))
    try:
        print(translasi_proxy('percobaan goslate','id','en','','http://translate.google.com'))
    except:
        print('terjadi kesalahan')