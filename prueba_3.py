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
        if nombre != None:
            buscar = validar_opcion2()
            buscar_nif(buscar)
        else:
            print("\nError: no hay usuarios registrados, ingrese a la opcion 1")

    elif opcion == 3:
        if nombre != None:
            nacimiento,estado,buscar = validar_opcion3()
            print("\n                    certificado")
            print("\nAño de nacimiento:",nacimiento)
            print("\nEstado conyugal:",estado)
            buscar_nif(buscar)
        else:
            print("\nError: no hay usuarios registrados, ingrese a la opcion 1")
    elif opcion == 4:
        print("\nSaliendo del programa..\nAutor: Gonzalo Ulloa\nVersion: 1.0\n")
        break

print("\nQue tenga un buen dia")
