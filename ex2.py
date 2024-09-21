#2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

def verificar_a(string):
  contador_letra_a = 0
  for i in range(len(string)):

    if 'a' in string.lower()[i]:
      contador_letra_a += 1
  return contador_letra_a;

frase = input('Insira uma frase: ')
contador = verificar_a(frase)

if contador != 0:
  print(f'A letra a apareceu {contador} vezes')
else:
  print('A letra a não apareceu na string!')

