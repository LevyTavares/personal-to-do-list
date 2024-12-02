# Licensed For Hyl1ght, Inc.
# Isaías Levi Tavaresd da Silva
# 37023010

# Sistema de Gerenciamento de Tarefas

# Listas para armazenar as tarefas e seus estados
tarefas = []  # Lista com os nomes das tarefas
estados = []  # Lista com os estados correspondentes (Pendente ou Concluída)

def adicionar_tarefa(nome):
    """Adiciona uma nova tarefa como pendente."""
    tarefas.append(nome)
    estados.append("Pendente")
    print(f"Tarefa '{nome}' adicionada com sucesso!")

def marcar_concluida(nome):
    """Marca uma tarefa como concluída, se existir."""
    if nome in tarefas:
        indice = tarefas.index(nome)
        estados[indice] = "Concluída"
        print(f"Tarefa '{nome}' marcada como concluída!")
    else:
        print(f"Tarefa '{nome}' não encontrada.")

def remover_tarefa(nome):
    """Remove uma tarefa, se ela existir."""
    if nome in tarefas:
        indice = tarefas.index(nome)
        tarefas.pop(indice)
        estados.pop(indice)
        print(f"Tarefa '{nome}' removida com sucesso!")
    else:
        print(f"Tarefa '{nome}' não encontrada.")

def listar_tarefas():
    """Exibe todas as tarefas e seus estados."""
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("Lista de tarefas:")
        for i in range(len(tarefas)):
            print(f"{i + 1}. {tarefas[i]} - {estados[i]}")

def listar_por_estado(estado):
    """Lista tarefas filtradas por estado (pendente ou concluída)."""
    print(f"Tarefas {estado.lower()}s:")
    for i in range(len(tarefas)):
        if estados[i].lower() == estado.lower():
            print(f"{tarefas[i]}")
    if estado.lower() not in [e.lower() for e in estados]:
        print(f"Nenhuma tarefa {estado.lower()} encontrada.")

def pesquisar_tarefa(nome):
    """Pesquisa uma tarefa pelo nome."""
    if nome in tarefas:
        indice = tarefas.index(nome)
        print(f"Tarefa encontrada: {tarefas[indice]} - {estados[indice]}")
    else:
        print(f"Tarefa '{nome}' não encontrada.")

# Exemplo de interação com o usuário
while True:
    print("\nSistema de Gerenciamento de Tarefas")
    print("1. Adicionar tarefa")
    print("2. Marcar tarefa como concluída")
    print("3. Remover tarefa")
    print("4. Listar todas as tarefas")
    print("5. Listar tarefas pendentes")
    print("6. Listar tarefas concluídas")
    print("7. Pesquisar tarefa")
    print("8. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome da tarefa: ")
        adicionar_tarefa(nome)
    elif opcao == "2":
        nome = input("Digite o nome da tarefa a marcar como concluída: ")
        marcar_concluida(nome)
    elif opcao == "3":
        nome = input("Digite o nome da tarefa a remover: ")
        remover_tarefa(nome)
    elif opcao == "4":
        listar_tarefas()
    elif opcao == "5":
        listar_por_estado("Pendente")
    elif opcao == "6":
        listar_por_estado("Concluída")
    elif opcao == "7":
        nome = input("Digite o nome da tarefa para pesquisar: ")
        pesquisar_tarefa(nome)
    elif opcao == "8":
        print("Saindo do sistema. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
