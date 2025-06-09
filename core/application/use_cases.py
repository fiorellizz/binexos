from core.infrastructure.repositories import ConferenciaRepository, DetalhadoProdutoRepository, EstoqueFisicoRepository, EstoquePorLocalRepository, MetaPorLocalRepository, MetaPorVendedorRepository, TradeInRepository, ValoresAReceberRepository, VendedorRepository

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

class AtualizarMetaPorVendedorUseCase:
    def __init__(self):
        self.repo = MetaPorVendedorRepository()

    def executar(self, dados):
        self.repo.salvar_lista(dados)

class AtualizarTradeInUseCase:
    def __init__(self):
        self.repo = TradeInRepository()

    def executar(self, dados):
        self.repo.salvar_lista(dados)

class AtualizarValoresReceberUseCase:
    def __init__(self):
        self.repo = ValoresAReceberRepository()

    def executar(self, dados):
        self.repo.salvar_lista(dados)

class AtualizarVendedoresUseCase:
    def __init__(self):
        self.repo = VendedorRepository()

    def executar(self, dados):
        self.repo.salvar_lista(dados)