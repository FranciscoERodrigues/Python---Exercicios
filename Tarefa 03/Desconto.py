Valorinteiro = float(input('Digite o valor do produto: '))
Desconto = int(input('Digite o desconto: '))

Calculo = (Valorinteiro/100)*Desconto

valordescontado = Valorinteiro - Calculo


print(" O valor do produto inteiro é ", Valorinteiro, "o desconto é de", Calculo, "com o desconto", valordescontado )
