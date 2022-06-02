print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
r1 = float(input('Digite o comprimento da reta 1: '))
r2 = float(input('Digite o comprimento da reta 2: '))
r3 = float(input('Digite o comprimento da reta 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Com estes valores você consegue formar um Triângulo!')
else:
    print('Não é posssível criar um Triângulo com estes valores digitados, tente de novo.')
