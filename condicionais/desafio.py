numero1 = int(input("informe um numero --> "))
numero2 = int(input("informe um numero --> "))
operacao = input("informe uma operacao --> ")
if operacao == "+": 
   print("a soma dos dois numeros é " ,numero1 + numero2,)
elif operacao == "-":
   print("a subtraçao dos dois numeros é " ,numero1 - numero2,)
elif operacao == "*":
   print("a multiplicaçao dos dois numeros é " ,numero1 * numero2,)
elif operacao == "/":
   print("a divisao dos dois numeros é " ,numero1 / numero2,)   
else:
   print("INVALIDO!!!") 