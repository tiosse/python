class jogo_gourmet:

    def __init__(self, caracteristica, resposta_sim, resposta_nao):
        self._caracteristica = caracteristica
        self._resposta_sim = resposta_sim
        self._resposta_nao = resposta_nao

    @property
    def caracteristica(self):
        return self._caracteristica

    @caracteristica.setter
    def caracteristica(self, caracteristica):
        self._caracteristica = caracteristica

    @property
    def resposta_sim(self):
        return self._resposta_sim

    @resposta_sim.setter
    def resposta_sim(self, resposta_sim):
        self._resposta_sim = resposta_sim

    @property
    def resposta_nao(self):
        return self._resposta_nao

    @resposta_nao.setter
    def resposta_nao(self, resposta_nao):
        self._resposta_nao = resposta_nao


class novo_prato(jogo_gourmet):

    def __init__(self, caracteristica, resposta_sim, resposta_nao, prato):
        super().__init__(caracteristica, resposta_sim, resposta_nao)
        self._prato = prato

    @property
    def prato(self):
        return self._prato

    @prato.setter
    def prato(self, prato):
        self._prato = prato

    def caracteristica_prato(self):
        print(f'O prato que vc pensou é {self.caracteristica} ?')
        retorno = input('Digite S ou N: ')
        retorno_sim = True if retorno.strip().lower() == "s" else False
        prato = self.resposta_sim if retorno_sim else self.resposta_nao
        prato_resposta = prato.resposta_sim if retorno_sim else prato.resposta_nao

        if prato_resposta is None:
            prato.adivinha_prato()
        else:
            prato.caracteristica_prato()

    def adivinha_prato(self):
        print(f'o prato que vc pensou é {self.prato} ?')
        retorno = input('Digite S ou N: ')
        retorno_sim = True if retorno.strip().lower() == "s" else False

        if retorno_sim:
            print('acertei denovo!!!')
        else:
            novo_prato_digitado = input('Qual prato você pensou?')
            self.caracteristica = input(f'{novo_prato_digitado} é _______ mas {self.prato} não.')
            self.resposta_sim = novo_prato(None, None, None, novo_prato_digitado)
            self.resposta_nao = novo_prato(None, None, None, self.prato)

        inicia_recomeca_jogo()


def inicia_recomeca_jogo():
    print('Pense em um prato que goste')
    inicio.caracteristica_prato()


respondeu_sim = novo_prato(None, None, None, 'lasanha')
respondeu_nao = novo_prato(None, None, None, 'bolo de chocolate')

inicio = novo_prato('massa', respondeu_sim, respondeu_nao, None)

inicia_recomeca_jogo()
