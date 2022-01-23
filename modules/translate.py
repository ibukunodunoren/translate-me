# Translates a message and returns the translation
#pip install translate in terminal
#pip install langdetect in terminal

from translate import Translator
from langdetect import detect #returns en, zh, fr for english, mandarin, french (accommodates 50 languages)
  
#for speaker 1 
def translateFirst(text_01, text_02):
    translator = Translator(to_lang="{}".format(detect(text_02))) #trying to input variable within list
    translation = translator.translate(text_01) 
    return(translation)

#for speaker 2 
def translateSecond(text_01, text_02):
    translator = Translator(to_lang="{}".format(detect(text_01))
    translation = translator.translate(text_02) 
    return(translation)
