import csv
codigopartidos = []
nombrepartidos = []
siglaspartidos = []
votospartidos = []
partidos = [codigopartidos, nombrepartidos, siglaspartidos, votospartidos]
bandera = 0
contador = 1

def exportarnotas(lista, nombre_archivo):
    # CREAMOS UN TRY EXCEPT PARA VERIFICAR QUE AL EXPORTAR NO TENGA NINGUN TIPO DE ERROR
    try:
        # EN ESTA PRIMERA LINEA NO LE GENERARA ES EL FORMATO DE EL ARCHIVO CSV, AÑADIENDOLO A UNA NUEVA LINEA, GENERANDO EL NOMBRE DEL ARCHIVO Y EN MODE 'W'
        # MODE 'W' GENERARA UN ARCHIVO DE ESCRITURA UNICAMENTE, PARA QUE EL ARCHIVO PUEDA SER MODIFICADO NO NECESARIAMENTE DESDE EL PROGRAMA
        with open(nombre_archivo, mode='w', newline='') as archivo_csv:
            # CREAMOS UNA VARIABLE WRITER, EL CUAL CONTENDRA EL FORMATO DEL ARCHIVO, EL DELIMITADOR QUE NOS SERVIRA EN CASO HAYAN TEXTOS MUY LARGOS
            # TAMBIEN CON UN QUOTECHAR QUE EN CASO DE SER UNA CITA, LO MOSTRARA ENTRE "" Y DE ULTIMO EL PROGRAMA VERIFICARA SI ES UNA CITA O NO
            writer = csv.writer(archivo_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            # CREAMOS UN FOR QUE RECORRERA LA VARIABLE LISTA
            for elemento in lista:
                # Y EL ELEMENTO LO IREMOS IMPRIMIENDO EN UNA NUEVA COLUMNA PARA ASI SE PUEDA VER DE MEJOR MANERA
                writer.writerow(elemento)
    # EN CASO ENCONTRARA UN ERROR, SE LE MOSTRARA EL MENSAJE DE ADVERTENCIA Y RETORNARA EL MENU PRINCIPAL
    except:
        print("Ocurrio un error, intentelo de nuevo mas tarde")


cantidad = int(input("Ingrese la cantidad de partidos a ingresar: "))
while bandera == 0:
    print("BIENVENIDO AL CONTEO RAPIDO")
    print("1. Ingresar partidos politicos")
    print("2. Ingresar actas")
    print("3. Ver Resultados")
    print("4. Exportar resultados")
    print("5. Salir")
    opcion = input("Seleccione una opcion: ")
    match opcion:
        case '1':
            for i in range(0, cantidad):
                print("Partido No.",contador)
                codpartido = input("Ingrese el codigo del partido: ")
                codigopartidos.append(codpartido)
                nombrepartido = input("Ingrese el nombre del partido: ")
                nombrepartidos.append(nombrepartido)
                siglapartidos = input("Ingrese las siglas del partido: ")
                siglaspartidos.append(siglapartidos)
                contador+=1
        case '2':
            for i in range(0, cantidad):
                print("Partido: ",nombrepartidos[i])
                votos = input("Ingrese el numero de votos: ")
                votospartidos.append(votos)
        case '3':
            print("Partidos    |          Votos")
            for i in range(0, cantidad):
                print(nombrepartidos[i], "       |       ", votospartidos[i])
        case '4':
            nombrearchivo = input("Ingrese el nombre del archivo sin la extension .csv: ")
            exportarnotas(partidos, nombrearchivo+".csv")
            print("Archivo exportado con exito")
        case '5':
            print("Gracias por usar el programa!")
            bandera = 1
        case _:
            print("No ingreso una opcion valida!. Retornandolo al menu...")