import random
import matplotlib.pyplot as plt
from Cromossomo import *
from Populacao import *
from Selecao import *
from Mutacao import *
from Crossover import *

# Classe principal do algoritmo genético
class AlgoritmoGenetico:
    def __init__(self, tamanho_populacao, geracoes, taxa_crossover, taxa_mutacao, tamanho_torneio, itens, capacidade_maxima):
        """
        Inicializa o algoritmo genético com:
        - tamanho_populacao: número de indivíduos na população
        - geracoes: número de iterações do algoritmo
        - taxa_crossover: probabilidade de realizar crossover
        - taxa_mutacao: probabilidade de realizar mutação em um gene
        - tamanho_torneio: número de competidores no torneio
        - itens: lista de itens disponíveis
        - capacidade_maxima: peso máximo permitido na mochila
        """
        self.tamanho_populacao = tamanho_populacao
        self.geracoes = geracoes
        self.taxa_crossover = taxa_crossover
        self.taxa_mutacao = taxa_mutacao
        self.tamanho_torneio = tamanho_torneio
        self.itens = itens
        self.capacidade_maxima = capacidade_maxima

    def executar(self):
        """
        Executa o algoritmo genético:
        - Inicializa a população.
        - Avalia e evolui a população ao longo de várias gerações.
        - Aplica seleção, crossover e mutação para gerar novas soluções.
        """
        populacao = Populacao(self.tamanho_populacao, self.itens, self.capacidade_maxima)
        populacao.avaliar()

        historico_fitness = []

        for geracao in range(self.geracoes):
            melhor = populacao.obter_melhor()
            historico_fitness.append(melhor.fitness)

            nova_populacao = []

            while len(nova_populacao) < self.tamanho_populacao:
                pai1 = Selecao.por_torneio(populacao, self.tamanho_torneio)
                pai2 = Selecao.por_torneio(populacao, self.tamanho_torneio)

                if random.random() < self.taxa_crossover:
                    filho1, filho2 = Crossover.cruzar(pai1, pai2)
                else:
                    filho1 = Cromossomo(self.itens, self.capacidade_maxima, pai1.genes[:])
                    filho2 = Cromossomo(self.itens, self.capacidade_maxima, pai2.genes[:])

                Mutacao.aplicar(filho1, self.taxa_mutacao)
                Mutacao.aplicar(filho2, self.taxa_mutacao)

                nova_populacao.extend([filho1, filho2])

            populacao.individuos = nova_populacao[:self.tamanho_populacao]
            populacao.avaliar()

        melhor = populacao.obter_melhor()

        # Exibir gráfico da evolução do fitness
        plt.plot(range(self.geracoes), historico_fitness)
        plt.title("Evolução do Fitness ao Longo das Gerações")
        plt.xlabel("Geração")
        plt.ylabel("Fitness")
        plt.grid()
        plt.show()

        return melhor