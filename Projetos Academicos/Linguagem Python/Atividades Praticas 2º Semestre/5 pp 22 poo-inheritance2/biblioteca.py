

class Publicacao:
    def __init__(self, titulo, ano):
        self.titulo = titulo
        self.ano = ano

    
    def get_titulo(self):
        return self.titulo

    def get_ano(self):
        return self.ano

    
    def set_titulo(self, novo_titulo):
        if len(novo_titulo.strip()) == 0:
            print("Erro: o título não pode ser vazio!")
        else:
            self.titulo = novo_titulo

    def set_ano(self, novo_ano):
        if novo_ano < 0:
            print("Erro: o ano não pode ser negativo!")
        else:
            self.ano = novo_ano

    
    def descricao(self):
        return f"Título: {self.titulo} | Ano: {self.ano}"



class Livro(Publicacao):
    def __init__(self, titulo, ano, autor, paginas, genero="Geral"):
        super().__init__(titulo, ano)
        self.autor = autor
        self.paginas = paginas
        self.genero = genero

    
    def get_autor(self):
        return self.autor

    def get_paginas(self):
        return self.paginas

    def get_genero(self):
        return self.genero

    
    def set_autor(self, novo_autor):
        if len(novo_autor.strip()) == 0:
            print("Erro: o autor não pode ser vazio!")
        else:
            self.autor = novo_autor

    def set_paginas(self, novas_paginas):
        if novas_paginas <= 0:
            print("Erro: número de páginas deve ser maior que zero!")
        else:
            self.paginas = novas_paginas

    def set_genero(self, novo_genero):
        self.genero = novo_genero



class Revista(Publicacao):
    def __init__(self, titulo, ano, editora, edicao, categoria="Atualidades"):
        super().__init__(titulo, ano)
        self.editora = editora
        self.edicao = edicao
        self.categoria = categoria

 
    def get_editora(self):
        return self.editora

    def get_edicao(self):
        return self.edicao

    def get_categoria(self):
        return self.categoria

  
    def set_editora(self, nova_editora):
        if len(nova_editora.strip()) == 0:
            print("Erro: a editora não pode ser vazia!")
        else:
            self.editora = nova_editora

    def set_edicao(self, nova_edicao):
        if nova_edicao <= 0:
            print("Erro: a edição deve ser maior que zero!")
        else:
            self.edicao = nova_edicao

    def set_categoria(self, nova_categoria):
        self.categoria = nova_categoria
