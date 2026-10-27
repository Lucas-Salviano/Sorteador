"""Back-end Flask do sorteador: serve a página e expõe a API /api/sortear."""

from flask import Flask, jsonify, render_template, request

from sorteador import sortear

LIMITE_QUANTIDADE = 10_000

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/api/sortear")
def api_sortear():
    dados = request.get_json(silent=True) or {}
    try:
        x = int(dados["x"])
        y = int(dados["y"])
        quantidade = int(dados.get("quantidade", 1))
    except (KeyError, TypeError, ValueError):
        return jsonify(erro="Informe x, y e quantidade como números inteiros."), 400

    if not 1 <= quantidade <= LIMITE_QUANTIDADE:
        return jsonify(erro=f"A quantidade deve estar entre 1 e {LIMITE_QUANTIDADE}."), 400

    try:
        numeros = sortear(x, y, quantidade, bool(dados.get("repetir", False)))
    except ValueError as erro:
        return jsonify(erro=str(erro)), 400

    return jsonify(numeros=numeros)


if __name__ == "__main__":
    app.run(debug=True)
