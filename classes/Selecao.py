import random

# Classe para realizar a seleção de indivíduos
class Selecao:
    @staticmethod
    def por_torneio(populacao, tamanho_torneio):
        """
        Implementa a seleção por torneio:
        - Seleciona aleatoriamente um grupo de indivíduos.
        - Retorna o indivíduo com o maior fitness do grupo.
        """
        competidores = random.sample(populacao.individuos, tamanho_torneio)
        return max(competidores, key=lambda x: x.fitness)