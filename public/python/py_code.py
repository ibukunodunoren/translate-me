from translate import Translator
from langdetect import detect #returns en, zh, fr for english, mandarin, french (accommodates 50 languages)
import sys
  
def translate(text):
    print(text)
    #translator = Translator(to_lang="fr")
    #translation = translator.translate(text)
    #return(translation)


if sys.argv[1] == 'tr':
    translate(sys.argv[2])

sys.stdout.flush()
