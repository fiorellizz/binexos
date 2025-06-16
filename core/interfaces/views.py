from rest_framework.views import APIView
from rest_framework.response import Response
from core.decorators import require_token
from core.infrastructure.models import ConferenciaModel, DetalhadoProdutoModel, EstoqueFisicoModel, EstoquePorLocalModel, MetaPorLocalModel, MetaPorVendedorModel, TradeInModel, ValoresAReceberModel, VendaPorProdutoModel, VendedorModel
from core.serializers import ConferenciaSerializer, DetalhadoProdutoSerializer, EstoqueFisicoSerializer, EstoquePorLocalSerializer, MetaPorLocalSerializer, MetaPorVendedorSerializer, TradeInSerializer, ValoresAReceberSerializer, VendaPorProdutoSerializer, VendedorSerializer

class ConferenciaAPIView(APIView):
    @require_token
    def get(self, request):
        queryset = ConferenciaModel.objects.all()
        serializer = ConferenciaSerializer(queryset, many=True)
        return Response(serializer.data)

class DetalhadoProdutoAPIView(APIView):
    @require_token
    def get(self, request):
        dados = DetalhadoProdutoModel.objects.all()
        serializer = DetalhadoProdutoSerializer(dados, many=True)
        return Response(serializer.data)

class EstoqueFisicoAPIView(APIView):

    @require_token
    def get(self, request):
        dados = EstoqueFisicoModel.objects.all()
        serializer = EstoqueFisicoSerializer(dados, many=True)
        return Response(serializer.data)
    
class EstoquePorLocalAPIView(APIView):

    @require_token
    def get(self, request):
        dados = EstoquePorLocalModel.objects.all()
        serializer = EstoquePorLocalSerializer(dados, many=True)
        return Response(serializer.data)

class MetaPorLocalAPIView(APIView):

    @require_token
    def get(self, request):
        dados = MetaPorLocalModel.objects.all()
        serializer = MetaPorLocalSerializer(dados, many=True)
        return Response(serializer.data)
    
class MetaPorVendedorAPIView(APIView):

    @require_token
    def get(self, request):
        dados = MetaPorVendedorModel.objects.all()
        serializer = MetaPorVendedorSerializer(dados, many=True)
        return Response(serializer.data)

class TradeInAPIView(APIView):

    @require_token
    def get(self, request):
        dados = TradeInModel.objects.all()
        serializer = TradeInSerializer(dados, many=True)
        return Response(serializer.data)

class ValoresAReceberAPIView(APIView):

    @require_token
    def get(self, request):
        dados = ValoresAReceberModel.objects.all()
        serializer = ValoresAReceberSerializer(dados, many=True)
        return Response(serializer.data)

class VendedorAPIView(APIView):

    @require_token
    def get(self, request):
        dados = VendedorModel.objects.all()
        serializer = VendedorSerializer(dados, many=True)
        return Response(serializer.data)

class VendaPorProdutoAPIView(APIView):

    @require_token
    def get(self, request):
        dados = VendaPorProdutoModel.objects.all()
        serializer = VendaPorProdutoSerializer(dados, many=True)
        return Response(serializer.data)