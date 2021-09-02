#Curso Alura

#1- Imprima a seguinte data 15/10/2015

dia=15
mes=10
ano=2015

print(dia,mes,ano, sep="/") #sep indica espaço vazio e estou pedindo para colocar a / no espaco vazio

type(pais) #para saber qual é o tipo da variavel: se é uma str , int, float

#2 - Declare a seguinte string: "Em 2017 o Carnaval acontece em fevereiro do dia 24 até o dia 28"

dia_ini = 24
dia_fim = 28
mes = "fevereiro"
ano = 2017

print ("Em {} o Carnaval acontece em {} do dia {} até o dia {}".format(ano,mes,dia_ini,dia_fim))

# função .format

print("Tentativa {} de {}".format(1, 3)) # irá imprimir Tentativa {1} de {3}"

print("Tentativa {1} de {0}".format(1, 3)) #irá imprimir de forma invertida
Tentativa 3 de 1

print("R$ {}".format(1.59)) #irá imprimir o valor em reais.
R$ 1.59
#mas podemos ter varios tamanhos e casas decimais por exemplo

print("R$ {:f}".format(1.59)) #impressão padrão float (f)
R$ 1.590000

print("R$ {:.2f}".format(1.59)) #apos o ponto tenha apenas 2 numeros
R$ 1.59

print("R$ {:07d}".format(4)) #para numeros inteiros usa (d), estou dizendo que antes do num 4 quero 7 casas de 0
R$ 0000004

#3 Digamos que queira exibir a seguinte mensagem: "Ola Sr. Leonardo Cordeiro", como ele pode formatar a string para obter o resultado desejado?

print("Ola Sr.{1} {0}".format("Cordeiro","Leonardo"))


#função .count()
#Um jeito fácil de contar o número de ocorrências de um determinado elemento em uma lista é a função .count() das listas, veja:
valores = [ 0, 0, 0, 1, 2, 3, 4]
print(valores.count(0))

#O código acima nos retorna 3, pois em nossa lista encontramos 3 vezes o número zero nela.
#Utilizando a função .count() podemos por exemplo, detectar quantas letras ainda faltam para o nosso usuário preencher:

letras_acertadas = ['_','_','_','_','_','_']
letras_faltando = str(letras_acertadas.count('_'))
print( 'Ainda faltam acertar {} letras'.format(letras_faltando))

#função .index()
#Uma outra função que pode ser bastante útil é a função .index(), que nos retorna o índice da primeira ocorrência de um determinado elemento em uma lista, veja:
frutas = ['Banana', 'Morango', 'Maçã', 'Uva', 'Maçã', 'Uva']
print(frutas.index('Uva'))

#O código acima nos retorna 3, pois é o índice da primeira ocorrência do elemento 'Uva' na lista frutas (lembre-se nas listas começamos a contar do índice 0).
#Só tome cuidado quando utilizar a função .index(), pois a mesma pode retornar um erro caso você tente buscar pelo índice de um elemento que não existe. Veja o caso abaixo:
frutas = ['Banana', 'Morango', 'Maçã', 'Uva']
print(frutas.index('Melancia'))

#Ao tentar buscar pela fruta 'Melancia', obteremos o erro "ValueError: 'Melancia' is not in list" no console, já que é impossível buscar o índice de algo que não está na lista.
# Por isto, é sempre uma boa prática verificar se o elemento está na lista com o operador in antes de obter o seu índice. Um código ideal que faz uso da função index() é demonstrado abaixo:
frutas = ['Banana', 'Morango', 'Maçã', 'Uva']

fruta_buscada = 'Melancia'
if fruta_buscada in frutas:
    print(frutas.index(fruta_buscada))
else:
    print('Desculpe, a {} não está na lista frutas'.format( fruta_buscada))

#Assim temos certeza que a fruta_buscada está dentro da lista antes de perguntarmos o seu índice, evitando assim de receber um erro no console.

#List Comprehension é um dos recursos mais legais da linguagem Python :)
#O recurso List Comprehension também permite utilizar condições para o preenchimento da lista. Considere o objetivo de inicializar uma lista com os números pares a partir de uma lista de números inteiros qualquer,
# por exemplo, os números 1,3,4,5,7,8,9. Para descobrir se um número é par, usamos a condição numero%2 == 0, que verifica se o resto de uma divisão por 2 é zero. O código abaixo usa um loop para inicializar a lista de pares.
inteiros = [1,3,4,5,7,8,9]
pares = [x for x in inteiros if x % 2 == 0]
