from observer import Observer

class JornalTempo(Observer):
    def update(self, *args, **kwargs):
        print(f"Jornal Tempo - Mudança no tempo recebida: {args} - {kwargs}")

class NoticiasTempo(Observer):
    def update(self, *args, **kwargs):
        print(f"Notícias Tempo - Mudança no tempo recebida: {args} - {kwargs}")