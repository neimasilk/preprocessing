# import StemmerFactory class
import sys
sys.path.insert(0, './pysastrawi/src')

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# stemming process
sentence = 'Perekonomian Indonesia sedang dalam pertumbuhan yang membanggakan'
output   = stemmer.stem(sentence)

print(output)
# ekonomi indonesia sedang dalam tumbuh yang bangga

print(stemmer.stem('Mereka meniru-nirukannya'))
# mereka tiru

def stem_amien(text):
# per@ an@ ekonomi indonesia sedang dalam per@ an@ tumbuh yang mem@ kan@ bangga.

# mereka plu@ me@ kan@ nya@ tiru

# buat daftar dictionary untuk menggabungkan. pelajari sastrawi selama seminggu
    pass
