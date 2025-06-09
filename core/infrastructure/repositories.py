from core.infrastructure.models import ConferenciaModel, DetalhadoProdutoModel, EstoqueFisicoModel, EstoquePorLocalModel, MetaPorLocalModel, MetaPorVendedorModel, TradeInModel, ValoresAReceberModel, VendedorModel

def parse_int(val):
    try:
        return int(val)
    except:
        return None

def parse_float(val):
    try:
        return float(val)
    except (ValueError, TypeError):
        return 0.0

def parse_date(valor):
    from datetime import datetime
    for fmt in ("%Y-%m-%d", "%d/%m/%Y"):
        try:
            return datetime.strptime(valor, fmt).date()
        except (ValueError, TypeError):
            continue
    return None

class ConferenciaRepository:
    def salvar_lista(self, lista_dados):
        ConferenciaModel.objects.all().delete()
        for row in lista_dados:
            ConferenciaModel.objects.create(
                deslocal=row.get("deslocal", ""),
                destipo=row.get("destipo", ""),
                codmarca=parse_int(row.get("codmarca")),
                desc_marca=row.get("desc_marca", ""),
                nomvendedor=row.get("nomvendedor", ""),
                status_ged=row.get("status_ged", ""),
                desplano=row.get("desplano", ""),
                descricao=row.get("descricao", ""),
                data=parse_date(row.get("data")),
                valorpago=parse_float(row.get("valorpago")),
                custo=parse_float(row.get("custo")),
                desativacao=row.get("desativacao", ""),
                codmovimen=parse_int(row.get("codmovimen")),
                quantidade=parse_int(row.get("quantidade")),
                estado_cliente=row.get("estado_cliente", ""),
                cobertura_residenc=row.get("cobertura_residenc", ""),
                atend=parse_int(row.get("atend")),
                preco=parse_float(row.get("preco")),
                acrescimo=parse_float(row.get("acrescimo")),
                desconto1=parse_float(row.get("desconto1")),
                motivod=row.get("motivod", ""),
                desconto2=parse_float(row.get("desconto2")),
                motivod2=row.get("motivod2", ""),
                desconto3=parse_float(row.get("desconto3")),
                motivod3=row.get("motivod3", ""),
                desconto_total=parse_float(row.get("desconto_total")),
            )

class DetalhadoProdutoRepository:
    def salvar_lista(self, lista):
        DetalhadoProdutoModel.objects.all().delete()
        for item in lista:
            DetalhadoProdutoModel.objects.create(
                cod_cliente=item.get("Cod Cliente", ""),
                cod_local=item.get("Cod local", ""),
                nome_local=item.get("Nome local", ""),
                data=parse_date(item.get("Data")),
                id_base=item.get("Id", ""),
                numero=item.get("Número", ""),
                modelo=item.get("Modelo", ""),
                descricao=item.get("Descrição", ""),
                num_serie=item.get("Num Série", ""),
                dias_estoque=parse_int(item.get("Dias no estoque")),
                qtd=parse_int(item.get("Qtd")),
                preco=parse_float(item.get("Preço")),
                acrescimo=parse_float(item.get("Acréscimo")),
                desconto=parse_float(item.get("Desconto")),
                desconto1=parse_float(item.get("Desconto 1")),
                motivo_desc1=item.get("Motivo Desc 1", ""),
                protocolo_desc1=item.get("Protocolo Desc 1", ""),
                desconto2=parse_float(item.get("Desconto 2")),
                motivo_desc2=item.get("Motivo Desc 2", ""),
                protocolo_desc2=item.get("Protocolo Desc 2", ""),
                vl_pago=parse_float(item.get("Vl Pago")),
                custo=parse_float(item.get("Custo")),
                vendedor=item.get("Vendedor", ""),
                cod_produto=item.get("Cod Produto", ""),
                cod_vendedor=item.get("Cod Vendedor", ""),
            )

class EstoqueFisicoRepository:
    def salvar_lista(self, lista):
        EstoqueFisicoModel.objects.all().delete()
        for item in lista:
            EstoqueFisicoModel.objects.create(
                descricao=item.get("Descrição", ""),
                estoque=parse_int(item.get("Estoque")),
                dias=parse_int(item.get("Dias")),
                defeito=item.get("Defeito", ""),
                local=item.get("Local", ""),
                tipo=item.get("Tipo", ""),
                data_entrada=parse_date(item.get("Data Entrada")),
                venda=parse_float(item.get("Venda")),
                custo=parse_float(item.get("Custo")),
            )

class EstoquePorLocalRepository:
    def salvar_lista(self, lista):
        EstoquePorLocalModel.objects.all().delete()
        for item in lista:
            EstoquePorLocalModel.objects.create(
                cod_produto=item.get("Cod Produto", ""),
                descricao=item.get("Descrição", ""),
                cod_local=item.get("Cod Local", ""),
                local=item.get("Local", ""),
                estoque=parse_int(item.get("Estoque"))
            )

class MetaPorLocalRepository:
    def salvar_lista(self, lista):
        MetaPorLocalModel.objects.all().delete()
        for item in lista:
            MetaPorLocalModel.objects.create(
                mes=parse_int(item.get("Mês")),
                ano=parse_int(item.get("Ano")),
                local=item.get("Local", ""),
                grupo=item.get("Grupo", ""),
                descricao=item.get("Descrição", ""),
                meta_por_valor=item.get("Meta por valor", ""),
                qtd=parse_int(item.get("Qtd")),
                valor=parse_float(item.get("Valor"))
            )

class MetaPorVendedorRepository:
    def salvar_lista(self, lista):
        MetaPorVendedorModel.objects.all().delete()
        for item in lista:
            MetaPorVendedorModel.objects.create(
                mes=parse_int(item.get("Mês")),
                ano=parse_int(item.get("Ano")),
                vendedor=item.get("Vendedor", "") or "",
                grupo=item.get("Grupo", ""),
                descricao=item.get("Descrição", ""),
                meta_por_valor=item.get("Meta por valor", ""),
                qtd=parse_int(item.get("Qtd")),
                valor=parse_float(item.get("Valor"))
            )

class TradeInRepository:
    def salvar_lista(self, lista):
        TradeInModel.objects.all().delete()
        for item in lista:
            TradeInModel.objects.create(
                data_atend=parse_date(item.get("Data Atend")),
                id_atend=parse_int(item.get("Id Atend")),
                empresa=item.get("Empresa", ""),
                id_registro=item.get("Id Registro", ""),
                desc_produto=item.get("Desc Produto", ""),
                imei=item.get("Imei", ""),
                imei_novo=item.get("Imei Novo", ""),
                valor=parse_float(item.get("Valor")),
                situacao=item.get("Situação", ""),
                cod_local=item.get("Cod Local", ""),
                local=item.get("Local", ""),
                vendedor=item.get("Vendedor", ""),
                cliente=item.get("Cliente", ""),
                situacao_caixa=item.get("Situação Caixa", ""),
                id_base=parse_int(item.get("Id")),
                id_situacao=parse_int(item.get("Id Situação")),
            )

class ValoresAReceberRepository:
    def salvar_lista(self, lista):
        ValoresAReceberModel.objects.all().delete()
        for item in lista:
            ValoresAReceberModel.objects.create(
                nome=item.get("nome", ""),
                data=parse_date(item.get("data")),
                atend=parse_int(item.get("atend")),
                tipo=item.get("tipo", ""),
                plano=item.get("plano", ""),
                descricao=item.get("descricao", ""),
                nomvendedor=item.get("nomvendedor", ""),
                dessituacao=item.get("dessituacao", ""),
                status_ged=item.get("status_ged", ""),
                comissao=parse_float(item.get("comissao")),
                comissaor=parse_float(item.get("comissaor")),
                comissao_premium=parse_float(item.get("comissao_premium")),
                comissaor_premium=parse_float(item.get("comissaor_premium")),
                comissao_max=parse_float(item.get("comissao_max")),
                comissaor_max=parse_float(item.get("comissaor_max")),
                operadorap=item.get("operadorap", ""),
                cidadecliente=item.get("cidadecliente", ""),
                codclaro=item.get("codclaro", ""),
                assinatura=parse_float(item.get("assinatura")),
                delta=parse_float(item.get("delta")),
                rebate=parse_float(item.get("rebate")),
                valorcartao=parse_float(item.get("valorcartao")),
                valoradic=parse_float(item.get("valoradic")),
                codmovimen=parse_int(item.get("codmovimen")),
                auditoria_cc=item.get("auditoria_cc", ""),
                auditoria_cr=item.get("auditoria_cr", ""),
                margem=parse_float(item.get("margem")),
                margemp=parse_float(item.get("margemp")),
                instalacao=item.get("instalacao", ""),
                franquia_total=parse_float(item.get("franquia_total")),
                dtvencimento=parse_date(item.get("dtvencimento")),
                obs=item.get("obs", ""),
                estado_cliente=item.get("estado_cliente", ""),
                cobertura_residenc=item.get("cobertura_residenc", "")
            )

class VendedorRepository:
    def salvar_lista(self, lista):
        VendedorModel.objects.all().delete()
        for item in lista:
            VendedorModel.objects.create(
                codigo=item.get("Código", ""),
                nome=item.get("Nome", ""),
                gerente=item.get("Gerente", ""),
                bloqueado=item.get("Bloqueado", ""),
                local=item.get("Local", "")
            )