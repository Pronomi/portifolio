// Atualiza o relógio dinâmico
function updateClock() {
    const clock = document.getElementById("clock");
    const now = new Date();
    const time = now.toLocaleTimeString('pt-BR');
    const date = now.toLocaleDateString('pt-BR');
    clock.textContent = `[${time} - ${date}]`;
  }
  setInterval(updateClock, 1000);
  updateClock();
  
  // Alternância de tema
  document.getElementById("toggle-theme").addEventListener("click", () => {
    document.body.classList.toggle("theme-fallout");
  });