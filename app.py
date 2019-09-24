import random, ast
from flask import Flask, render_template as rend
app = Flask(__name__)
with open("frettir.txt") as frett_file:
	frettir = ast.literal_eval(frett_file.read())
with open("tolur.txt") as frett_file:
	tolur = ast.literal_eval(frett_file.read())
@app.route("/")
def index():
	return "<a href='/frettir'>fréttir</a><a href='/kennitala'>kennitölur</a>"

@app.route('/frettir')
def fretti():
	return rend("frettir.html", title="index", frettir=frettir.keys())


@app.route("/frettir/<frett>")
def frett(frett):
	if frett in frettir.keys():
		return rend("frett.html", title=frettir[frett][0], content=frettir[frett][1], pic=frettir[frett][2])
	else:
		return page_not_found(None)

@app.route("/kennitala/")
def kennitolur():
	return rend("tolur.html", title="index", frettir=[tolur[i] for i in tolur.keys()])
@app.route("/kennitala/<tala>")
def kennitala(tala):
	return rend("tala.html", kennitala=tala, summa=sum(list(map(int, list(tala)))))
@app.errorhandler(404)
def page_not_found(e):
    return rend('404.html')


if __name__ == "__main__":
	app.run(debug=True)