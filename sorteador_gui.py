"""Interface gráfica (tkinter) do sorteador de números de x a y."""

import tkinter as tk
from tkinter import messagebox, ttk

from sorteador import sortear


class App(ttk.Frame):
    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master, padding=16)
        self.pack(fill="both", expand=True)

        self.x = tk.StringVar(value="1")
        self.y = tk.StringVar(value="60")
        self.qtd = tk.StringVar(value="1")
        self.repetir = tk.BooleanVar(value=False)
        self.resultado = tk.StringVar(value="—")

        for linha, (texto, var) in enumerate(
            [("De (x):", self.x), ("Até (y):", self.y), ("Quantidade:", self.qtd)]
        ):
            ttk.Label(self, text=texto).grid(row=linha, column=0, sticky="w", pady=4)
            ttk.Entry(self, textvariable=var, width=12).grid(row=linha, column=1, pady=4)

        ttk.Checkbutton(self, text="Permitir repetições", variable=self.repetir).grid(
            row=3, column=0, columnspan=2, sticky="w", pady=4
        )
        ttk.Button(self, text="Sortear", command=self.sortear).grid(
            row=4, column=0, columnspan=2, sticky="ew", pady=8
        )
        ttk.Label(
            self, textvariable=self.resultado, font=("Segoe UI", 20, "bold"),
            wraplength=300, justify="center",
        ).grid(row=5, column=0, columnspan=2, pady=8)

        master.bind("<Return>", lambda _e: self.sortear())

    def sortear(self) -> None:
        try:
            x, y, qtd = int(self.x.get()), int(self.y.get()), int(self.qtd.get())
        except ValueError:
            messagebox.showerror("Erro", "Digite apenas números inteiros.")
            return
        if qtd < 1:
            messagebox.showerror("Erro", "A quantidade deve ser pelo menos 1.")
            return
        try:
            numeros = sortear(x, y, qtd, self.repetir.get())
        except ValueError as erro:
            messagebox.showerror("Erro", str(erro))
            return
        self.resultado.set(", ".join(map(str, numeros)))


def main() -> None:
    root = tk.Tk()
    root.title("Sorteador de números")
    root.resizable(False, False)
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
