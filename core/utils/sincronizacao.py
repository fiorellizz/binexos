def limpar_modelos(modelos: list):
    for modelo in modelos:
        nome = modelo.__name__
        try:
            modelo.objects.all().delete()
            print(f"🧹 {nome} limpo com sucesso.")
        except Exception as e:
            print(f"❌ Erro ao limpar {nome}: {e}")