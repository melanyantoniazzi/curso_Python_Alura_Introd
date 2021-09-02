#Primeiro programa: Implemente a lógica no seu jogo para mostrar se o chute do usuário foi maior ou menor do que o número secreto.
#Para tal:
#Crie para cada condição uma variável: acertou, maior e menor.
#Teste o chute e imprima uma mensagem.

import random

def jogar():

    print("*********************************")
    print("Bem Vindo ao Jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Dificil")

    nivel = int(input("Define o nível: "))

    if(nivel ==1):
        total_de_tentativas = 20
    elif(nivel ==2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    #rodada = 1 #so usamos essa variavel caso deseje rodar o codigo/linha WHILE

    #while (rodada <= total_de_tentativas): #while sera o looping de 3 tentativas: valor rodada (1) for menor igual a total de tentativas(3)
    #nesse caso podemos substituir a função WHILE para função FOR....IN
    for rodada in range(1, total_de_tentativas +1): #ou seja, a rodada tem valor inical 1 e vai até 3, isso se chama laço de repetição
        print("Tentativa", rodada, "de", total_de_tentativas) #outra forma de fazer essa linha do codigo print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    #imprima: Tentativa 1 de 3 o while dara o looping
        chute_str = input("Digite um número entre 1 e 100: ") #limitando os valores
        print("Você digitou: ", chute_str)
        chute = int(chute_str)  # esta convertendo uma string para inteiro

        if (chute <1 or chute >100):
            print("Você deve digitar um número entre 1 e 100!")
            continue #essa funcao de continue ira continuar a rodar o programa sem interromper

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!" .format(pontos))
            break #se acerta o numero o programa nao continua rodando para as tentantiva e sim finaliza o programa
        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute) #aqui ira subtrair e transformar num valor positivo com a funcao abs()
            pontos = pontos - pontos_perdidos

        rodada = rodada + 1

    print("Fim do jogo")