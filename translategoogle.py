from googletrans import Translator
translator = Translator()
translator.translate('안녕하세요.', dest='ja')


# Basic Usage
# If source language is not given, google translate attempts to detect the source language.
#
# >>> from googletrans import Translator
# >>> translator = Translator()
# >>> translator.translate('안녕하세요.')
# # <Translated src=ko dest=en text=Good evening. pronunciation=Good evening.>
# >>> translator.translate('안녕하세요.', dest='ja')
# # <Translated src=ko dest=ja text=こんにちは。 pronunciation=Kon'nichiwa.>
# >>> translator.translate('veritas lux mea', src='la')
# # <Translated src=la dest=en text=The truth is my light pronunciation=The truth is my light>
# Customize service URL
# You can use another google translate domain for translation. If multiple URLs are provided it then randomly chooses a domain.
#
# >>> from googletrans import Translator
# >>> translator = Translator(service_urls=[
#       'translate.google.com',
#       'translate.google.co.kr',
#     ])
# Advanced Usage (Bulk)
# Array can be used to translate a batch of strings in a single method call and a single HTTP session. The exact same method shown above work for arrays as well.
#
# >>> translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='ko')
# >>> for translation in translations:
# ...    print(translation.origin, ' -> ', translation.text)
# # The quick brown fox  ->  빠른 갈색 여우
# # jumps over  ->  이상 점프
# # the lazy dog  ->  게으른 개
# Language detection
# The detect method, as its name implies, identifies the language used in a given sentence.
#
# >>> from googletrans import Translator
# >>> translator = Translator()
# >>> translator.detect('이 문장은 한글로 쓰여졌습니다.')
# # <Detected lang=ko confidence=0.27041003>
# >>> translator.detect('この文章は日本語で書かれました。')
# # <Detected lang=ja confidence=0.64889508>
# >>> translator.detect('This sentence is written in English.')
# # <Detected lang=en confidence=0.22348526>
# >>> translator.detect('Tiu frazo estas skribita en Esperanto.')
# # <Detected lang=eo confidence=0.10538048>
# GoogleTrans as a command line application
# $ translate -h
# usage: translate [-h] [-d DEST] [-s SRC] [-c] text
#
# Python Google Translator as a command-line tool
#
# positional arguments:
#   text                  The text you want to translate.
#
# optional arguments:
#   -h, --help            show this help message and exit
#   -d DEST, --dest DEST  The destination language you want to translate.
#                         (Default: en)
#   -s SRC, --src SRC     The source language you want to translate. (Default:
#                         auto)
#   -c, --detect
#
# $ translate "veritas lux mea" -s la -d en
# [veritas] veritas lux mea
#     ->
# [en] The truth is my light
# [pron.] The truth is my light
#
# $ translate -c "안녕하세요."
# [ko, 1] 안녕하세요.