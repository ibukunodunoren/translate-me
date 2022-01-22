#import modules.deepgram
from modules.analyse import *
#import modules.translate


# EXAMPLE: running this should output '-0.8' and '-0.15'
text = "I really hate this product"
sentence = ["I really hate this product", "but it's also quite interesting to play with"]
print(analyse(text))
print(analyse2(sentence))
