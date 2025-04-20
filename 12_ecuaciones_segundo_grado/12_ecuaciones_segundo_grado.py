n = int(input("numero de ecuaciones a resolver:"))
for i in range(1,n+ 1): 
    a = int(input("Ingresa a: "))
    b = int(input("ingresa b: "))
    c = int(input("ingresa c: "))

    x_1 = (-b + (b**2 - 4*a*c)**0.5) / (2 * a)
    x_2 = (-b - (b**2 - 4*a*c)**0.5) / (2 * a)

    print("X_1 =", x_1, "X_2 =", x_2)