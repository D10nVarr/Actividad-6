def operar_nums(cant_nums):
    nums_sum = 0
    count_pst=0
    count_ngt=0
    for i in range(cant_nums):
        num=float(input("Ingrese su numero: "))
        nums_sum+=num
        if num>0:
            count_pst+=1
        else:
            count_ngt+=1
    print(f"La suma los {cant_nums} números es {nums_sum}, el promedio es {nums_sum/cant_nums}, existen {count_pst} numeros por positivos y {count_ngt} negativos")

def calcular_a_triangulo(b,a):
    return (b*a)/2

def num_par(num):
    return num % 2 == 0

def promediar_notas(cant_nums):
    num_suma = 0
    for i in range(cant_nums):
        num=float(input(f"Ingrese la calificación : "))
        num_suma+=num
    print(f"El promedio de las notas es de {num_suma/ cant_nums}")

def calcular_max_min(cant_nums):
    num = float(input("Ingrese un numero: "))
    max_num=num
    min_num=num
    for i in range(cant_nums-1):
        num = float(input("Ingrese un numero: "))
        if num>max_num:
            max_num=num
        elif num<min_num:
            min_num=num
    print(f"El número mayor es {max_num} y el menor es {min_num}")

while True:
    print("\n---MENÚ DE OPERACIONES---")

    print("1. Suma, promediar y contar positivos y negativos")
    print("2. Cálcular el área de un triángulo")
    print("3. Verificar si un número es par o impar")
    print("4. Calcular el promedio de n calificaciones")
    print("5. Mayor y menor de n números")
    print("6. Salir")

    opcion=input("Seleccione una de las 6 opciones: ")

    match opcion:
        case "1":
            nums = int(input("Ingrese la cantidad de numeros: "))
            operar_nums(nums)

        case "2":
            base=float(input("Ingrese la base del triángulo: "))
            altura=float(input("Ingrese la altura del triángulo: "))
            print(f"El área del triángulo es {calcular_a_triangulo(base,altura)}")
        case "3":
            num_par_impar=int(input("Ingrese el número de desee verificar: "))
            if num_par(num_par_impar):
                print("El número es par")
            else:
                print("El número es impar")
        case "4":
            numeros=int(input("Ingrese la cantidad de calificaciones: "))
            promediar_notas(numeros)
        case "5":
            cant=int(input("Ingrese la cantidad de números que desea ingresar: "))
            calcular_max_min(cant)
        case "6":
            print("Saliendo...")
            break
        case _:
            print("Opción no válida")

