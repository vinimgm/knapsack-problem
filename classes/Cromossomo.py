import random

# Classe que representa um indivíduo da população
class Cromossomo:
    def __init__(self, itens, capacidade_maxima, genes=None):
        """
        Inicializa o cromossomo com:
        - itens: lista de itens disponíveis (cada item é [valor, peso])
        - capacidade_maxima: peso máximo permitido na mochila
        - genes: lista binária que indica a seleção (1 para incluir, 0 para não incluir)
        """
        self.itens = itens
        self.capacidade_maxima = capacidade_maxima
        self.genes = genes if genes else self._gerar_aleatorio()
        self.fitness = 0  # Avaliação da qualidade da solução

    def _gerar_aleatorio(self):
        """
        Gera um conjunto de genes aleatórios (seleções de itens).
        Cada gene representa a escolha de incluir ou não um item na mochila.
        """
        return [random.choice([0, 1]) for _ in range(len(self.itens))]

    def calcular_fitness(self):
        """
        Calcula o fitness do cromossomo:
        - Soma os valores dos itens selecionados (genes = 1).
        - Penaliza soluções que excedem o peso máximo, atribuindo fitness = 0.
        """
        valor_total = 0
        peso_total = 0
        for gene, item in zip(self.genes, self.itens):
            if gene == 1:
                valor_total += item[0]
                peso_total += item[1]
        # Se o peso total exceder a capacidade máxima, fitness é 0
        self.fitness = 0 if peso_total > self.capacidade_maxima else valor_total