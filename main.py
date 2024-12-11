import matplotlib.pyplot as plt
from prettytable import PrettyTable
from .classes.AlgoritmoGenetico import *

# Função principal
if __name__ == "__main__":
    # Defina os itens e capacidade máxima diretamente no main
    itens = [
        [150.00, 3.5], [100.00, 2.0], [50.00, 0.5], [80.00, 1.0],
        [30.00, 0.2], [20.00, 0.5], [15.00, 0.1], [20.00, 0.2],
        [10.00, 0.1], [25.00, 0.3], [15.00, 1.8], [50.00, 0.5],
        [50.00, 3.0], [70.00, 1.5], [30.00, 1.2], [20.00, 0.5],
        [80.00, 1.5], [120.00, 2.0], [20.00, 0.5], [30.00, 0.5]
    ]
    capacidade_maxima = 15.0

    # Configurações do algoritmo
    tamanho_populacao = 20
    geracoes = 100
    taxa_crossover = 0.8
    taxa_mutacao = 0.1
    tamanho_torneio = 3

    # Executar o algoritmo genético
    ag = AlgoritmoGenetico(tamanho_populacao, geracoes, taxa_crossover, taxa_mutacao, tamanho_torneio, itens, capacidade_maxima)
    melhor_solucao = ag.executar()

    # Exibir a melhor solução em formato de tabela
    tabela = PrettyTable()
    tabela.field_names = ["Item", "Valor", "Peso", "Selecionado"]
    
    valor_total = 0
    peso_total = 0

    for (item, gene) in zip(itens, melhor_solucao.genes):
        selecionado = "Sim" if gene == 1 else "Não"
        tabela.add_row([f"Item {itens.index(item) + 1}", f"R$ {item[0]:.2f}", f"{item[1]:.2f} kg", selecionado])
        if gene == 1:
            valor_total += item[0]
            peso_total += item[1]

    print(tabela)
    print(f"\nValor total: R$ {valor_total:.2f}")
    print(f"Peso total: {peso_total:.2f} kg")
