#Se inicializa el programa

import os, sys
# Importamos operador para organizar datos en el diccionario
import operator

# Diccionario de colores
colores = {
    "red":'\033[91m',
    "blue":'\033[94m',
    "end":'\033[0m'
}


def limpieza_pantalla():
    if sys.platform.startswith('linux'): 
        os.system('clear')

def separadores():
    print("="*50)

# Creacion del menu
def menu():
    mensaje = "\tBienvenido al MENÚ\n"
    mensaje+="_"*40
    mensaje+= "\n1) Crear listas"
    # mensaje+= "\n2) Mostrar Resultados"
    # mensaje+= "\n3) ¿Desea continuar?"
    return mensaje;

# Función encargada de guardar la opciopn del usuario
def opcion_elegida():
    return int(input("\nIngrese la opcion: "))

# Donde se valida la desicion del usuario
def desicion_menu(opcion):
    if (opcion != 1):
        return "XXXXXX Opción incorrecta!! XXXXXX"
    # return "Opcion correcta!!!"
    definir_logica(opcion)

#Funcion que define el proceso según la opcion
def definir_logica (opcion): 
    if opcion == 1:
        #Creación de listas
        creacion_lista()
    

# Función encargada de crear las listas que desea el usuario
def creacion_lista():

    # Lista que guarda los nombres de las listas
    list_names = []
    # Lista que guarda las listas de los datos
    list_datos =[]
    # Validacion de tipo de dato
    while True:
        try:
            cantidad_listas = int(input("->Cantidad de LISTAS a crear: "))
            cantidad_datos = int(input("->Cantidad de DATOS para las listas: ")) 
            print()
            break
        except ValueError:
            # Validar numero ingresado por el usuario, si el numero ES flotante
            # Hara una excepción 
            print(colores["red"] + '\tXXX ERROR :: DATO INCORRECTO' + ' SOLO numeros' + colores["end"] )
    # For que me pide los nombres
    for i in range(cantidad_listas):
        name_list = input(f"Nombre de la lista {i+1}: ")
        # Agregar nombre a la lista 
        list_names.append(name_list)
    # print(f"nombres listas = {list_names}\n")
    
# Ciclo que itera cada lista y lo almacena en la lista global
    for i in range(cantidad_listas):
        #Lista para guardar los datos solicitados
        datos_list = []
        # Ciclo que itera los datos ingresados y almacena en una lista
        separadores()
        print(f"lista :: {list_names[i]}")
        for i in range(cantidad_datos):
            # Ciclo que se repetira si el dato es incorrecto
            while True:
                # Tratamos de hacer
                try:
                    solitar_datos = float(input(f"Ingrese el dato a guardar {i+1}: "))
                    break
                except ValueError:
                    print(colores["red"] + "XX ERROR XX solo 'numeros'" + colores["end"])
            
            datos_list.append(solitar_datos)
        # Guardamos la lista de datos en la lista global
        list_datos.append(datos_list)
    # print(f"\n{list_datos}")

    # listas referenciadas
    separadores()
    print("\nListas con sus datos")
    for i in range(cantidad_listas):
        print(f"{list_names[i]} = {list_datos[i]}")
    print()

    # Función para calcular la media 
    calcular_desviacion_media(list_datos,list_names,cantidad_datos)


#Función que calcula la desviación media
def calcular_desviacion_media(list_datos,list_names,cantidad_datos):  
    # lista de promedios
    promedios_list = []
    for i in list_datos:
        promedio = ((sum(i)) / cantidad_datos);
        promedios_list.append(promedio)
    # print(f"promedios = {promedios_list}")

    #Lista para guardar la DM de cada lista 
    list_desviacion_media = []
    for i in range(len(list_datos)):
        # Variable bandera que llevara la suma de cada elemneto, reiniciandose cuando pasa de lista
        suma = 0
        list = list_datos[i]
        # Se pasa por cada elemneto de la lista
        for elemento in list:
            resta = abs(elemento - promedios_list[i])
            suma += resta 
        # Agregamos valor del proceso a la lista DM
        DM = suma / cantidad_datos
        list_desviacion_media.append(DM)
    
    print("Lista valores DM = ",list_desviacion_media)

    # Llamamos función
    organizar_datos(list_names, list_desviacion_media)



#  FUncion que organiza la la DM 
def organizar_datos(lists_names, list_dm):
    # Se crea el diccionario
    dicc1 = {}
    for i in range(len(lists_names)):
        #Agregamos item al dicicionario
        dicc1[lists_names[i]]=list_dm[i]
    # print(dicc1)
    # Se organiza El doiccionario con sus Values de menos a mayor
    organizarDicc1 = sorted(dicc1.items(), key=operator.itemgetter(1))
    
    # print(organizarDicc1)
    # Llamar funcion
    imprimir_resultado_final(organizarDicc1)

# Funcion enecargada de imprimir los resultados finales
def imprimir_resultado_final(dicc_valores):
    separadores()
    print("||||\tDATOS\t||||\n")
    # Pasamos por cada valor del diccionario e imprimimos
    for (k,v) in dicc_valores:
        print(f"Lista '{k}' presenta una desviacion media de {v}")



#///////////////////////////////////////
# Funcion que se encarga de inicializar el programa
def main():
    while True:
        print("_"*40)
        miMenu = menu()
        print(miMenu)
        # ciclo que valida que la opcion del usuario sea un numero
        while True:
            try:
                opcionUsuario = opcion_elegida()
                break
            except ValueError:
                print("Error :: DATO INCORRECTO")

        print("*"*30)
        validar_opcion = desicion_menu(opcionUsuario)
        # Se valida la opcion ingresada por el usuario
        if not validar_opcion is None:
            print(validar_opcion)
        desicion = input(colores["blue"] + "\nDesea continuar Si/No ::" + colores["end"] + "\n").lower()
        
        if(desicion != 'si'):
            # desicion = 'no'
            limpieza_pantalla()
            # Funcion que se encarga de limpiar la pantalla
            print("Hasta pronto!!")
            break
        else:
            limpieza_pantalla()


if __name__ == "__main__":
    main()