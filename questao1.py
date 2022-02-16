def escada_asterisco(n):
  #verifica se o input é um numero
  if n.isnumeric()==True:
    #converte input em inteiro
    n = int(n)
    i = 0
    #loop para em cada iteração imprimir uma linha
    while i < n:
      #o texto que vai ser impresso, que é '*' repetido i+1 vezes
      texto = '*'*(i+1)
      #imprime o texto
      print(texto)
      i=i+1
  #se o input não for número, a função não retorna nada
  else:
    return None

#lê o valor de entrada
n = input()

#chama a função de impressão da pirâmide com o valor de entrada como parâmetro
escada_asterisco(n)

  
  
