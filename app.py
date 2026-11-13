from flask import Flask, render_template, request, redirect, url_for
import models

app = Flask(__name__)

models.init_db()

@app.route("/")
def index():
    transacoes = models.get_all_transacoes()
    categorias = models.get_categorias()

    saldo = 0
    for t in transacoes:
        if t['tipo'] == "receita":
            saldo += t['valor']
        else: 
            saldo -= t['valor']

    return render_template("index.html", transacoes=transacoes, categorias=categorias, saldo=saldo)

@app.route("/add", methods=["POST"])
def add():
    descricao = request.form.get("descricao")
    valor = float(request.form.get("valor"))
    data = request.form.get("data")
    categoria_id = int(request.form.get("categoria_id"))

    models.add_transacoes(descricao, valor, data, categoria_id)

    return redirect(url_for("index"))

@app.route('/clear', methods=['POST'])
def clear():
    models.limpar_transacoes()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)



