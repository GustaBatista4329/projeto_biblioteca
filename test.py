class Biblioteca:
    def __init__(self):
        self._livros = []

    def inserir_livros(self, titulo, autor, ano_lancamento, genero):
            self._livros.append(Livro(titulo, autor, ano_lancamento, genero))

    def listar_livros(self):
        for livro in self._livros:
            print(f'{livro.titulo}, {livro.autor}, {livro.ano}, {livro.genero}')

class Livro:
    def __init__(self, titulo, autor, ano_lancamento, genero):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano_lancamento
        self.genero = genero

livro1 = Biblioteca()
livro2 = Biblioteca()
livro3 = Biblioteca()

livro1.inserir_livros('O Hobbit', 'J.R.R Tolkien', '1937', 'Fantasia')
livro2.inserir_livros('Senhor Das Moscas', 'Willian Golding', '1954', 'Romance')
livro3.inserir_livros('O Pequeno Princípe', 'Antoine de Saint-Exupéry', '1943', 'Literatura Infanto-Juvenil')

livro1.listar_livros()
livro3.listar_livros()
livro2.listar_livros()

print(livro1._livros)