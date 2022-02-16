#função para calcular quantos anagramas a palavra de entrada tem
def anagramas(palavra):
  #lista de todas as letras na palavra de entrada
  lista_letras=[]
  #lista de todas as palavras possíveis a partir da palavra de entrada
  words=[]
  anagramas=[]

  for char in palavra:
    #inserindo letras na lista de letras
    lista_letras.append(char)
    #inserindo letras como palavras de 1 caracter na lista de palavras possíveis
    words.append(char)

  
  i=0
  #completando a lista de palavras possíveis com as palavras com mais de um caracter
  while i<len(palavra):
    j=i+1
    while j<len(palavra):
      words.append(palavra[i:j+1])
      j=j+1
    i=i+1
  
  #variavel para armazenar nro de anagramas
  nro_anagramas=0
  i=0
  
  while i<len(words):
    j=i+1
    while j<len(words):
      #se a composição de letras de uma palavra é igual a de outra, o numero de anagramas aumenta 1
      if sorted(words[i])==sorted(words[j]):
        nro_anagramas=nro_anagramas+1
      j=j+1
    i=i+1


  #imprime número de anagramas
  print(nro_anagramas)

palavra_anagrama = input()
anagramas(palavra_anagrama)
