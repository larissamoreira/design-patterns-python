from tipo_pagamento import TipoPagamento

class Boleto(TipoPagamento):
    
    def pagar(self, valor):
        print(f'Boleto pago no valor de {valor}')
    