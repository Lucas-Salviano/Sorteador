# Sorteador de números

Sorteia números inteiros em um intervalo de **x** a **y** (inclusive), em Python.

## Versão web (Flask)

Back-end em `app.py` (API `POST /api/sortear`) e front-end em `templates/` e `static/`.

```bash
pip install -r requirements.txt
python app.py
```

Deploy no Render: Build Command `pip install -r requirements.txt`, Start Command `gunicorn app:app`.

## Docker

```bash
docker build -t sorteador:1.0 .
docker run -p 8000:8000 sorteador:1.0
```

Acesse http://localhost:8000. A porta pode ser trocada com a variável `PORT`.

## Uso local

Interface gráfica:

```bash
python sorteador_gui.py
```

Modo interativo:

```bash
python sorteador.py
```

Por argumentos (`x y [quantidade]`):

```bash
python sorteador.py 1 60 6
```

Como biblioteca:

```python
from sorteador import sortear

sortear(1, 60, quantidade=6, repetir=False)  # ex.: [14, 3, 57, 22, 41, 8]
```

Requer Python 3.9+.
