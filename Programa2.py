'''
##################################################################
#Codigo no Git Hub: https://github.com/thiagomoyses/AP1_Programa2#
#----------------------------------------------------------------#
#Created by: Thiago da Silva Moyses                              #
#RA: 1811515099                                                  #
#Course: electrical engineering                                  #
#GitHub: http://github.com/thiagomoyses                          #
#----------------------------------------------------------------#
#created by: Washington Luis Santos Bezerra                      #
#RA: 1811512370                                                  #
#Course: computer engineering                                    #
#GitHub: http://github.com/washington-bezerra                    #
#----------------------------------------------------------------#
#Last Update: 2020/04/12                                         #
##################################################################
'''
#bibliotecas
import csv

def opcoes():
    #Variavel Global
    global caminho, nome_csv
    print("#################### MENU ##########################")
    print("#                                                  #")
    print("# 1. Abrir arquivo de configuracao.                #")
    print("# 2. Adicionar servidor ao arquivo de configuracao.#")
    print("# 3. Visualizar arquivo de configuracao.           #")
    print("#                                                  #")
    print("####################################################")
    #Testando se a opçao escolhida é valida
    global opc_escolhida
    while True:
        try:
            opc_escolhida = int(input("\nEscolha uma das opções -> "))
            if (opc_escolhida != 1) and (opc_escolhida != 2) and (opc_escolhida != 3):
                print("Opçao invalida")
            else:
                break
        except:
            print("Opçao invalida")
    os.system('cls')
#funçao 01(conforme instruçoes)
def opcao1():
    global caminho, nome_csv
    caminho = input("Diga qual o caminho onde será salvo: ")
    nome_csv = input("Nome do arquivo (sem a extenção): ")

    if os.path.exists(f'{caminho}') == False:  # Verifica se existe a pasta Edital
        os.makedirs(f"{caminho}")  # Criando a pasta

    with open(f'{caminho}\{nome_csv}.csv', mode='w', newline='') as csv_file:
        fieldnames = ["Nome", "IP", "Hostname"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()


    csv_file.close()
    print('Seu arquivo será aberto')
    os.system(f'{caminho}/"{nome_csv}.csv"')  # Abre o arquivo

    os.system("cls")

    print('= Tudo certo, você será levado à 2 etapa. =')
    opcao2()
#funçao 02(conforme instruçoes)
def opcao2():

    desejo = "S"

    while desejo == "S":
        nome = input("Nome: ")
        IP = input("IP: ")
        hostname = input("Hostname: ")

        try:
            with open(f'{caminho}\{nome_csv}.csv', mode='a', newline='') as csv_file:
                fieldnames = ["Nome", "IP", "Hostname"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                #writer.writeheader()
                writer.writerow({"Nome": nome, "IP": IP, "Hostname": hostname})

        except NameError:
            os.system("cls")
            print("ERROR!!! Você pulou a etapa 1, vc será redirecionado à mesma, preencha corretamente e"
                  "depois volte à opção 2")
            opcao1()

        desejo = input("Deseja continuar (S/N)? ").upper()

    if desejo == "N":

        os.system("cls")

        print("Vc finalizou os inputs, será levado à etapa 3")
        opcao3()
#funçao 03(conforme instruçoes)
def opcao3():

    try:
        arquivo = open(f'{caminho}\{nome_csv}.csv')

        linhas = csv.reader(arquivo)

        for linha in linhas:
            print('{:15}|{:15}|{:15}'.format(linha[0], linha[1], linha[2]))

    except NameError:
        os.system("cls")
        print("ERROR!!! Você pulou a etapa 1, vc será redirecionado à mesma, preencha corretamente e"
              "depois volte à opção 2")
        opcao1()

opcoes()

if opc_escolhida == 1:
    opcao1()
elif opc_escolhida == 2:
    opcao2()
elif opc_escolhida == 3:
    opcao3()