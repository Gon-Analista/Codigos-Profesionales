valido = True
nif_union = [] ; nif_not_union = [] ; nombres  = [] ; edades = []
def validar_menu():
    while valido:
        try:
            opcion = int(input("\nIngrese la opcion que desee:\t"))
            if opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4:
                return opcion
            else:
                print("\nError: ingrese opcion 1,2,3,4 segun corresponda")
        except ValueError:
            print("\nError: ingrese la opcion como un numero")

def validar_nif():
    while valido:
        nif = str(input("\nIngrese su NIF:\t"))
        if len(nif) == 12 and nif[0:8].isdigit() and nif[9:11].isalpha():
            pertenece = "Usted pertenece a la union"
            nif_union.append(nif)
            break
        else:
            pertenece = "Usted no pertenece a la union"
            nif_not_union.append(nif)
            break
    return nif_union,nif_not_union,pertenece
def validar_opcion1():
    while valido:
        nombre = str(input("\nIngrese su nombre:\t"))
        if len(nombre) >= 8:
            nombres.append(nombre)
            break
        else:
            print("\nError: Su nombre debe tener como minimo 8 caracteres")
    while valido:
        try:
            edad = int(input("\ningrese su edad:\t"))
            if edad > 0:
                edades.append(edad)
                break
            else:
                print("\nError: Ingrese una edad mayor a 0")
        except ValueError:
            print("\nError: Ingrese su edad en numeros")
    return nombres,edades,nombre

def validar_opcion2(nombre):
    if nombre != None:
        buscar = str(input("\nIngrese el NIF de la persona que desea buscar:\t"))
        while valido:
            try:
                if buscar in nif_not_union:
                    index = nif_not_union.index(buscar)
                    print("\nNIF:",nif_not_union[index])
                    print("\nNombre:",nombres[index])
                    print("\nEdad:",edades[index])
                    print("\nEsta persona no pertenece a la union")
                elif buscar in nif_union:
                    print("\nNIF:",nif_not_union[index])
                    print("\nNombre:",nombres[index])
                    print("\nEdad:",edades[index])
                    print("\nEsta persona no pertenece a la union")
                else:
                    print("\nError: no se encuentra en la lista")
                break
            except ValueError:
                print("\nError: no se encuentra en la lista")
                break
    else:
        print("\nError: No tenemos usuarios registrados, ingrese a la opcion 1")

def validar_opcion3(nombre):
    if nombre != None:
        nacimiento = str(input("Ingrese su fecha de nacimiento: "))
        estado = str(input("Ingrese su estado conyugal: "))
        nif_union, nif_not_union, pertenece = validar_nif()
        print(pertenece)
     
    
    else:
        print("\nError: No tenemos usuarios registrados, ingrese a la opcion 1")
