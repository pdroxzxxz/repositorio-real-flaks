from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")




from flask import Flask, render_template

app = Flask(__name__)


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")





from flask import Flask, render_template

app = Flask(__name__)


@app.route("/ola/<nome>")
def ola(nome):
    return render_template("ola.html", nome=nome)























#deve ficar no final do arquivo
if __name__ == "__main__":
    # host=0.0.0.0 permite o encaminhamento da porta no Codespaces.
    app.run(host="0.0.0.0", port=5000, debug=True)

