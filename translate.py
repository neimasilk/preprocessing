
import googletrans

translator = googletrans.Translator()
text = 'ini adalah percobaan translasi'
# print(translator.translate(text,'en','id').text)
outputfile = './indonesia_sentences_10.txt'
file_hasil_translasi = './english_sentences_10.txt'

sentences = []
with open(outputfile, 'r') as f:
    for item in f:
        print(item)
        sentences.append(translator.translate(item,'en','id').text)
    f.close()
with open(file_hasil_translasi, 'w') as f:
    for item in sentences:
        f.write("%s\n" % item)
    f.close()