numero1 = int(input("informe o primeiro numero --> "))
numero2 = int(input("informe o segundo numero --> "))
numero3 = int(input("informe o terceiro numero --> "))
if numero1 > numero2 and numero1 > numero3:
    print("o numero",numero1, "é o maior")
elif numero2 > numero1 and numero2 > numero3:
    print("o numero",numero2,"é o maior")
elif numero1 == numero2 == numero3:
    print("os numeros sao iguais")
else:
    print("o numero",numero3,"é o maior!")