from flask import Flask, render_template

#import modules.deepgram
from modules.analyse import *
#import modules.translate

# <<<<<<< HEAD
# =======

# EXAMPLE: running this should output '-0.8' and '-0.15'
#text = "I really hate this product"
#sentence = ["I really hate this product", "but it's also quite interesting to play with"]
#print(analyse(text))
#print(analyse2(sentence))
# >>>>>>> 76be03e2bf8b9ebb2cde64f7b5e09881ebac0465


app = Flask(__name__)

@app.route("/")
def translate():
	return render_template("translate.html")
	
@app.route("/about")
def about():
	return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
