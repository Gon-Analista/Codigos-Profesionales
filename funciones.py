valido = True
nif_union = [] ; nif_not_union = []
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

def validar_opcion1():
    while valido:
        nif = str(input("\nIngrese su NIF:\t"))
        if len(nif) == 12 and nif[0:8].isdigit() and nif[9:11].isalpha():
            nif_union.append(nif)
            break
        else:
            print("\nError: debe ingresar un NIF valido, ejemplo: '99999999-RTX'")
            nif_not_union.append(nif)

    while valido:
        nombre = str(input("\nIngrese su nombre:\t"))
        if len(nombre) >= 8:
            break
        else:
            print("\nError: Su nombre debe tener como minimo 8 caracteres")
    while valido:
        try:
            edad = int(input("\ningrese su edad:\t"))
            if edad > 0:
                break
            else:
                print("\nError: Ingrese una edad mayor a 0")
        except ValueError:
            print("\nError: Ingrese su edad en numeros")


    return nif_union,nif_not_union,nombre,edad