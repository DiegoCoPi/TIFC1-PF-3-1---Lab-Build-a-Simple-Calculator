#Pedir numeros de entrada

num1 = int(input("Ingresa el numero 1"))
num2 = int(input("Ingresa el numero 2"))

print(num1+num2)

#Calculadora asignar numeros
operation=int(input("Elija un numero para la operación:\n" 
"1. Suma \n 2.Resta \n 3.Multiplicación \n 4. División"))

dig1=int(input("Ingrese el primner digito"))
dig2=int(input("Ingrese el segundo digito"))

def operacion():
    if(operation == 1):
        result    =   dig1   +  dig2
        print(f"La suma de {dig1} + {dig2} = {result}")
    elif(operation == 2):
        result    =   dig1 -  dig2
        print(f"La resta de {dig1} - {dig2} = {result}")
    elif(operation == 3):
        result   =   dig1    *   dig2
        print(f"El producto de {dig1} X {dig2} = {result}")
    elif(operation == 4):
        result  =   dig1    /   dig2
        print(f"La división de {dig1} / {dig2} = {result}")
    else:
       print("Numero no valido")
