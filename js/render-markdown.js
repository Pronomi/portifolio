async function renderMarkdown(mdPath, containerId) {
    try {
      const response = await fetch(mdPath);
      const mdText = await response.text();
  
      // Conversor básico de Markdown para HTML (simples)
      const html = mdText
        .replace(/^### (.*$)/gim, '<h3>$1</h3>')
        .replace(/^## (.*$)/gim, '<h2>$1</h2>')
        .replace(/^# (.*$)/gim, '<h1>$1</h1>')
        .replace(/\*\*(.*?)\*\*/gim, '<strong>$1</strong>')
        .replace(/\*(.*?)\*/gim, '<em>$1</em>')
        .replace(/\n$/gim, '<br />');
  
      document.getElementById(containerId).innerHTML = html;
    } catch (err) {
      document.getElementById(containerId).innerHTML = `<p style="color: red;">Erro ao carregar o arquivo Markdown.</p>`;
      console.error("Erro ao renderizar markdown:", err);
    }
  }