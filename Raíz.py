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
