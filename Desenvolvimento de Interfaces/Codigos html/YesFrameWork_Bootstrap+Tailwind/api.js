const produtos = [
    { id: 1, nome: "Rolex Submariner", preco: 89000, estoque: 2 },
    { id: 2, nome: "Patek Philippe Nautilus", preco: 150000, estoque: 1 },
    { id: 3, nome: "Audemars Piguet Royal Oak", preco: 120000, estoque: 3 },
    { id: 4, nome: "Richard Mille RM 11-03", preco: 2500000, estoque: 1 },
    { id: 5, nome: "Jacob & Co Astronomia", preco: 3100000, estoque: 1 }
  ];
  
  function carregarProdutos() {
    const container = document.getElementById("catalogoContainer");
    produtos.forEach(p => {
      const col = document.createElement("div");
      col.classList.add("col-md-3", "p-3", "bg-gray-900", "rounded", "shadow", "hover:scale-105", "transition-transform");
      col.innerHTML = `
        <h3 class="text-yellow-500 fw-semibold">${p.nome}</h3>
        <p>Preço: R$ ${p.preco.toLocaleString('pt-BR')}</p>
        <p>Estoque: ${p.estoque}</p>
      `;
      container.appendChild(col);
    });
  }
  
  document.addEventListener("DOMContentLoaded", carregarProdutos);
  