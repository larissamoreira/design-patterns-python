import datetime
from boleto import Boleto
from cartao_credito import CartaoCredito

class Reserva:
    def __init__(self, cliente, data_entrada, data_saida, quarto):
        self.cliente = cliente
        self.data_entrada = data_entrada
        self.data_saida = data_saida
        self.quarto = quarto
        self.quarto.reservar()
        self.modo_pagamento = Boleto()

    def get_data_entrada(self):
        return self.data_entrada.strftime("%x")

    def get_data_saida(self):
        return self.data_saida.strftime("%x")
    
    def realizar_pagamento(self, valor):
        self.modo_pagamento.pagar(valor)

    def modo_pagamento(self, novo_modo):
        self.modo_pagamento = novo_modo

    def __str__(self):
        return f'Reserva: {self.cliente}, de {self.get_data_entrada()} até {self.get_data_saida()}, Quarto: {self.quarto}'