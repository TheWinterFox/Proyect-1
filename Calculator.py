def add(a,b):
    result=a+b
    print(result)

def sub(a,b):
    result=a-b
    print(result)

def mul(a,b):
    result=a*b
    print(result)

def div(a,b):
    result=a/b
    print(result)

a=int(input("Ingrese el primer número: "))
b=int(input("Ingrese el segundo núemero: "))
op=input("Ingrese el operador: ")

if op=="+":
    add(a,b)
elif op=="-":
    sub(a,b)
elif op=="*":
    mul(a,b)
elif op=="/":
    div(a,b)
else:
    print("Operador inválido")
    
