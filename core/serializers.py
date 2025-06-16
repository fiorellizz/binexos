from rest_framework import serializers
from core.infrastructure.models import ConferenciaModel, DetalhadoProdutoModel, EstoqueFisicoModel, EstoquePorLocalModel, MetaPorLocalModel, MetaPorVendedorModel, TradeInModel, ValoresAReceberModel, VendaPorProdutoModel, VendedorModel

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

class TradeInSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeInModel
        fields = '__all__'

class ValoresAReceberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValoresAReceberModel
        fields = '__all__'

class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendedorModel
        fields = '__all__'

class VendaPorProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendaPorProdutoModel
        fields = '__all__'