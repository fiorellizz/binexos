import os
import django
import time
import requests
from datetime import datetime, timedelta
from requests.auth import HTTPBasicAuth

from core.infrastructure.models import ValoresAReceberModel, VendaPorProdutoModel
from core.utils.sincronizacao import limpar_modelos

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meu_projeto.settings")
django.setup()

from core.application.use_cases import (
    # AtualizarConferenciaUseCase,
    AtualizarValoresReceberUseCase,
    AtualizarVendaPorProdutoUseCase,
    # AtualizarDetalhadoProdutoUseCase,
    # # AtualizarServicosUseCase,
    # AtualizarTradeInUseCase,
    # AtualizarEstoqueFisicoUseCase,
    # AtualizarEstoquePorLocalUseCase,
    # AtualizarVendedoresUseCase,
    # AtualizarMetaPorLocalUseCase,
    # AtualizarMetaPorVendedorUseCase,
)

BASE_URL = "https://self.controlecelular.com.br/api/v1/"
USERNAME = "CAIO"
PASSWORD = "2a6bbc77b6edd3c26fca43defeed5ebc"

HEADERS = {
    "User-Agent": "PowerBI-Sync",
    "Accept": "*/*",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive"
}

def obter_token():
    url = f"{BASE_URL}atoken/index.php"
    response = requests.get(url, auth=HTTPBasicAuth(USERNAME, PASSWORD), headers=HEADERS)
    response.raise_for_status()
    return response.json()["access_token"]

def solicitar_recibo(token, idRelat, data_ini=None, data_fin=None):
    url = f"{BASE_URL}relatorios/"
    params = {"idRelat": idRelat, "com": "gerarRelatorio"}
    if data_ini and data_fin:
        params.update({"data_ini": data_ini.strftime("%Y-%m-%d"), 
                      "data_fin": data_fin.strftime("%Y-%m-%d")})
    headers = HEADERS.copy()
    headers["Authorization"] = f"Bearer {token}"

    while True:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()["recibo"]
        elif response.status_code == 400:
            continue
        else:
            raise Exception(f"Erro ao solicitar recibo {idRelat}: {response.status_code} {response.text}")

def montar_dicts(head, body):
    labels = [item["label"] for item in head[0].values()]
    return [dict(zip(labels, linha)) for linha in body]

def baixar_relatorio(token, idRelat, recibo):
    url = f"{BASE_URL}relatorios/"
    headers = HEADERS.copy()
    headers["Authorization"] = f"Bearer {token}"

    for _ in range(50):
        response = requests.get(url, headers=headers, params={"idRelat": idRelat, "recibo": recibo})
        if response.status_code == 200:
            data = response.json()
            head = data.get("head")
            body = data.get("body", [])
            return montar_dicts(head, body)
        elif response.status_code == 202:
            time.sleep(5)
        elif response.status_code == 400:
            continue
        else:
            print(f"Erro ao baixar relatório {idRelat}: {response.status_code}")
            return []
    return []

# def baixar_paginado(token, endpoint_url):
#     headers = HEADERS.copy()
#     headers["Authorization"] = f"Bearer {token}"
#     all_rows = []

#     while True:
#         response = requests.get(endpoint_url, headers=headers, params={"data_ini": data_ini, "data_fin": data_fin})
#         if response.status_code == 200:
#             break
#         elif response.status_code == 400:
#             continue
#         else:
#             print(f"Erro ao iniciar paginação: {response.status_code}")
#             return []

#     info = response.json().get("info", {})
#     total = info.get("totalReg", 0)
#     per_page = info.get("regPerPage", 1)
#     total_pages = (total + per_page - 1) // per_page

#     for page in range(1, total_pages + 1):
#         while True:
#             resp = requests.get(endpoint_url, headers=headers, params={
#                 "data_ini": data_ini,
#                 "data_fin": data_fin,
#                 "currentPage": page
#             })
#             if resp.status_code == 200:
#                 break
#             elif resp.status_code == 400:
#                 continue
#             elif resp.status_code == 401:
#                 token = obter_token()
#                 headers["Authorization"] = f"Bearer {token}"
#                 break
#             else:
#                 print(f"Erro na página {page}: {resp.status_code}")
#                 return all_rows

#         rows = resp.json().get("list", [])
#         all_rows.extend(rows)
#         print(f"Página {page}/{total_pages} com {len(rows)} registros")

#     return all_rows

def baixar_relatorio_por_data(token, idRelat, recibo, data_ini, data_fin):
    url = f"{BASE_URL}relatorios/"
    headers = HEADERS.copy()
    headers["Authorization"] = f"Bearer {token}"

    for _ in range(50):
        response = requests.get(
            url,
            headers=headers,
            params={
                "idRelat": idRelat,
                "recibo": recibo,
                "data_ini": data_ini.strftime("%Y-%m-%d"),
                "data_fin": data_fin.strftime("%Y-%m-%d"),
            },
        )
        if response.status_code == 200:
            data = response.json()
            head = data.get("head")
            body = data.get("body", [])
            return montar_dicts(head, body)
        elif response.status_code == 202:
            time.sleep(5)
        elif response.status_code == 400:
            continue
        else:
            print(f"Erro ao baixar relatório {idRelat}: {response.status_code}")
            return []
    return []

def gerar_periodos():
    hoje = datetime.today()
    periodos = []

    # Mês atual
    inicio_mes_atual = hoje.replace(day=1)
    fim_mes_atual = (inicio_mes_atual + timedelta(days=32)).replace(day=1) - timedelta(days=1)
    periodos.append(("Mês atual", inicio_mes_atual, fim_mes_atual))

    # Mês anterior
    inicio_mes_passado = (inicio_mes_atual - timedelta(days=1)).replace(day=1)
    fim_mes_passado = inicio_mes_atual - timedelta(days=1)
    periodos.append(("Mês passado", inicio_mes_passado, fim_mes_passado))

    # Mesmo mês do ano anterior
    try:
        inicio_mes_ano_passado = inicio_mes_atual.replace(year=inicio_mes_atual.year - 1)
        fim_mes_ano_passado = fim_mes_atual.replace(year=fim_mes_atual.year - 1)
    except ValueError:  # fevereiro 29
        inicio_mes_ano_passado = inicio_mes_atual.replace(year=inicio_mes_atual.year - 1, day=28)
        fim_mes_ano_passado = fim_mes_atual.replace(year=fim_mes_atual.year - 1, day=28)
    periodos.append(("Mesmo mês do ano passado", inicio_mes_ano_passado, fim_mes_ano_passado))

    return periodos

def sincronizar():

    # Horario inicial
    print(f"🕒 Iniciando sincronização em {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Limpar modelos antes de sincronizar
    limpar_modelos([
        ValoresAReceberModel,
        VendaPorProdutoModel
    ])
    
    token = obter_token()

    relatorios_recibo = [
        # ("integracao/atendimentos/detalhado_produto/", AtualizarDetalhadoProdutoUseCase, True),
        ("integracaoV2/operadora/valores_a_receber/", AtualizarValoresReceberUseCase, True),
        ("integracaoV2/produtos/venda_por_produto/", AtualizarVendaPorProdutoUseCase, True)
        # ("integracao/atendimentos/servicos/", AtualizarServicosUseCase, True),
        # ("integracao/utilitarios/trade_in/", AtualizarTradeInUseCase, True),
        # ("integracao/produtos/estoque_fisico/", AtualizarEstoqueFisicoUseCase, False),
        # ("integracao/produtos/estoque_por_local/", AtualizarEstoquePorLocalUseCase, False),
        # ("integracao/vendedores/cadastro/", AtualizarVendedoresUseCase, False),
        # ("integracao/utilitarios/meta_por_local/", AtualizarMetaPorLocalUseCase, False),
        # ("integracao/utilitarios/meta_por_vendedor/", AtualizarMetaPorVendedorUseCase, False),
    ]

    for label, data_ini_periodo, data_fin_periodo in gerar_periodos():
        print(f"\n📅 Sincronizando período: {label} ({data_ini_periodo.date()} a {data_fin_periodo.date()})")
        
        for endpoint, use_case_class, incluir_datas in relatorios_recibo:
            print(f"\n➡️ Relatório {endpoint}")
            try:
                recibo = solicitar_recibo(token, endpoint, 
                                        data_ini_periodo if incluir_datas else None, 
                                        data_fin_periodo if incluir_datas else None)
                dados = baixar_relatorio_por_data(token, endpoint, recibo, data_ini_periodo, data_fin_periodo)
                use_case_class().executar(dados)
                print(f"✅ {len(dados)} registros sincronizados para {endpoint} ({label})")
            except Exception as e:
                print(f"❌ Erro ao processar {endpoint} para {label}: {str(e)}")

    # Horario final
    print(f"✅ Sincronização concluída em {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # token = obter_token()

    # relatorios_paginados = {
    #     # "conferencia": {
    #     #     "url": f"{BASE_URL}integracaoV1/atendimentos/conferencia/",
    #     #     "use_case": AtualizarConferenciaUseCase
    #     # }
    # }

    # for nome, config in relatorios_paginados.items():
    #     print(f"\n🔄 Paginado: {nome}")
    #     dados = baixar_paginado(token, config["url"])
    #     config["use_case"]().executar(dados)
    #     print(f"✅ {len(dados)} registros sincronizados para {nome}")

def loop_principal():
    while True:
        sincronizar()
        print("🕒 Aguardando 60 minutos...")
        time.sleep(60 * 60)

if __name__ == "__main__":
    loop_principal()