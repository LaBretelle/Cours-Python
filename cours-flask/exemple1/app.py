from flask import Flask

app = Flask("Application")

@app.route("/")
def index():
    return "Hello world !"

@app.route("/banane")
def affichage():
	return "j'aime pas les bananes"
app.run()
