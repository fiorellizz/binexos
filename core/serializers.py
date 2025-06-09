from rest_framework import serializers
from core.infrastructure.models import ConferenciaModel, DetalhadoProdutoModel, EstoqueFisicoModel, EstoquePorLocalModel, MetaPorLocalModel, MetaPorVendedorModel

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

class EstoquePorLocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstoquePorLocalModel
        fields = '__all__'

class MetaPorLocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaPorLocalModel
        fields = '__all__'

class MetaPorVendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaPorVendedorModel
        fields = '__all__'