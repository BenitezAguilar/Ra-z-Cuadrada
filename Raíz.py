from math import sqrt

def calcular_raices(a, b, c):
    print("\n---Uso de la Fórmula General---")
    a=float(input("Ingrese el valor de a: "))
    b=float(input("Ingrese el valor de b: "))
    c=float(input("Ingrese el valor de c: "))
    d=(b**2)-(4*a*c)
    if d<0:
        print("\nNo existe solución en los números reales")
        return None
    else: 
        r=sqrt(d)
        x1=(-b+r)/(2*a)
        x2=(-b-r)/(2*a)
        print("\nEl valor de x1 es: ", x1)
        print("El valor de x2 es: ", x2)

while True:
    print("--Calculadora de Raíces Cuadradas--")
    print("1. Calcular raíces")
    print("2. Salir")
    opcion = input("\nSeleccione una opción: ")
    if opcion == "1":
        calcular_raices(0, 0, 0)
    elif opcion == "2":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")