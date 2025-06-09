from core.infrastructure.repositories import ConferenciaRepository, DetalhadoProdutoRepository, EstoqueFisicoRepository, EstoquePorLocalRepository, MetaPorLocalRepository

class AtualizarConferenciaUseCase:
    def __init__(self):
        self.repo = ConferenciaRepository()

    def executar(self, lista_dados):
        self.repo.salvar_lista(lista_dados)

class AtualizarDetalhadoProdutoUseCase:
    def __init__(self):
        self.repo = DetalhadoProdutoRepository()

    def executar(self, dados):
        self.repo.salvar_lista(dados)
    
class AtualizarEstoqueFisicoUseCase:
    def __init__(self):
        self.repo = EstoqueFisicoRepository()

    def executar(self, dados):
        self.repo.salvar_lista(dados)

class AtualizarEstoquePorLocalUseCase:
    def __init__(self):
        self.repo = EstoquePorLocalRepository()

    def executar(self, dados):
        self.repo.salvar_lista(dados)

class AtualizarMetaPorLocalUseCase:
    def __init__(self):
        self.repo = MetaPorLocalRepository()

    def executar(self, dados):
        self.repo.salvar_lista(dados)