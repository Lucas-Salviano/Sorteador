# Sorteador de números

Sorteia números inteiros em um intervalo de **x** a **y** (inclusive), em Python.

## Uso

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
