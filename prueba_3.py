from funciones import *
menu = True
while menu:
    print("\n          Registro de ciudadados")
    print("\n1.Grabar\n2.Buscar\n3.Imprimir certificados\n4.Salir")
    opcion = validar_menu()
    if opcion == 1:
        nif_union, nif_not_union, nombre, edad= validar_opcion1()
        print(nif_union,nif_not_union,nombre,edad)
    elif opcion == 2:
        print("op2")
    elif opcion == 3:
        print("op3")
    elif opcion == 4:
        print("\nSaliendo del programa..\nAutor: Gonzalo Ulloa\nVersion: 1.0\n")
        break
