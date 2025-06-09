from django.db import models

class ConferenciaModel(models.Model):
    
    deslocal = models.CharField(max_length=255)
    destipo = models.CharField(max_length=255)
    codmarca = models.IntegerField(blank=True, null=True)
    desc_marca = models.CharField(max_length=255)
    nomvendedor = models.CharField(max_length=255)
    status_ged = models.CharField(max_length=50)
    desplano = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    data = models.DateField()
    valorpago = models.DecimalField(max_digits=10, decimal_places=2)
    custo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    desativacao = models.CharField(max_length=255)
    codmovimen = models.IntegerField(blank=True, null=True)
    quantidade = models.PositiveIntegerField(blank=True, null=True)
    estado_cliente = models.CharField(max_length=50)
    cobertura_residenc = models.CharField(max_length=50)
    atend = models.PositiveIntegerField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    acrescimo = models.DecimalField(max_digits=10, decimal_places=2)
    desconto1 = models.DecimalField(max_digits=10, decimal_places=2)
    motivod = models.CharField(max_length=255)
    desconto2 = models.DecimalField(max_digits=10, decimal_places=2)
    motivod2 = models.CharField(max_length=255)
    desconto3 = models.DecimalField(max_digits=10, decimal_places=2)
    motivod3 = models.CharField(max_length=255)
    desconto_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nomvendedor} - {self.deslocal} ({self.data})"

class DetalhadoProdutoModel(models.Model):
    cod_cliente = models.CharField(max_length=50)
    cod_local = models.CharField(max_length=50)
    nome_local = models.CharField(max_length=255)
    data = models.DateField()
    id_base = models.CharField(max_length=50)
    numero = models.CharField(max_length=50)
    modelo = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    num_serie = models.CharField(max_length=255)
    dias_estoque = models.IntegerField(null=True, blank=True)
    qtd = models.IntegerField(null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    acrescimo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    desconto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    desconto1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    motivo_desc1 = models.CharField(max_length=255, blank=True)
    protocolo_desc1 = models.CharField(max_length=255, blank=True)
    desconto2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    motivo_desc2 = models.CharField(max_length=255, blank=True)
    protocolo_desc2 = models.CharField(max_length=255, blank=True)
    vl_pago = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    custo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    vendedor = models.CharField(max_length=255)
    cod_produto = models.CharField(max_length=50)
    cod_vendedor = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.vendedor} - {self.modelo} - {self.numero}"

class EstoqueFisicoModel(models.Model):
    descricao = models.CharField(max_length=255)
    estoque = models.IntegerField(null=True, blank=True)
    dias = models.IntegerField(null=True, blank=True)
    defeito = models.CharField(max_length=10)
    local = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10)
    data_entrada = models.DateField(null=True, blank=True)
    venda = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    custo = models.DecimalField(max_digits=15, decimal_places=3, null=True, blank=True)

    def __str__(self):
        return f"{self.descricao} - {self.local}"

class EstoquePorLocalModel(models.Model):
    cod_produto = models.CharField(max_length=50)
    descricao = models.CharField(max_length=255)
    cod_local = models.CharField(max_length=50)
    local = models.CharField(max_length=255)
    estoque = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.descricao} - {self.local}"

class MetaPorLocalModel(models.Model):
    mes = models.IntegerField()
    ano = models.IntegerField()
    local = models.CharField(max_length=100)
    grupo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    meta_por_valor = models.CharField(max_length=5)
    qtd = models.IntegerField(null=True, blank=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.mes}/{self.ano} - {self.local} - {self.grupo}"

class MetaPorVendedorModel(models.Model):
    mes = models.IntegerField()
    ano = models.IntegerField()
    vendedor = models.CharField(max_length=255, blank=True)
    grupo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    meta_por_valor = models.CharField(max_length=5)
    qtd = models.IntegerField(null=True, blank=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.mes}/{self.ano} - {self.vendedor or 'Sem Vendedor'}"

class TradeInModel(models.Model):
    data_atend = models.DateField()
    id_atend = models.IntegerField()
    empresa = models.CharField(max_length=100)
    id_registro = models.CharField(max_length=100)
    desc_produto = models.CharField(max_length=255)
    imei = models.CharField(max_length=30)
    imei_novo = models.CharField(max_length=30)
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    situacao = models.CharField(max_length=100)
    cod_local = models.CharField(max_length=50)
    local = models.CharField(max_length=255)
    vendedor = models.CharField(max_length=255)
    cliente = models.CharField(max_length=255)
    situacao_caixa = models.CharField(max_length=100)
    id_base = models.IntegerField()
    id_situacao = models.IntegerField()

    def __str__(self):
        return f"{self.desc_produto} - {self.vendedor} - {self.data_atend}"

class ValoresAReceberModel(models.Model):
    nome = models.CharField(max_length=255)
    data = models.DateField()
    atend = models.IntegerField()
    tipo = models.CharField(max_length=100)
    plano = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255, blank=True)
    nomvendedor = models.CharField(max_length=255)
    dessituacao = models.CharField(max_length=100, blank=True)
    status_ged = models.CharField(max_length=50)
    comissao = models.DecimalField(max_digits=10, decimal_places=2)
    comissaor = models.DecimalField(max_digits=10, decimal_places=2)
    comissao_premium = models.DecimalField(max_digits=10, decimal_places=2)
    comissaor_premium = models.DecimalField(max_digits=10, decimal_places=2)
    comissao_max = models.DecimalField(max_digits=10, decimal_places=2)
    comissaor_max = models.DecimalField(max_digits=10, decimal_places=2)
    operadorap = models.CharField(max_length=100, blank=True)
    cidadecliente = models.CharField(max_length=100)
    codclaro = models.CharField(max_length=50)
    assinatura = models.DecimalField(max_digits=10, decimal_places=2)
    delta = models.DecimalField(max_digits=10, decimal_places=2)
    rebate = models.DecimalField(max_digits=10, decimal_places=2)
    valorcartao = models.DecimalField(max_digits=10, decimal_places=2)
    valoradic = models.DecimalField(max_digits=10, decimal_places=2)
    codmovimen = models.IntegerField()
    auditoria_cc = models.CharField(max_length=10)
    auditoria_cr = models.CharField(max_length=10)
    margem = models.DecimalField(max_digits=10, decimal_places=2)
    margemp = models.DecimalField(max_digits=10, decimal_places=2)
    instalacao = models.CharField(max_length=50, blank=True)
    franquia_total = models.DecimalField(max_digits=10, decimal_places=5)
    dtvencimento = models.DateField(null=True, blank=True)
    obs = models.TextField(blank=True)
    estado_cliente = models.CharField(max_length=50)
    cobertura_residenc = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nome} - {self.nomvendedor} - {self.data}"