import cadastros
from hotel import Hotel
from reserva import Reserva
from datetime import datetime
from boleto import Boleto
from cartao_credito import CartaoCredito

opcoes = {}
def busca(cidade, tipo, preço=None, r=None, d=None, p=None):
    print(r, d, p)
    x = 0
    if r:
        Hotel.instances.sort(key=lambda h: float(h.recomendacao), reverse=True)
    if d:
        Hotel.instances.sort(key=lambda h: float(h.dist_centro), reverse=False)
    for hotel in Hotel.instances:
        if hotel.cidade == cidade:
            quartos = hotel.get_quartos(tipo, preço)
            quartos.sort(key=lambda q: float(q.preço), reverse=False)
            for quarto in quartos:
                x += 1
                print(f'[id {x}] {hotel.nome} - R${quarto.preço} - {hotel.recomendacao}')
                opcoes[x] = quarto
    

# Realizando a busca.
resultado = busca(cidade='João Pessoa', tipo='Single', preço=100.0, r=None, d=None, p=True)

# Selecionando quarto para reserva
id_quarto = int(input('Digite o id do quarto que deseja reservar: '))
quarto = opcoes[id_quarto]

# Criando a reserva
reserva1 = Reserva('cliente1', datetime(2020, 5, 17), datetime(2020, 5, 27), quarto)

# Selecionar modo de pagamento
modos = {1: Boleto, 2: CartaoCredito}
modo = int(input('1: Boleto\n2: Cartão de crédito\nSelecione o modo de pagamento: '))
reserva1.modo_pagamento = modos[modo]()

# Realizando pagamento e retornando reserva
reserva1.realizar_pagamento(quarto.preço)
print(reserva1)