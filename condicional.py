print("Bem vindo ao menu")
print("1) Criar lista")
print("2) Deletar lista")
print("9) Retornar ao menu")
print("0) Encerrar programa")

option = int(input())
list_names = []

print("option value:", option)
print("names on list:", list_names)

while option !=0:
    if option == 1:
        print("Qual o nome da lista?")
        list_names = input()
        for names in list_names:
            print(names)
    elif option == 2:
        print("Qual o nome da lista que deseja deletar?")
        del_names = input()
    elif option == 0:
        break