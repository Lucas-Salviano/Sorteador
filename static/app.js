const form = document.getElementById("form");
const resultado = document.getElementById("resultado");
const erro = document.getElementById("erro");

function mostrarVazio() {
  resultado.innerHTML = '<span class="vazio">Os números sorteados aparecem aqui</span>';
}

function mostrarNumeros(numeros) {
  resultado.replaceChildren(
    ...numeros.map((numero, i) => {
      const bola = document.createElement("span");
      bola.className = "bola";
      bola.textContent = numero;
      bola.style.animationDelay = `${Math.min(i, 30) * 60}ms`;
      return bola;
    })
  );
}

form.addEventListener("submit", async (evento) => {
  evento.preventDefault();
  erro.textContent = "";

  const corpo = {
    x: form.x.value,
    y: form.y.value,
    quantidade: form.quantidade.value,
    repetir: form.repetir.checked,
  };

  try {
    const resposta = await fetch("/api/sortear", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(corpo),
    });
    const dados = await resposta.json();
    if (!resposta.ok) {
      mostrarVazio();
      erro.textContent = dados.erro;
      return;
    }
    mostrarNumeros(dados.numeros);
  } catch {
    erro.textContent = "Não foi possível falar com o servidor.";
  }
});
