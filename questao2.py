#função para verificar a senha
def senha_segura(senha):
  #salva quantos caracteres a senha de entrada tem
  length = len(senha)
  #se a senha de entrada tiver 6 ou mais caracteres, imprime 0 (caracteres faltantes)
  if length >=6:
    print(0)
  #se a senha não tiver 6 ou mais caracteres
  else:
    #quantos caracteres faltam para a senha ter 6 caracteres
    diferenca = 6-length
    #imprime quantos caracteres faltam
    print(diferenca)

#lê a senha de entrada
senha = input()

#imprime quantos caracteres faltam
senha_segura(senha)
