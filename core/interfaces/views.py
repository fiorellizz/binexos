from rest_framework.views import APIView
from rest_framework.response import Response
from core.decorators import require_token
from core.infrastructure.models import ConferenciaModel, DetalhadoProdutoModel, EstoqueFisicoModel
from core.serializers import ConferenciaSerializer, DetalhadoProdutoSerializer, EstoqueFisicoSerializer

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