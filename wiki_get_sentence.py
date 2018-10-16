import sqlite3
import random
from nltk import sent_tokenize
from nltk import word_tokenize


class WikiGetSentence(object):
    def __init__(self, f_data="/home/mukhlis/machine_learning_nlp"):
        self.filepath = f_data
        try:
            self._db_connection = sqlite3.connect(self.filepath)
            self._db_cur = self._db_connection.cursor()
        except Error as e:
            print(e)

    def query(self, query, params=""):
        return self._db_cur.execute(query, params)

    def generate_list(self, tabel, ukuran, max_count):
        ukur = 0
        daftar_id = []
        toks = []
        l = list(range(max_count))
        random.shuffle(l)
        print("randomize...")
        a = ""
        indeks = 0
        while ((indeks < max_count) and (ukur <= ukuran)):
            self._db_cur.execute(
                "select id,dokumen, ukuran from {df_tabel} where id = {df_acak}+1".format(df_tabel=tabel,
                                                                                          df_acak=l[indeks]))
            (id_nya, dokumen, ukuran_data) = self._db_cur.fetchone()
            # select limit 1 offset acak
            # ambil id dan ukuran_data
            daftar_id.append(id_nya)
            toks.append(dokumen.replace('\n', ' '))
            ukur = ukur + ukuran_data
            indeks = indeks + 1
            if indeks % 2000 == 0:
                print("Suffeling {0:.2f}%".format((ukur / ukuran) * 100))
        return toks, daftar_id

    def generate_list_sentences(self, tabel, ukuran, max_word):
        ukur = 0
        daftar_id = []
        toks = []
        token =[]
        max_count = 408734
        l = list(range(max_count))
        random.shuffle(l)
        a = ""
        indeks = 0
        while ((indeks < max_count) and (ukur <= ukuran)):
            self._db_cur.execute(
                "select id,dokumen from {df_tabel} where id = {df_acak}+1".format(df_tabel=tabel, df_acak=l[indeks]))
            (id_nya, document) = self._db_cur.fetchone()

            # sentence tokenize

            sentence = "My friend holds a Msc. in Computer Science."
            token = sent_tokenize(document.replace('\n', ' '))
            temp_kalimat =[]
            for kalimat in token:
                word = word_tokenize(kalimat)
                if len(word) <= max_word:
                    temp_kalimat.append(kalimat)

            token = temp_kalimat
            ukuran_data = len(token)

            # ['My friend holds a Msc.', 'in Computer Science.']
            ukur_sebelum = ukur
            ukur = ukur + ukuran_data
            toks = toks + token


            indeks = indeks + 1
            if indeks % 2000 == 0:
                print("Suffeling {0:.2f}%".format((ukur / ukuran) * 100))
        toks = toks[:ukuran]
        return toks

    def generate_sentence(self, lang, max_len, size, outputfile=''):
        if lang == 'id':
            generate_id(max_len, size)

        if outputfile == '':
            savedb(lang, sentences)
        else:
            savefile(lang, sentences, outputfile)

    def generate_id(self, max_sentence_len, sentences_count):
        # generate indonesia sentences with max lengh of sentences max_len and count of sentences size
        # examples : sentences = generate_id(80, 5)
        # it should generates sentences with max sentences lenght of 80 with 5 sentences
        #  sentences = ['kalimat 1', 'kalimat 2', 'kalimat 3', 'kalimat 4', 'kalimat 5']
        return self.generate_list_sentences('wiki_id',sentences_count,max_sentence_length)


    def savedb(self, lang, sentences):
        # saving sentences list generated by generate sentences to database
        pass

    def savefile(self, sentences, outputfile):
        # saving sentences generated by generate sentences function to text file
        with open(outputfile, 'w') as f:
            for item in sentences:
                f.write("%s\n" % item)


if __name__ == '__main__':
    count_id = 408734
    sumber = 'wiki_id'
    ukuran = 10
    max_sentence_length = 80
    sentences_count = 2000000
    wikiget = WikiGetSentence()
    # b = wikiget.generate_id(max_sentence_length,sentences_count)
    b = wikiget.generate_id(max_sentence_length,sentences_count)
    wikiget.savefile(b,'indonesia_sentences_2milion.txt')

