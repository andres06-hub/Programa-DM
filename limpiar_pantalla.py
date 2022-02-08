import os, sys

# Funcion que limpia pantalla
def limpieza_pantalla():
    if sys.platform.startswith('linux'): 
        os.system('clear')
    elif sys.platform.startswith('win'):
        os.system('cls')