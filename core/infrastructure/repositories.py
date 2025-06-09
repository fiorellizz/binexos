from core.infrastructure.models import ConferenciaModel, DetalhadoProdutoModel, EstoqueFisicoModel, EstoquePorLocalModel, MetaPorLocalModel, MetaPorVendedorModel

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