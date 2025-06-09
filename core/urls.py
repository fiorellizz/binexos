from django.urls import path
from core.interfaces.views import ConferenciaAPIView, DetalhadoProdutoAPIView, EstoqueFisicoAPIView, EstoquePorLocalAPIView, MetaPorLocalAPIView, MetaPorVendedorAPIView, TradeInAPIView, ValoresAReceberAPIView

urlpatterns = [
    path('dados/conferencia/', ConferenciaAPIView.as_view(), name='conferencia'),
    path("dados/detalhado_produto/", DetalhadoProdutoAPIView.as_view(), name="detalhado_produto"),
    path("dados/estoque_fisico/", EstoqueFisicoAPIView.as_view(), name="estoque_fisico"),
    path("dados/estoque_por_local/", EstoquePorLocalAPIView.as_view(), name="estoque_por_local"),
    path("dados/meta_por_local/", MetaPorLocalAPIView.as_view(), name="meta_por_local"),
    path("dados/meta_por_vendedor/", MetaPorVendedorAPIView.as_view(), name="meta_por_vendedor"),
    path("dados/trade_in/", TradeInAPIView.as_view(), name="trade_in"),
    path("dados/valores_a_receber/", ValoresAReceberAPIView.as_view(), name="valores_a_receber"),
]