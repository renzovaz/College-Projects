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
      const div = document.createElement("div");
      div.classList.add("produto");
      div.innerHTML = `
        <h3>${p.nome}</h3>
        <p>Preço: R$ ${p.preco.toLocaleString('pt-BR')}</p>
        <p>Estoque: ${p.estoque}</p>
      `;
      container.appendChild(div);
    });
  }
  
  document.addEventListener("DOMContentLoaded", carregarProdutos);
  