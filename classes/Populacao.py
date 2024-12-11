from Cromossomo import *

# Classe que representa a população de cromossomos
class Populacao:
    def __init__(self, tamanho, itens, capacidade_maxima):
        """
        Inicializa a população com:
        - tamanho: número de indivíduos
        - itens: lista de itens disponíveis
        - capacidade_maxima: peso máximo permitido na mochila
        """
        self.individuos = [
            Cromossomo(itens, capacidade_maxima) for _ in range(tamanho)
        ]

    def avaliar(self):
        """
        Avalia cada indivíduo da população, calculando seu fitness.
        """
        for individuo in self.individuos:
            individuo.calcular_fitness()

    def obter_melhor(self):
        """
        Retorna o melhor indivíduo da população (com o maior fitness).
        """
        return max(self.individuos, key=lambda x: x.fitness)