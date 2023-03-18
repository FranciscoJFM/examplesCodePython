#Hola mundo en python
print('Hello,MattEvan!')

#Suma de dos numeros en python
num1 = float(input("introduce el primer número:"))
num2 =  float(input("introduce el segundo número"))
suma = num1 + num2
print("la sema de",num1,"y",num2,"es", suma)

#Convertir millas a kilometros
millas = float(input("Introduce la cantidad en millas"))
kilometros = millas * 1.60934
print(millas,"Millas son equivalentes a",kilometros,"kilometros")

#Programa que calcula el area de un triangulo
base  = float(input("intoduce la base  del rectangulo: "))
altura = float(input("introduce la altura del rectangulo"))
area = base * altura
print("el área del rectangulo es:", area)

#Contador de vocales
frase = input("introduce una frase:")
frase =  frase.lower()
contador_vocales = 0
for letra in frase:
    if letra in "aeiou":
        contador_vocales += 1
print("La frase introducida contiene" , contador_vocales,"vocales.")

#cifrado Cesar
mensaje = input("Introduce el mensaje a cifrar: ")
desplazamiento = int(input("Introduce el desplazamiento"))
alfabeto ="abcdefghijklmnopqrstuvwxyz"
alfabeto_dezplazado = alfabeto[desplazamiento:]+alfabeto[:desplazamiento]
diccionario_cifrado = dict(zip(alfabeto,alfabeto_dezplazado))
mensaje_cifrado =[diccionario_cifrado.get(letra,letra) for letra in mensaje]
mensaje_cifrado = "".join(mensaje_cifrado)
print("Mensaje cifrado:", mensaje_cifrado)



#Programa que muestre los primeros numeros pares hasta el 10  
contador = 0
while contador < 10:
    contador +=1
    if contador % 2 == 0:
        print("Los 10 primeros numeros par son:",contador)
        