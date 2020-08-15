from fn_CalculoDeVotos import fn_CalculaSomatorioVotos,fn_CalculoPorcentagem

def fn_Entrada():
  print("Digite somente a quantidade de votos,nao deixe em branco!!")
  int_nulos = int(input("Digite a quantidade de votos nulos: "))
  int_brancos = int(input("Digite a quantidade de votos brancos: "))
  int_validos = int(input("Digite a quantidade de votos validos: "))
  return [int_nulos,int_brancos,int_validos]

def fn_Resultados(vet_perc_votos):
  print(f'Votos Nulos   : {vet_perc_votos[0]:.2f}%')
  print(f'Votos Brancos : {vet_perc_votos[1]:.2f}%')
  print(f'Votos Validos : {vet_perc_votos[2]:.2f}%')

if __name__ =='__main__':
  vet_votos = fn_Entrada()
  int_soma_votos = fn_CalculaSomatorioVotos(vet_votos)
  vet_porc_votos = fn_CalculoPorcentagem(vet_votos, int_soma_votos)
  fn_Resultados(vet_porc_votos)