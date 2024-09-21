numeroAtual = 0
anterior = 0
for i in range(8):
  if i <= 1:
    numeroAtual = i
  else:
    aux = numeroAtual
    numeroAtual = numeroAtual + anterior
    anterior = aux
  print(numeroAtual)

  # o proximo numero da sequencia sera 13