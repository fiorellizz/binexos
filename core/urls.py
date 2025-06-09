from django.urls import path
from core.interfaces.views import ConferenciaAPIView, DetalhadoProdutoAPIView, EstoqueFisicoAPIView, EstoquePorLocalAPIView

urlpatterns = [
    path('dados/', ConferenciaAPIView.as_view(), name='dados'),
    path("dados/detalhado_produto/", DetalhadoProdutoAPIView.as_view(), name="detalhado_produto"),
    path("dados/estoque_fisico/", EstoqueFisicoAPIView.as_view(), name="estoque_fisico"),
    path("dados/estoque_por_local/", EstoquePorLocalAPIView.as_view(), name="estoque_por_local"),
]