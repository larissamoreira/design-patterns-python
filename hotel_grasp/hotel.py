class Hotel:
    def __init__(self, nome, cidade, endereço, dist_centro, recomendacao):
        self.nome = nome
        self.cidade = cidade
        self.endereço = endereço
        self.dist_centro = dist_centro
        self.recomendacao = recomendacao
        self.quartos = []
    
    def add_quarto(self, Quarto):
        self.quartos.append(Quarto)

    # Retorna os quartos disponiveis do hotel, é opcional filtrar por tipo e preço do quarto.
    def get_quartos(self, tipo=None, preço=None):
        r = []
        for quarto in self.quartos:
            if quarto.disponivel:
                if tipo:
                    if quarto.tipo == tipo:
                        if preço:
                            if quarto.preço <= preço:
                                r.append(quarto)
                        else:
                            r.append(quarto)
                else:
                    r.append(quarto)          
        return r
