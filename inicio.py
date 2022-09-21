class agentaTelefonica:
    def __init__(self,nombre,numero,direccion):
        self.__nombre=nombre
        self.__numero=numero
        self.__direccion=direccion
    
    #crear métodos GETTER
    def verNombre(self):
        return self.__nombre
    
    def verNumero(self):
        return self.__numero
    
    def verDireccion(self):
        return self.__direccion
    
    #métodos SETTER
    def modificarNombre(self,nuevonombre):
        self.__nombre=nuevonombre
    
    def modificarNumero(self,nuevoNumero):
        self.__numero= nuevoNumero
    
    def modificardireccion(self,nuevaDireccion):
        self.__direccion=nuevaDireccion