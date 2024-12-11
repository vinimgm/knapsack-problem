import random

# Classe para realizar a mutação
class Mutacao:
    @staticmethod
    def aplicar(individuo, taxa_mutacao=0.1):
        """
        Aplica mutação em um indivíduo:
        - Para cada gene, há uma chance (taxa_mutacao) de inverter seu valor (0 ↔ 1).
        """
        for i in range(len(individuo.genes)):
            if random.random() < taxa_mutacao:
                individuo.genes[i] = 1 - individuo.genes[i]