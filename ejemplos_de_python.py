# 1. Entrada y salida de datos
nombre = input("¿Cómo te llamas? ")
print("Hola,", nombre)

# 2. Variables y tipos de datos
nombre = "Alan"
edad = 20
altura = 1.75
es_estudiante = True

print(nombre)
print(edad)
print(altura)
print(es_estudiante)

# 8.Listas
frutas = ["manzana", "banana", "naranja"]

print(frutas[0])  # primer elemento

for fruta in frutas:
    print(fruta)

# 9.Diccionarios
persona = {
    "nombre": "Alan",
    "edad": 20
}

print(persona["nombre"])
print(persona["edad"])

# 4. Condicionales
edad = 18

if edad >= 18:
    print("Sos mayor de edad")
else:
    print("Sos menor de edad")
    
# 10.Operadores logicos
edad = 20
tiene_cedula = True

# AND → ambas condiciones deben cumplirse
if edad >= 18 and tiene_cedula:
    print("Puede pasar")

# OR → con una sola condición basta
if edad < 18 or tiene_cedula:
    print("Cumple al menos una condición")

# NOT → invierte el valor
if not tiene_cedula:
    print("No tiene cédula")

# 5. Bucles (for)
for i in range(5):
    print("Número:", i)

# 6. Bucles (while)
contador = 0

while contador < 5:
    print("Contador:", contador)
    contador += 1

# 7.Funciones
def saludar(nombre):
    print("Hola,", nombre)

saludar("Alan")
