import io
from posixpath import split
from click import option
from parso import split_lines
from SingleLinkedList import SingleLinkedList
class ReadData:
    #'r'->Modo lectura
    #'a'->Agregar info al archivo
    #'w'->Modo escritura - borrar
    def __init__(self):
        self.file = open('ArchivoRetoI.txt','r+')
        self.list_node = SingleLinkedList()
        self.Menu_I()
        
    def Menu_I(self):
        archivo = str(input("Ingrese el nombre del archivo (con '.txt' al final)\n      >>>"))
        while True:
            try:
                option = int(input("\nSeleccione una opción\n     1.Leer archivo\n     2.Editar archivo (añadir linea)\n     3.Sobreescribir archivo\n     4.Siguiente menú\n     >>>"))
                if option != 1 and option != 2 and option != 3 and option != 4:
                    option = int(input("Opción incorrecta\n     >>>"))
                elif option == 1:
                    self.Lectura_del_Archivo(archivo)
                elif option == 2:
                    self.Editar_Archivo(archivo)
                    print(">>La información deseada se agrego exitosamente al archivo<<")
                elif option == 3:
                    self.Sobreescribir_Archivo(archivo)
                    print(">>El archivo se sobreescribio de forma correcta<<")
                elif option == 4:
                    self.lines_to_nodes(archivo)
                    self.Menu_II(archivo)
                    break 
            except ValueError:
                    print("\n>>>Se espera un valor numerico<<<\n")
       
    def Menu_II(self,archivo):
        while True:
            try:
                option = int(input("\nSeleccione una opción\n     0.Ver lista de nodos\n     1.Insertar nodo\n     2.Eliminar nodo\n     3.Consultar valor de un nodo especifico\n     4.Editar valor nodo existente\n     5.Invertir contenido lista\n     6.Vaciar contenido lista\n     7.Cerrar sesión\n     >>>"))
                if option != 0 and option != 1 and option != 2 and option != 3 and option != 4 and option != 5 and option != 6 and option != 7:
                     option = int(input("Opción incorrecta\n     >>>"))
                elif option == 0:
                    self.list_node.show_nodes_list()
                elif option == 1:
                    self.Menu_Insertar_Nodo()
                    print("Nodo insertado exitosamente\n")
                    self.actualizar_archivo_txt(archivo)
                elif option == 2:
                    self.Menu_Eliminar_Nodo()
                    print("Nodo eliminado exitosamente\n")
                    self.actualizar_archivo_txt(archivo)
                elif option == 3:
                    index = int(input("Ingrese la posición del nodo del cual quiere consultar su valor\n     >>>"))
                    self.list_node.get(index)
                elif option == 4:
                    index = int(input("Ingrese la posición del nodo que quiere editar\n     >>>"))
                    value = str(input("Ingrese el valor a editar\n     >>>"))
                    self.list_node.update(index,value)
                    self.actualizar_archivo_txt(archivo)
                elif option == 5:
                    self.list_node.reverse_list()
                elif option == 6:
                    self.list_node.remove_all_elements()
                    self.vaciar_archivo(archivo)
                elif option == 7:
                    break
            except ValueError:
                print("\n>>>Se espera un valor numerico<<<\n") 
                
    def Menu_Insertar_Nodo(self):
        while True:
            try:
                option = int(input("\nDonde desea insertar el nodo\n     1.Al inicio\n     2.Al final\n     3.En una posicion especifica\n     >>>"))
                value = str(input("\nIngrese el valor del nodo a insertar\n      >>>"))
                if option != 1 and option != 2 and option != 3 and option != 4:
                    option = int(input("Opción incorrecta\n     >>>"))
                elif option == 1:
                    self.list_node.addFirst_Node(value)
                    break
                elif option == 2:
                    self.list_node.addLast_Node(value)
                    break
                elif option == 3:
                    index = int(input("\nIngrese el indice donde quiere insertar el nuevo nodo\n     >>>"))
                    self.list_node.insert(index,value)
                    break
            except ValueError:
                    print("\n>>>Se espera un valor numerico<<<\n")
                    
    def Menu_Eliminar_Nodo(self):
        while True:
            try:
                option = int(input("\nQue nodo desea eliminar\n     1.El inicio\n     2.El final\n     3.En una posicion especifica\n     >>>"))
                if option != 1 and option != 2 and option != 3 and option != 4:
                    option = int(input("Opción incorrecta\n     >>>"))
                elif option == 1:
                    self.list_node.deleteFirst_node()
                    break
                elif option == 2:
                    self.list_node.deleteLast_node()
                    break
                elif option == 3:
                    index = int(input("\nIngrese el indice del nodo a eliminar\n     >>>"))
                    self.list_node.remove(index)
                    break
            except ValueError:
                    print("\n>>>Se espera un valor numerico<<<\n")
                
    def Lectura_del_Archivo(self,archivo):
        with io.open(archivo,'r+', encoding='utf-8') as data_file:
            file_line = data_file.readline()
            while (file_line != ''):
                print(file_line, end='')
                file_line = data_file.readline()
        data_file.close()
        
    def Editar_Archivo(self,archivo):
        line_write = input('\nIngrese la información que quiere añadir al archivo txt : \n     >>>')
        with io.open(archivo,'a',encoding='utf-8') as data_file:
            data_file.write('\n'+line_write)
        data_file.close()
        
    def Sobreescribir_Archivo(self,archivo):
        new_data = str(input('\nIngrese la información a sobreescribir : \n     >>>'))
        lista = new_data.split(" ")
        with io.open(archivo,'w',encoding='utf-8') as data_file:
            for item  in range (len(lista)):
                if item != len(lista)-1:
                    data_file.write(lista[item]+'\n')
                else:
                    data_file.write(lista[item])
        print(lista)
        data_file.close()
        
    def lines_to_nodes(self,archivo):
        with io.open(archivo,'r+', encoding='utf-8') as data_file:
            lines = [line.strip() for line in data_file ]
            for item in range (len(lines)):
                new_node = SingleLinkedList.Node(lines[item])
                self.list_node.addLast_Node(new_node.value)
        data_file.close()
        
    def actualizar_archivo_txt(self,archivo):
        current_node = self.list_node.head
        with io.open(archivo,'w',encoding='utf-8') as data_file:
            while(current_node != None):
                data_file.write(current_node.value+'\n')
                current_node = current_node.linked_next_node
        data_file.close()
        
    def vaciar_archivo(self,archivo):
        with io.open(archivo,'a',encoding='utf-8') as data_file:
            data_file.truncate(0)