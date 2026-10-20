"""Sorteador de números inteiros em um intervalo de x a y (inclusive)."""

import random
import sys


def sortear(x: int, y: int, quantidade: int = 1, repetir: bool = True) -> list[int]:
    """Sorteia `quantidade` números inteiros entre x e y (inclusive).

    Se `repetir` for False, os números sorteados não se repetem.
    """
    if x > y:
        x, y = y, x
    if not repetir and quantidade > (y - x + 1):
        raise ValueError("Quantidade maior que o total de números disponíveis no intervalo.")
    if repetir:
        return [random.randint(x, y) for _ in range(quantidade)]
    return random.sample(range(x, y + 1), quantidade)


def ler_inteiro(mensagem: str) -> int:
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


def main() -> None:
    if len(sys.argv) >= 3:
        x, y = int(sys.argv[1]), int(sys.argv[2])
        quantidade = int(sys.argv[3]) if len(sys.argv) >= 4 else 1
    else:
        x = ler_inteiro("Número inicial (x): ")
        y = ler_inteiro("Número final (y): ")
        quantidade = ler_inteiro("Quantos números sortear? ")

    repetir = True
    if quantidade > 1 and len(sys.argv) < 3:
        repetir = input("Permitir repetições? (s/n): ").strip().lower() != "n"

    try:
        resultado = sortear(x, y, quantidade, repetir)
    except ValueError as erro:
        print(f"Erro: {erro}")
        sys.exit(1)

    print("Sorteado(s):", ", ".join(map(str, resultado)))


if __name__ == "__main__":
    main()
