class Conferencia:
    def __init__(
        self,
        deslocal, destipo, codmarca, desc_marca, nomvendedor, status_ged,
        desplano, descricao, data, valorpago, custo, desativacao,
        codmovimen, quantidade, estado_cliente, cobertura_residenc,
        atend, preco, acrescimo, desconto1, motivod,
        desconto2, motivod2, desconto3, motivod3, desconto_total
    ):
        self.deslocal = deslocal
        self.destipo = destipo
        self.codmarca = codmarca
        self.desc_marca = desc_marca
        self.nomvendedor = nomvendedor
        self.status_ged = status_ged
        self.desplano = desplano
        self.descricao = descricao
        self.data = data
        self.valorpago = valorpago
        self.custo = custo
        self.desativacao = desativacao
        self.codmovimen = codmovimen
        self.quantidade = quantidade
        self.estado_cliente = estado_cliente
        self.cobertura_residenc = cobertura_residenc
        self.atend = atend
        self.preco = preco
        self.acrescimo = acrescimo
        self.desconto1 = desconto1
        self.motivod = motivod
        self.desconto2 = desconto2
        self.motivod2 = motivod2
        self.desconto3 = desconto3
        self.motivod3 = motivod3
        self.desconto_total = desconto_total

class DetalhadoProduto:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

class EstoqueFisico:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

class EstoquePorLocal:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

class MetaPorLocal:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

class MetaPorVendedor:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

class TradeIn:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

class ValoresAReceber:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

class Vendedor:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)