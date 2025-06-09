# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.renderers import JSONRenderer
# import time
# import requests
# from requests.auth import HTTPBasicAuth

# class RelatorioAPIView(APIView):
#     renderer_classes = [JSONRenderer]

#     def get(self, request):
#         base_url = "https://self.controlecelular.com.br/api/v1/"
#         token_url = f"{base_url}atoken/index.php"
#         username = "CAIO"
#         password = "2a6bbc77b6edd3c26fca43defeed5ebc"
#         data_ini = "2023-05-01"
#         data_fin = "2025-05-31"

#         headers = {
#             "User-Agent": "PostmanRuntime/7.44.0",
#             "Accept": "/",
#             "Cache-Control": "no-cache"
#         }

#         def obter_token():
#             resp = requests.get(token_url, auth=HTTPBasicAuth(username, password), headers=headers)
#             if resp.status_code == 200:
#                 return resp.json()["access_token"]
#             raise Exception("Erro ao obter token")

#         def solicitar_relatorio(token, idRelat, incluir_datas=True):
#             auth_headers = headers.copy()
#             auth_headers["Authorization"] = f"Bearer {token}"

#             params = {
#                 "idRelat": idRelat,
#                 "com": "gerarRelatorio"
#             }
#             if incluir_datas:
#                 params["data_ini"] = data_ini
#                 params["data_fin"] = data_fin

#             recibo_resp = requests.get(f"{base_url}relatorios/", headers=auth_headers, params=params)

#             if recibo_resp.status_code != 200:
#                 raise Exception(f"Erro ao solicitar recibo: {recibo_resp.text}")

#             recibo = recibo_resp.json().get("recibo")

#             for _ in range(50):
#                 time.sleep(2)
#                 dados_resp = requests.get(
#                     f"{base_url}relatorios/",
#                     headers=auth_headers,
#                     params={"idRelat": idRelat, "recibo": recibo}
#                 )

#                 while dados_resp.status_code == 400:
#                     dados_resp = requests.get(
#                         f"{base_url}relatorios/",
#                         headers=auth_headers,
#                         params={"idRelat": idRelat, "recibo": recibo}
#                     )

#                 if dados_resp.status_code == 200:
#                     report_data = dados_resp.json()
#                     headers_dict = list(report_data["head"][0].values())
#                     column_names = [h["label"] for h in headers_dict]
#                     rows = report_data["body"]
#                     resultado = [dict(zip(column_names, row)) for row in rows]
#                     return resultado

#                 elif dados_resp.status_code == 202:
#                     continue

#             return []

#         def relatorio_paginado(token, url):
#             auth_headers = headers.copy()
#             auth_headers["Authorization"] = f"Bearer {token}"
#             params = {"data_ini": data_ini, "data_fin": data_fin}

#             response = requests.get(url, headers=auth_headers, params=params)
#             while response.status_code == 400:
#                 response = requests.get(url, headers=auth_headers, params=params)

#             if response.status_code != 200:
#                 raise Exception(f"Erro ao obter info inicial: {response.text}")

#             data = response.json()
#             info = data.get("info", {})
#             total = info.get("totalReg", 0)
#             por_pagina = info.get("regPerPage", 1)
#             paginas = (total + por_pagina - 1) // por_pagina

#             todos_dados = []

#             for p in range(1, paginas + 1):
#                 params["currentPage"] = p
#                 resp = requests.get(url, headers=auth_headers, params=params)
#                 while resp.status_code == 400:
#                     resp = requests.get(url, headers=auth_headers, params=params)

#                 if resp.status_code != 200:
#                     break

#                 lista = resp.json().get("list", [])
#                 todos_dados.extend(lista)

#             return todos_dados

#         try:
#             token = obter_token()

#             relatorios_normais = [
#                 ("integracao/atendimentos/detalhado_produto/", True),
#                 ("integracao/atendimentos/servicos/", True),
#                 ("integracao/utilitarios/trade_in/", True),
#                 ("integracao/produtos/estoque_fisico/", False),
#                 ("integracao/produtos/estoque_por_local/", False),
#                 ("integracao/vendedores/cadastro/", False),
#                 ("integracao/utilitarios/meta_por_local/", False),
#                 ("integracao/utilitarios/meta_por_vendedor/", False),
#             ]

#             relatorios_paginados = [
#                 f"{base_url}integracaoV1/operadora/valores_a_receber/",
#                 f"{base_url}integracaoV1/atendimentos/conferencia/",
#             ]

#             dados_finais = []
#             for idRelat, incluir_data in relatorios_normais:
#                 dados = solicitar_relatorio(token, idRelat, incluir_data)
#                 dados_finais.extend(dados)

#             for url in relatorios_paginados:
#                 dados = relatorio_paginado(token, url)
#                 dados_finais.extend(dados)

#             return Response(dados_finais)

#         except Exception as e:
#             return Response({"erro": str(e)}, status=500)