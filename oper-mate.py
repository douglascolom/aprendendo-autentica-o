n1 = int(input("Informe o primeiro numero: "))

n2 = int(input("Informe o segundo número: "))

op = int(input("""
           Qual operação deseja realizar?
           1 = Soma
           2 = Subtração
           3 = Multiplicão
           4 = Divisão
           """))

if op == 1:
    soma = n1 + n2
    print(soma)
elif op == 2:
    subtrair = n1 - n2
    print(subtrair)
elif op == 3:
    mult = n1 * n2
    print(mult)
elif op == 4:
    div = n1 / n2
    print(div)
else:
    print("Operação invalida")