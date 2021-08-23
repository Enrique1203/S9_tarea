class Lista ():
    def __init__(self,tamanio=3):
        self.lista = []
        self.longitud = 0
        self.size = tamanio
        
    def append(self,dato):
        if self.longitud < self.size:
            self.lista += [dato]
            self.longitud +=1
            return self.lista
        else:
            print("Lista esta llena")
            
    def obtener(self,pos):
        if pos < 0 or pos >= self.longitud:
            return None
        else:
            return self.lista[pos]
     #busca un dato en la lista y retorna la posicion de ese valor en la lista    
    def buscar(self,buscado):
        print("Buscar un valor en una lista")
        enc=False
        for pos,ele in enumerate(self.lista):
            if ele==buscado:
                enc=True
                break
        if enc==True:
           print("Su valor si se encuentra en la lista, se encuentra en la posicion: {}".format(pos))
        else:
            print("Su valor no se encuentra en la lista")
            
   #busca un dato con el metodobuscar y si no lo encuentro inserte           
    def insertar(self,valor):
        if(self.buscar (valor)):
            print("Su valor si se encuentra en la lista, se encuentra en la posicion: {}".format(valor))
        else:
            print("No se puede insertar ,ya se encuentra dentro de la lista") 
            
        
        
        
        
        
       
    # busca el dato eliminar con el metodo buscar y lo elimina de lista 
    def eliminar(self,dato):
        
       pass 
    def obtenerEliminado(self,pos):
        if pos < 0 or pos >= self.longitud:
            return None
        else:
            eliminado = self.lista[pos]
            #self.lista = self.lista[:dato] + self.lista[dato+1:]
            listaAux = []
            for ind in range(pos):
                listaAux += [self.lista[ind]]
            for indice in range(pos+1,self.longitud):
                listaAux += [self.lista[indice]]
                self.longitud -= 1
                self.lista = listaAux
            return [self.lista,eliminado]
            
    
    def mostrar(self):
        print(" {:6} {}".format("lista","Posicion"))
        for pos, ele in enumerate(self.lista):
            print("[{:6}] {:3}".format(ele,pos))
            
lista1 = Lista()
lista1.append("Daniel")
lista1.append(52)
lista1.append(32)
lista1.append("Milagro")
# pos=lista1.buscar(52)
lista1.insertar(68)

# if dato:print("El elemento se encuentra en la lista:{}".format(dato))
# else : print("El elemento no se encuentra en la lista")
# lista1.mostrar()
# print(lista)

# posicion=int(input("Ingrese posicion:"))
# resp = lista1.obtenerEliminado(posicion)
# if resp == None:
#     print("Posicion no Valida")
# else:
#     print("El elemento de la posicion: {} es: {}".format(posicion,resp))
     