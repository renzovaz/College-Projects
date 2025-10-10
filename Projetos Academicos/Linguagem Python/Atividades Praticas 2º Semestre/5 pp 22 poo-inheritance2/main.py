
from biblioteca import Publicacao, Livro, Revista


print("=== TESTE SUPERCASSE PUBLICAÇÃO ===")
pub1 = Publicacao("Aprendendo Python", 2022)
pub2 = Publicacao("Programação Moderna", 2020)

print(pub1.descricao())
print(pub2.descricao())

pub1.set_titulo("Python Avançado")
pub1.set_ano(2023)
print(pub1.descricao())


pub2.set_ano(-10)  
pub2.set_titulo("")  



print("\n=== TESTE SUBCLASSE LIVRO ===")
livro1 = Livro("POO em Python", 2024, "Renzo Vaz", 350)
livro2 = Livro("Lógica de Programação", 2023, "Carlos Silva", 200, "Educação")

print(livro1.descricao())
print(f"Autor: {livro1.get_autor()} | Páginas: {livro1.get_paginas()} | Gênero: {livro1.get_genero()}")

livro1.set_paginas(400)
livro1.set_genero("Tecnologia")
print(f"Atualizado: {livro1.get_paginas()} páginas, gênero {livro1.get_genero()}")


livro2.set_paginas(0)  



print("\n=== TESTE SUBCLASSE REVISTA ===")
revista1 = Revista("Ciência Hoje", 2025, "Editora Alfa", 42)
revista2 = Revista("Tecnologia Atual", 2024, "Editora Beta", 30, "Inovação")

print(revista1.descricao())
print(f"Editora: {revista1.get_editora()} | Edição: {revista1.get_edicao()} | Categoria: {revista1.get_categoria()}")

revista1.set_edicao(43)
revista1.set_categoria("Ciência")
print(f"Atualizada: Edição {revista1.get_edicao()}, Categoria: {revista1.get_categoria()}")


revista2.set_editora("")  
