# Cria o objeto biblioteca
class Biblioteca:
    def __init__(self):
        self._livros = []

    # Função para inserir os livros guardados na biblioteca
    def inserir_livros(self, *livros):
        for livro in livros:
            self._livros.append(livro)

    # Função para mostrar os livros guardados na biblioteca
    def listar_livros(self):
        for livro in self._livros:
            print(f'{livro.titulo}, {livro.autor}, {livro.ano}, {livro.genero}')

# Cria os livros
class Livro:
    def __init__(self, titulo, autor, ano_lancamento, genero):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano_lancamento
        self.genero = genero

biblioteca = Biblioteca()

livro1 = Livro('O Hobbit', 'J.R.R Tolkien', '1937', 'Fantasia')
livro2 = Livro('Senhor das Moscas', 'Willian Golding', '1954', 'Romance')
livro3 = Livro('O Pequeno Princípe', 'Antoine de Saint-Exupéry', '1943', 'Literatura Infanto-Juvenil')
livro4 = Livro('O Senhor dos Anéis: A Sociedade do Anel', 'J.R.R Tolkien', '1954', 'Fantasia')
livro5 = Livro('O Homem de Giz', 'C.J Tudor', '2018', 'Suspense')
livro6 = Livro('Caco', 'Gilberto Mattje', '1900', 'Romance')
livro7 = Livro('Eu Sou a Lenda', 'Richard Matheson', '1954', 'Horror')
livro8 = Livro('Magnus Chase e os Deuses de Asgard', 'Rick Riordan', '2015', 'Romance')
livro9 = Livro('Como Eu Era Antes de Você', 'Jojo Moyes', '2012', 'Romance')

# Inseri os livros dentro da biblioteca
biblioteca.inserir_livros(livro1, livro2, livro3, livro4, livro5, livro6, livro7, livro8, livro9)

# Lista os livros dentro de self._livros
biblioteca.listar_livros()