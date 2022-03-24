class SingleLinkedList:
    class Node:
        def __init__(self,value):
            self.value = value
            self.linked_next_node = value = None
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    #Método que imprime el contenido de la lista simplemente enlazada
    def show_nodes_list(self):
        node_list = []
        current_node = self.head
        #Recorremos la lista hasta que no existan nodos
        while(current_node != None):
            #A la lista node_list ke agregamos  al final el valor del nodo actual
            node_list.append(current_node.value)
            current_node = current_node.linked_next_node
        print(f'{node_list} Cantidad de nodos es {self.length}')
    
    #Método que agrega un nodo nuevo al INICIO de la lista   
    def addFirst_Node(self,value):
        new_node = self.Node(value)
        #Consultar si  la lista No tiene head y cola
        if self.head == None and self.tail == None:
            #En este caso la lista esta vacía, no tiene nodos
            self.head = new_node
            self.tail = new_node
        else:
            #En este caso la lista contiene al menos un nodo
            #Para este caso habría que enlazar el nodo nuevo con la cabeza de la lista
            new_node.linked_next_node = self.head
            #Actualizar la cabeza de la lista
            self.head = new_node
        self.length += 1
    
    #Método que agrega un nodo nuevo al FINAL de la lista   
    def addLast_Node(self,value):
        new_node = self.Node(value)
        #Consultar si  la lista No tiene head y cola
        if self.head == None and self.tail == None:
            #En este caso la lista esta vacía, no tiene nodos
            self.head = new_node
            self.tail = new_node
        else:
            #En este caso la lista contiene al menos un nodo
            #Para este caso habría que enlazar el nodo nuevo con la cola de la lista
            self.tail.linked_next_node = new_node
            #Actualizar la cola de la lista
            self.tail = new_node
        self.length += 1
        
    #Eliminar el primer nodo de la lista
    def deleteFirst_node(self):
        if self.length == 0:
            self.head = None
            self.tail = None
        else:
            #Eliminamos la cabeza de la lista
            remove_node = self.head
            #El nodo que le seguia  al primero pasa a ser la cabeza de la lista
            self.head = remove_node.linked_next_node
            #Eliminamos el enlace del nodo que se eliminara de la lista
            remove_node.linked_next_node = None
            self.length -= 1
            print(f'El valor del nodo eliminado es {remove_node.value}')
            
    #Eliminar el ultimo nodo de la lista
    def deleteLast_node(self):
        if self.length == 0:
                self.head = None
                self.tail = None
        else:
            #Creamos una variabe para iniciar al recorrido de la lista desde las cabeza
            current_node = self.head
            #Creamos una variable que asignara el nuevo valor de la cola
            new_tail = current_node
            while (current_node.linked_next_node != None):
                new_tail = current_node
                current_node = current_node.linked_next_node
            self.tail = new_tail
            self.tail.linked_next_node = None
            self.length -= 1
            print(f'El valor del nodo eliminado es {current_node.value}')
            
    def reverse_list(self):
        nodeAux = None
        nodeAux2 = None
        current_node = self.head
        if self.length == 0:
                self.head = self.tail
                self.tail = self.head
        else:
            while(current_node != None):
                nodeAux2 = current_node.linked_next_node
                current_node.linked_next_node = nodeAux
                nodeAux = current_node
                current_node = nodeAux2
            self.head = nodeAux
    
    def get(self, index):
        #Obtine un nodo dado un index
        #Si el indice es el utimo nodo de la lista, nos referimos a la cola
        if index == self.length - 1:
            print(self.tail.value)
            return self.tail
        #Si el indice es el primer value de la lista, nos referimos a la cabeza 
        elif index == 0:
            print(self.head.value)
            return self.head
        #De lo contrario, es porque el indice esta en una posicion intermedia de la lista
        #Validar que el indice se encuentra entre los rangos permitidos de la lista
        elif not (index >= self.length or index < 0):
            current_node = self.head
            contador = 0
            #Recorremos la lista siempre y cuando el contador sea diferente al nodo a buscar
            while contador != index:
                #Incrementamos en una el while pasando a visitar el siguiente nodo
                current_node = current_node.linked_next_node
                contador += 1
            print(current_node.value)
            return current_node
        else:
            return None
    
    #Método que nos permite actualizar el valor del nodo
    def update(self, index, value):
        #Cambia el value de un nodo dado un index
        nodo_objetivo = self.get(index)
        if nodo_objetivo != None:
            #Reemplazamos el valor actual del nodo por el suministrado por el usuario
            nodo_objetivo.value = value
        else:
            return None
        
    #Agrega un elemento en la liista dado el index 
    def insert(self,index,value):
        #Siempre que se desee crear un nuevo nodo es necesario solicitar el valor
        #Si el usuario quiere añadir el nodo al final de la lista, se llama la función append_node() o addLast_Node()
        if index == self.length:
            return self.addLast_Node(value)
        #Se valida si el nodo se quiere insertar en la cabeza de la lista
        elif index == 1:
            return self.addFirst_Node(value)
        #Se valida si el indice esta entre los rangos de la lista
        elif not (index >= self.length or index < 0):
            new_node = self.Node(value)
            #Identificamos los nodos contonuos al nuevo nodo
            nodos_anteriores = self.get(index-2)
            nodos_siguientes = nodos_anteriores.linked_next_node
            #Generamos los enlaces del nuevo nodo con el anterior y el siguiente
            nodos_anteriores.linked_next_node = new_node
            new_node.linked_next_node = nodos_siguientes
            self.length += 1
        else:
            return None
        
    def remove(self, index):
        #Saca un elemento de donde sea de la LinkedList dado un index
        if index == 1:
            return self.deleteFirst_node()
        elif index == self.length:
            return self.deleteLast_node()
        elif not (index > self.length  or index <= 0):
            nodos_anteriores = self.get(index-2)
            nodo_removido = nodos_anteriores.linked_next_node
            nodos_anteriores.linked_next_node = nodo_removido.linked_next_node
            nodo_removido.linked_next_node = None
            self.length -= 1
        else:
            return None
        
    #Método para vaciar la lista de nodos 
    def remove_all_elements(self):
        i=0
        length = self.length
        while i<length:
            self.deleteFirst_node()
            i += 1
        self.length = 0