from core.infrastructure.models import ConferenciaModel, DetalhadoProdutoModel, EstoqueFisicoModel, EstoquePorLocalModel, MetaPorLocalModel, MetaPorVendedorModel, TradeInModel, ValoresAReceberModel, VendedorModel, VendaPorProdutoModel

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
                cod_claro=item.get("Cod Claro", ""),
                nome=item.get("Nome", ""),
                atendimento=parse_int(item.get("Atendimento")),
                cpf=item.get("CPF", ""),
                data=parse_date(item.get("Data")),
                id_ativacao=item.get("ID Ativação", ""),
                ativacao=item.get("Ativação", ""),
                ntc=item.get("NTC", ""),
                cod_plano=item.get("Cod Plano", ""),
                plano=item.get("Plano", ""),
                iccid=item.get("ICCID", ""),
                imei=item.get("IMEI", ""),
                descricao=item.get("Descrição", ""),
                valor=parse_float(item.get("Valor")),
                desconto=parse_float(item.get("Desconto")),
                motivo_desconto=item.get("Motivo desconto", ""),
                desconto_1=parse_float(item.get("Desconto 1")),
                desconto_2=parse_float(item.get("Desconto 2")),
                motivo_desconto_2=item.get("Motivo desconto 2", ""),
                cod_tabela=item.get("Cod Tabela", ""),
                desc_tabela=item.get("Desc Tabela", ""),
                valor_tabela=parse_float(item.get("Valor tabela")),
                data_tabela=parse_date(item.get("Data tabela")),
                protocolo_ativacao=item.get("Protocolo Ativação", ""),
                vendedor=item.get("Vendedor", ""),
                nf_numero=item.get("Nº NF", ""),
                modelo_nf=item.get("Modelo NF", ""),
                contrato=item.get("Contrato", ""),
                margem=parse_float(item.get("Margem")),
                margem_percentual=parse_float(item.get("Margem %")),
                custo=parse_float(item.get("Custo")),
                rebate=parse_float(item.get("Rebate")),
                valor_cartao=parse_float(item.get("Valor Cartão")),
                valor_adicional=parse_float(item.get("Valor Adicional")),
                adicional_parcelas=parse_int(item.get("Adicional Parcelas")),
                comissao_percentual=parse_float(item.get("Comissão %")),
                data_entrada=parse_date(item.get("Data Entrada")),
                nf_entrada=item.get("NF Entrada", ""),
                comissao=parse_float(item.get("Comissão")),
                rebate_2=parse_float(item.get("Rebate")),
                fidelidade=item.get("Fidelidade", ""),
                cod_combo=item.get("Cod Combo", ""),
                tipo_combo=item.get("Tipo Combo", ""),
                area_cabeada=item.get("Área Cabeada", ""),
                status_ged=item.get("Status GED", ""),
                autorizacao_desconto=item.get("Autorização de desconto", ""),
                protocolo_ged=item.get("Protocolo GED", ""),
                tipo_lancamento=item.get("Tipo Lançamento", ""),
                id_comissao=item.get("ID Comissão", ""),
                acoes=item.get("Ações", ""),
                promocoes=item.get("Promoções", ""),
                assinatura=parse_float(item.get("Assinatura")),
                plano_anterior=item.get("Plano Anterior", ""),
                assinatura_anterior=parse_float(item.get("Assinatura Anterior")),
                delta=parse_float(item.get("Delta")),
                aparelho_fidelidade_anterior=item.get("Aparelho / Fidelidade (anterior)", ""),
                aparelho_fidelidade=item.get("Aparelho / Fidelidade", ""),
                protocolo_desconto_1=item.get("Protocolo Desconto 1", ""),
                protocolo_desconto_2=item.get("Protocolo Desconto 2", ""),
                aceite=item.get("Aceite", ""),
                preco_pre=parse_float(item.get("Preço pré")),
                acrescimo=parse_float(item.get("Acréscimo")),
                local_compra=item.get("Local Compra", ""),
                situacao=item.get("Situação", ""),
                vendimento=item.get("Vendimento", ""),
                email=item.get("Email", ""),
                ntc_provisorio=item.get("NTC Provisório", ""),
                canal_venda=item.get("Canal de Venda", ""),
                oferta=item.get("Oferta", ""),
                cod_local=item.get("Cod Local", ""),
                contestar_residencial=item.get("Contestar Residencial", ""),
                cpf_vendedor=item.get("CPF Vendedor", ""),
                cod_vendedor=item.get("Cod Vendedor", "")
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

class VendaPorProdutoRepository:
    def salvar_lista(self, lista):
        VendaPorProdutoModel.objects.all().delete()
        for item in lista:
            VendaPorProdutoModel.objects.create(
                data=parse_date(item.get("Data")),
                cod_produto=parse_int(item.get("Cód Produto")),
                descricao=item.get("Descrição", ""),
                origem=parse_int(item.get("Origem")),
                qtd=parse_int(item.get("Qtd")),
                subtotal=parse_float(item.get("Sub-Total")),
                custo_total=parse_float(item.get("Custo Total")),
                local=item.get("Local", ""),
                cod_local=parse_int(item.get("Cod Local")),
                vendedor=item.get("Vendedor", ""),
                cod_vendedor=parse_int(item.get("Cod vendedor")),
                ncm=item.get("NCM/SH", ""),
                cpf=item.get("CPF", ""),
                grupo=item.get("Grupo", ""),
                marca=item.get("Marca", ""),
                cod_barras=item.get("Cod Barras", ""),
                cod_tipo=parse_int(item.get("Cod Tipo")),
                cadastro_geral=parse_int(item.get("Cadastro Geral")),
            )