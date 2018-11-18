from observer import Observer

class CondicoesAtuais(Observer):
    def update(self, *args, **kwargs):
        print(f"Mudança nas condições recebida: {args} - {kwargs}")

class Estatisticas(Observer):
    def update(self, *args, **kwargs):
        print(f"Mudança nas estatísticas do tempo recebida: {args} - {kwargs}")

class Previsao(Observer):
    def update(self, *args, **kwargs):
        print(f"Mudança na previsão do tempo recebida: {args} - {kwargs}")