# 1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def fibonacci(numero):
    fibonacci = [0, 1]
    for i in range(2, numero):
        numAtual = fibonacci[i - 1] + fibonacci[i - 2]
        fibonacci.append(numAtual)
    return fibonacci

n = int(input("Insira a quantidade de numeros da sequencia de fibonacci que você desenja: "))
print(fibonacci(n))

if n in fibonacci(n):
  print(f'{n} está presente na sequencia de fibonacci!')
else:
  print(f'{n} não está presente na sequencia de fibonacci!')