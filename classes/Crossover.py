import random
from Cromossomo import *

# Classe para realizar o crossover (recombinação genética)
class Crossover:
    @staticmethod
    def cruzar(pai1, pai2):
        """
        Realiza o crossover entre dois indivíduos (pais):
        - Seleciona um ponto de corte aleatório.
        - Combina os genes antes e depois do ponto de corte para gerar dois filhos.
        """
        ponto = random.randint(1, len(pai1.genes) - 1)
        filho1 = Cromossomo(pai1.itens, pai1.capacidade_maxima, pai1.genes[:ponto] + pai2.genes[ponto:])
        filho2 = Cromossomo(pai2.itens, pai2.capacidade_maxima, pai2.genes[:ponto] + pai1.genes[ponto:])
        return filho1, filho2