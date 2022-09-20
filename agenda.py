from inicio import agentaTelefonica
registro=[]

#Crear contactos
def nuevocontacto(nombreCliente, numero, direccion):
    registro.append(agentaTelefonica(nombreCliente, numero, direccion))

#mostrar contactos
def mostrarcontactos():
    for i in range(len(registro)):
        print(registro[i].verNombre())
        print(registro[i].verNumero())
        print(registro[i].verdireccion())
    print('------------------------------------------')

 #buscar y modificar contacto
def BuscarModificar(nombreCliente, nuevaDireccion):
    posicion=None
    for indice in range (len(registro)):
        if nombreCliente==registro[indice].verNombre():
            posicion = indice
            break
    if posicion==None:
        return 'El cliente ingresado no existe'
    else:
        registro[posicion].modificardireccion(nuevaDireccion)
        return 'Datos del cliente actualizados con éxito'

#Buscar y eliminar
def buscaryeliminar(nombreCliente):
    posicion= None
    for m in range(len(registro)):
        if nombreCliente == registro[m].verNombre():
            posicion= m
            break
    if posicion==None:
        return 'El cliente no existe'
    else:
        registro.pop(posicion)
        return 'Cliente eliminado con éxito'

def main():
    op=0
    while op!=5:
        print('AGENDA TELEFÓNICA \n',
        '1. Crear contacto \n',
        '2. Ver contactos \n',
        '3. Modificar contactos \n',
        '4. Eliminar contacto\n',
        '5. Salir del programa\n')
        op=int(input('Ingrese una opción del menú: '))
        if op==1:
            nombre=input('Ingrese nombre: ')
            numero=int(input('Ingrese número de telefono: '))
            direccion=input('Ingrese direccion cliente: ')
            nuevocontacto(nombre, numero, direccion)
            print('contacto creado')
            print('----------------------------------------------')
        
        elif op==2:
            mostrarcontactos()
            print('')
        
        elif op==3:
            nombre=input('Ingrese el nombre del cliente: ')
            nuevadireccion=input('Ingrese nueva dirección: ')
            print(BuscarModificar(nombre,nuevadireccion))
            print('------------------------------------------------------')
        
        elif op==4:
            nombre=input('Ingrese el nombre del cliente: ')
            print(buscaryeliminar(nombre))
            print('------------------------------------------------------')
        elif op==5:
            print('################# FIN DEL PROGRAMA ##################')
        else:
            print('Número de opción no válido')
        
main()