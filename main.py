def add(x,y):
  return x + y

def sub(x,y):
  return x - y

def mult(x,y):
  return x * y

def div(x,y):
  return x / y 

print(" selecione uma operação.")
print(" 1. adicão")
print("2.subtração")
print("3.multiplicação")
print("4. divisão")

escolha = input("escolha uma operação (1/2/3/4)")

if escolha in ('1','2','3','4'):
    n1  = float(input ("digite um numero: "))
    n2 = float(input("digite outro numero: "))

    if  escolha == '1': 
      print(add(n1,n2))  

    if  escolha == '2': 
     print(sub(n1,n2)) 

    if escolha =='3':
      print(mult(n1,n2))

    if escolha =='4':
     print(div(n1,n2))