from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/projetos")
def projetos():
    return render_template("projetos.html")

@app.route("/1")
def projeto1():
    return render_template("1.html")

@app.route("/2")
def projeto2():
    return render_template("2.html")

# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)

    # servidor do heroku

