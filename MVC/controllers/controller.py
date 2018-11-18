from models.hotel import Hotel
from models.reserva import Reserva
from views.view import View
from models.boleto import Boleto
from models.cartao_credito import CartaoCredito

class ControllerHotel:

    def __init__(self):
        self.view = View()

    def start(self):
        dados = self.view.start()
        quartos = self.busca(dados['cidade'], dados['tipo'], dados['preço'])
        quarto = self.view.mostrar_quartos(quartos)
        self.reservar(quarto)

    def busca(self, cidade, tipo, preço=None, r=None, d=None, p=None):
        result = []
        if r:
            Hotel.instances.sort(key=lambda h: float(h.recomendacao), reverse=True)
        if d:
            Hotel.instances.sort(key=lambda h: float(h.dist_centro), reverse=False)
        for hotel in Hotel.instances:
            if hotel.cidade == cidade:
                quartos = hotel.get_quartos(tipo, preço)
                quartos.sort(key=lambda q: float(q.preço), reverse=False)
                for quarto in quartos:
                    result.append(quarto)
        return result
    
    def reservar(self, quarto):
        modos = {1: Boleto, 2: CartaoCredito}
        dados = self.view.fazer_reserva()
        r = Reserva(dados['cliente'], dados['entrada'], dados['saida'], quarto)
        modo = dados['modo']
        r.modo_pagamento = modos[modo]()
        r.realizar_pagamento(quarto.preço)
        self.view.mostrar_reservas(Reserva.instances)
        