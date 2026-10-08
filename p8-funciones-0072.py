# catherine eileen huerta rascon NC = 0072
print("+*-+-++-+-+-+-+EJEMPLO 1-+-+-+-++-+-+-+-+")
def saludar():
    print("¡Hola, mundo!")

# Llamar a la función
saludar()
# Salida: ¡Hola, mundo!

print("+*-+-++-+-+-+-+EJEMPLO 2-+-+-+-++-+-+-+-+")
def sumar_todos(*numeros):
    """Suma cualquier cantidad de números"""
    total = 0
    for num in numeros:
        total += num
    return total

print(sumar_todos(1, 2, 3))           # 6
print(sumar_todos(10, 20, 30, 40))    # 100
print(sumar_todos(5))   

print("+*-+-++-+-+-+-+EJEMPLO 3-+-+-+-++-+-+-+-+")
def calcular_area_rectangulo(ancho, alto):
    """Calcula el área de un rectángulo"""
    area = ancho * alto
    return area

# Llamar a la función
resultado = calcular_area_rectangulo(5, 10)
print(resultado)  # Salida: 50

# El orden importa
resultado2 = calcular_area_rectangulo(10, 5)
print(resultado2)  # Salida: 50 (mismo resultado en este caso)

print("+*-+-++-+-+-+-+EJEMPLO 4-+-+-+-++-+-+-+-+")
def saludar(nombre, saludo="Hola"):
    """Saluda a una persona con un saludo personalizable"""
    return f"{saludo}, {nombre}!"

print(saludar("María"))  # Hola, María!
print(saludar("Pedro", "Buenos días"))  # Buenos días, Pedro!
print(saludar("Ana", saludo="Qué tal"))  # Qué tal, Ana!

print("+*-+-++-+-+-+-+EJEMPLO 5-+-+-+-++-+-+-+-+")
def crear_usuario(nombre, edad, ciudad):
    return f"{nombre}, {edad} años, de {ciudad}"

# Usando parámetros posicionales
usuario1 = crear_usuario("Ana", 25, "Madrid")

# Usando parámetros con nombre (más claro)
usuario2 = crear_usuario(nombre="Carlos", edad=30, ciudad="Barcelona")

# Puedes cambiar el orden si usas nombres
usuario3 = crear_usuario(ciudad="Valencia", nombre="Laura", edad=28)

print(usuario1)  # Ana, 25 años, de Madrid
print(usuario2)  # Carlos, 30 años, de Barcelona
print(usuario3)  # Laura, 28 años, de Valencia

print("+*-+-++-+-+-+-+EJEMPLO 6-+-+-+-++-+-+-+-+")
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(resultado)  # 8

print("catherine eileen huerta rascon NC = 0072")