from models import Autor, Livro


def popular_banco(session):
    """Cadastre autores e livros iniciais para testar a aplicação."""
    # TODO: crie pelo menos 3 autores.
    autor1 = Autor(nome = "Clarisse Lispector", pais = "Brasil")
    autor2 = Autor(nome = "Machado de Assis", pais = "Brasil")
    autor3 = Autor(nome = "Nicolau Maquiavel", pais = "Itália")
    session.add_all([autor1, autor2, autor3])
    session.flush()

    # TODO: crie pelo menos 6 livros.
    livro1 = Autor(titulo = "Hora da Estrela", disponivel = True, autor_id = autor1.id)
    livro2 = Autor(titulo = "Água-viva", disponivel = True, autor_id = autor1.id)
    livro3 = Autor(titulo = "Maquiavel", disponivel = True, autor2 = "Itália")
    # TODO: inclua livros disponíveis e indisponíveis.
    session.add_all([livro1, livro2, livro3])
    session.flush()

    # TODO: use session.add ou session.add_all e finalize com session.commit().
    session.commit()