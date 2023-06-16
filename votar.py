## DEPARTAMENTOS AGREGADOS: TODOS
## MUNICIPIOS AGREGADOS: 
## (MIXCO, CODIGO: 57), 
# (VILLA CANALES, CODIGO: 65), 
# (PUERTA PARADA, CODIGO: 73), 
# (AMATITLAN, CODIGO: 63), 
# (CHINAUTLA, CODIGO: 55)
bandera = 0
while bandera == 0:
    mayoredad = 16062005
    edad = int(input("Ingrese su edad: "))
    diferencia = mayoredad-edad
    if diferencia > 0:
        DPI = input("Ingrese su numero de DPI: ")
        mesa = DPI[:4]
        centro = DPI[4:9]
        departamento = DPI[9:11]
        municipio = DPI[11:]
        if departamento == '01':
            print("Departamento: Guatemala")
        elif departamento == '02':
            print("Departamento: El Progreso")
        elif departamento == '03':
            print("Departamento: Sacatepequez")
        elif departamento == '04':
            print("Departamento: Chimaltenango")
        elif departamento == '05':
            print("Departamento: Escuintla")
        elif departamento == '06':
            print("Departamento: Santa Rosa")
        elif departamento == '07':
            print("Departamento: Solola")
        elif departamento == '08':
            print("Departamento: Totonicapan")
        elif departamento == '09':
            print("Departamento: Quetzaltenango")
        elif departamento == '10':
            print("Departamento: Suchitepequez")
        elif departamento == '11':
            print("Departamento: Retalhuleu")
        elif departamento == '12':
            print("Departamento: San Marcos")
        elif departamento == '13':
            print("Departamento: Huehuetenango")
        elif departamento == '14':
            print("Departamento: Quiche")
        elif departamento == '15':
            print("Departamento: Baja Verapaz")
        elif departamento == '16':
            print("Departamento: Alta Verapaz")
        elif departamento == '17':
            print("Departamento: Peten")
        elif departamento == '18':
            print("Departamento: Izabal")
        elif departamento == '19':
            print("Departamento: Zacapa")
        elif departamento == '20':
            print("Departamento: Chiquimula")
        elif departamento == '21':
            print("Departamento: Jalapa")
        elif departamento == '22':
            print("Departamento: Jutiapa")
        
        if municipio == '57':
            print("Municipio: Mixco")
        elif municipio == '65':
            print("Municipio: Villa Canales")
        elif municipio == '73':
            print("Municipio: Puerta Parada")
        elif municipio == '63':
            print("Municipio: Amatitlan")
        elif municipio == '55':
            print("Municipio: Chinautla")

        print("Centro de votacion: ",centro)
        print("Numero de Mesa: ",mesa)

        respuesta = input("¿Desea realizar otra consulta? (S/N)")
        match respuesta:
            case 'S':
                bandera = 0
            case 'N':
                print("Gracias por usar el programa!")
                bandera = 1
            case _:
                print("No ingreso una opcion valida!. Retornandolo al inicio...")
    else:
        respuesta = input("Aun no puede votar. ¿Desea realizar otra consulta? (S/N)")
        match respuesta:
            case 'S':
                bandera = 0
            case 'N':
                print("Gracias por usar el programa!")
                bandera = 1
            case _:
                print("No ingreso una opcion valida!. Retornandolo al inicio...")