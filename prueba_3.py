from funciones import *
menu = True
nombre = None

while menu:
    print("\n          Registro de ciudadados")
    print("\n1.Grabar\n2.Buscar\n3.Imprimir certificados\n4.Salir")
    opcion = validar_menu()
    if opcion == 1:
        nif_union, nif_not_union, pertenece = validar_nif()
        nombres, edades,nombre= validar_opcion1()
    elif opcion == 2:
        validar_opcion2(nombre)
    elif opcion == 3:
        validar_opcion3(nombre)
    elif opcion == 4:
        print("\nSaliendo del programa..\nAutor: Gonzalo Ulloa\nVersion: 1.0\n")
        break
