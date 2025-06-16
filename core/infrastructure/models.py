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
    cod_claro = models.CharField(max_length=50)
    nome = models.CharField(max_length=255)
    atendimento = models.IntegerField()
    cpf = models.CharField(max_length=20)
    data = models.DateField()
    id_ativacao = models.CharField(max_length=50)
    ativacao = models.CharField(max_length=100)
    ntc = models.CharField(max_length=50, blank=True)
    cod_plano = models.CharField(max_length=100)
    plano = models.CharField(max_length=255)
    iccid = models.CharField(max_length=50, blank=True)
    imei = models.CharField(max_length=50, blank=True)
    descricao = models.CharField(max_length=255, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    desconto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    motivo_desconto = models.CharField(max_length=255, blank=True)
    desconto_1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    desconto_2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    motivo_desconto_2 = models.CharField(max_length=255, blank=True)
    cod_tabela = models.CharField(max_length=50, blank=True)
    desc_tabela = models.CharField(max_length=255, blank=True)
    valor_tabela = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    data_tabela = models.DateField(null=True, blank=True)
    protocolo_ativacao = models.CharField(max_length=255, blank=True)
    vendedor = models.CharField(max_length=255)
    nf_numero = models.CharField(max_length=100, blank=True)
    modelo_nf = models.CharField(max_length=100, blank=True)
    contrato = models.CharField(max_length=100, blank=True)
    margem = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    margem_percentual = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    custo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rebate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    valor_cartao = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    valor_adicional = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    adicional_parcelas = models.IntegerField(null=True, blank=True)
    comissao_percentual = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    data_entrada = models.DateField(null=True, blank=True)
    nf_entrada = models.CharField(max_length=100, blank=True)
    comissao = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rebate_2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fidelidade = models.CharField(max_length=50, blank=True)
    cod_combo = models.CharField(max_length=50, blank=True)
    tipo_combo = models.CharField(max_length=100, blank=True)
    area_cabeada = models.CharField(max_length=10, blank=True)
    status_ged = models.CharField(max_length=50, blank=True)
    autorizacao_desconto = models.CharField(max_length=100, blank=True)
    protocolo_ged = models.CharField(max_length=100, blank=True)
    tipo_lancamento = models.CharField(max_length=100, blank=True)
    id_comissao = models.CharField(max_length=100, blank=True)
    acoes = models.TextField(blank=True)
    promocoes = models.TextField(blank=True)
    assinatura = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    plano_anterior = models.CharField(max_length=255, blank=True)
    assinatura_anterior = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    delta = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    aparelho_fidelidade_anterior = models.CharField(max_length=255, blank=True)
    aparelho_fidelidade = models.CharField(max_length=255, blank=True)
    protocolo_desconto_1 = models.CharField(max_length=100, blank=True)
    protocolo_desconto_2 = models.CharField(max_length=100, blank=True)
    aceite = models.CharField(max_length=10, blank=True)
    preco_pre = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    acrescimo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    local_compra = models.CharField(max_length=255, blank=True)
    situacao = models.CharField(max_length=255, blank=True)
    vendimento = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    ntc_provisorio = models.CharField(max_length=50, blank=True)
    canal_venda = models.CharField(max_length=100, blank=True)
    oferta = models.CharField(max_length=255, blank=True)
    cod_local = models.CharField(max_length=50, blank=True)
    contestar_residencial = models.CharField(max_length=10, blank=True)
    cpf_vendedor = models.CharField(max_length=20, blank=True)
    cod_vendedor = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.nome} - {self.vendedor} - {self.data}"

class VendedorModel(models.Model):
    codigo = models.CharField(max_length=50)
    nome = models.CharField(max_length=255)
    gerente = models.CharField(max_length=5)
    bloqueado = models.CharField(max_length=5)
    local = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.nome} ({self.codigo})"

class VendaPorProdutoModel(models.Model):
    data = models.DateField()
    cod_produto = models.IntegerField()
    descricao = models.CharField(max_length=255)
    origem = models.IntegerField()
    qtd = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    custo_total = models.DecimalField(max_digits=10, decimal_places=2)
    local = models.CharField(max_length=255)
    cod_local = models.IntegerField()
    vendedor = models.CharField(max_length=255)
    cod_vendedor = models.IntegerField()
    ncm = models.CharField(max_length=20, blank=True)
    cpf = models.CharField(max_length=20, blank=True)
    grupo = models.CharField(max_length=100, blank=True)
    marca = models.CharField(max_length=100, blank=True)
    cod_barras = models.CharField(max_length=50)
    cod_tipo = models.IntegerField()
    cadastro_geral = models.IntegerField()