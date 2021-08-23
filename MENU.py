import os
from pilas import Pila 
from cola import Cola
from listas import Lista 


class Menu:
    def __init__(self, titulo, opciones=[]):
        self.titulo=titulo
        self.opciones= opciones
    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc = input("Elija la opción [1...{}]:".format(len(self.opciones)))
        return opc
opc = ""
while opc != "4":
    os.system("cls")
    men = Menu("Menu Principal",["1)Pila", "2)Cola", "3)Lista","4)Salir" ])
    opc = men.menu()
    dato=int(input("Ingrese el tamaño : "))
    pila1=Pila (dato)
    cola1= Cola (dato)
    lista1= Lista (dato)
    if opc == "1":
        opc1 = ""
        while opc1 != "6":
            os.system("cls")
            men1 = Menu("Menu Pila",["1)Push", "2)Pop", "3)Show","4)Longitud", "5)Empty", "6)Salir"])
            opc1 = men1.menu()
            if opc1 == "1":
                os.system("cls")
                print("OPERACIONES CON PUSH")
                valor=int(input("Ingrese el valor : "))
                print(pila1.push(valor))
                input("presione una tecla para continuar...")
                
            elif opc1 == "2":
                os.system("cls")
                print("OPERACIONES CON POP")
                dato = pila1.pop()
                if dato: print("el dato elimanado es :{}".format(dato))
                else: print(" La lista esta vacia")
                input("presione una tecla para continuar...")
            
            elif opc1 == "3":
                os.system("cls")
                print("OPERACIONES CON SHOW")
                pila1.show()
                input("presione una tecla para continuar...")
                
            elif opc1 == "4":
                os.system("cls")
                print("OPERACIONES CON LONGITUD") 
                num=pila1.longitud() 
                print("La longitud de la pila es:{}".format(num))
                input("presione una tecla para continuar...")
                
            elif opc1 == "5":
                 os.system("cls")
                 print("OPERACIONES CON EMPTY") 
                 valor1=pila1.empty()
                 if valor1:print("La pila se encuentra vacía")
                 else : print("La pila encuentra con elementos")
                 input("presione una tecla para continuar...")
                 
    if opc == "2":
        opc1 = ""
        while opc1 != "6":
            os.system("cls")
            men1 = Menu("Menu Cola ",["1)Push", "2)Pop", "3)Show","4)Longitud", "5)Empty", "6)Salir"])
            opc1 = men1.menu()
            if opc1 == "1":
                os.system("cls")
                print("OPERACIONES CON PUSH")
                valor=int(input("Ingrese el valor : "))
                print(cola1.push(valor))
                input("presione una tecla para continuar...")
                
            elif opc1 == "2":
                os.system("cls")
                print("OPERACIONES CON POP")
                dato = cola1.pop()
                if dato: print("el dato elimanado es :{}".format(dato))
                else: print(" La lista esta vacia")
                input("presione una tecla para continuar...")
                
            elif opc1 == "3":
                os.system("cls")
                print("OPERACIONES CON SHOW")
                cola1.show()
                input("presione una tecla para continuar...")
                
            elif opc1 == "4":
                os.system("cls")
                print("OPERACIONES CON LONGITUD") 
                num=cola1.longitud() 
                print("La longitud de la cola es:{}".format(num))
                input("presione una tecla para continuar...")
                
            elif opc1 == "5":
                 os.system("cls")
                 print("OPERACIONES CON EMPTY") 
                 valor1=cola1.empty()
                 if valor1:print("La cola se encuentra vacía")
                 else : print("La cola encuentra con elementos")
                 input("presione una tecla para continuar...")
                
    if opc == "3":
        opc1 = ""
        while opc1 != "8":
            os.system("cls")
            men1 = Menu("Menu Lista ",["1)Append", "2)Obtener Posicion ", "3)Buscar","4)Insertar", "5)Eliminar", "6)Obtener eliminado","7),Mostrar","8)Salir"])
            opc1 = men1.menu()
            if opc1 == "1":
                os.system("cls")
                print("OPERACIONES CON APPEND")
                dato=(input("Ingrese el dato de la lista : "))
                print(lista1.append(dato))
                input("presione una tecla para continuar...")
            
            if opc1 == "2":
                os.system("cls")
                print("OBTENER POSSION ")
                dato=int(input("Ingrese la possicion que desee conocer : "))
                print(lista1.obtener(dato))
                input("presione una tecla para continuar...")       
                
            if opc1 == "3":
                os.system("cls")
                print("BUSCAR ")
                dato=int(input("Ingrese el dato que desee conocer : "))
                print(lista1.buscar(dato))
                input("presione una tecla para continuar...")    
                
                          
                
            
                
    
                
                
            
                
                
            
                