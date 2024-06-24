def adicionar_tarefa(tarefas, nome_tarefa):  
    
    #tarefa composta em 2 partes, com nome e se foi completa
    tarefa = {"nome": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} foi adicionada com sucesso")
    return

def ver_tarefas(tarefas):
    print("\nLista de tarefas:")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["completada"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice}. [{status}] {nome_tarefa}")

tarefas = []

while True:
    print("Bem vindo ao menu")
    print("1) Criar tarefa")
    print("2) Ver tarefas")
    print("3) Atualizar tarefa")
    print("4) Deletar tarefa")
    print("0) Encerrar programa")

    option = int(input("Digite sua opção: "))

    if option == 1:
        nome_tarefa = input("Digite o nome da tarefa: ")
        adicionar_tarefa(tarefas, nome_tarefa)

    elif option == 2:
        ver_tarefas()

    elif option == 0:
        break

print("programa finalizado")