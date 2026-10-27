const form = document.getElementById("form");
const resultado = document.getElementById("resultado");
const erro = document.getElementById("erro");

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
      resultado.textContent = "—";
      erro.textContent = dados.erro;
      return;
    }
    resultado.textContent = dados.numeros.join(", ");
  } catch {
    erro.textContent = "Não foi possível falar com o servidor.";
  }
});
