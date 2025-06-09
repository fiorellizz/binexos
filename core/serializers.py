from rest_framework import serializers
from core.infrastructure.models import ConferenciaModel, DetalhadoProdutoModel, EstoqueFisicoModel

class ConferenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConferenciaModel
        fields = '__all__'

class DetalhadoProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalhadoProdutoModel
        fields = '__all__'

class EstoqueFisicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstoqueFisicoModel
        fields = '__all__'