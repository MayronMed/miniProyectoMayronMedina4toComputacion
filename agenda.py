from io import open
from inicio import agentaTelefonica
misContactos=[]

#Crear contactos
def NuevoContacto(nombre, numero, direccion):
    misContactos.append(agentaTelefonica(nombre, numero, direccion))

def BuscarContacto(nombre):
    if len(misContactos) ==0:
        print('la lista esta vacia, no hay contactos')
    else:
        encontrado = False
        for i in range(len(misContactos)):
            if misContactos[i].verNombre() == nombre:
                print('el telefono es ', misContactos[i].verNumero())
                print('la direccion es ', misContactos[i].verDireccion())
                encontrado = True
                break 


#mostrar contactos
def MostrarContactos():
    for i in range(len(misContactos)):
        print('Nombre: ',misContactos[i].verNombre())
        print('Numero: ',misContactos[i].verNumero())
        print('Direccion: ',misContactos[i].verDireccion())
    
 #buscar y modificar contacto
def ModificarContacto(nombre, nuevaDireccion):
    posicion=None
    for indice in range (len(misContactos)):
        if nombre == misContactos[indice].verNombre():
            posicion = indice
            break
    if posicion == None:
        return 'El cliente ingresado no existe'
    else:
        misContactos[posicion].modificardireccion(nuevaDireccion)
        return 'Datos del cliente actualizados con éxito'

#Buscar y eliminar
def EliminarContacto(nombre):
    posicion= None
    for m in range(len(misContactos)):
        if nombre == misContactos[m].verNombre():
            posicion= m
            break
    if posicion==None:
        return 'El cliente no existe'
    else:
        misContactos.pop(posicion)
        return 'Cliente eliminado con éxito'

def crearReporte():
    documento = open("reporte contactos.html","w")
    documento.write("<!doctype html>\n")
    documento.write("<html>\n")
    documento.write("<head>\n")
    documento.write("\t<title>Agenda 2022</title>\n")
    documento.write("</head>\n")
    documento.write("<body>\n")
    documento.write("\t<center>\n")
    documento.write("\t<h1>Mis contactos</h1>\n")
    documento.write('\t<table border="1">\n')
    documento.write("\t\t<tr>\n")
    documento.write("\t\t\t<td>Número de teléfono</td><td>Nombre</td><td>Dirección</td>\n")
    for i in range(len(misContactos)):
        documento.write("\t\t<tr>\n")
        documento.write("\t\t\t<td>" + str(misContactos[i].verNumero()) + "</td><td>" + misContactos[i].verNombre() + "</td><td>" + misContactos[i].verDireccion() + "</td>")
        documento.write("\t\t</tr>\n")

    documento.write("\t\t</tr>\n")
    documento.write("\t</table>\n")
    documento.write("\t</center>\n")
    documento.write("</body>\n")
    documento.write("</html>")
    documento.close()
    print('reporte HTML creado con exito...')
def main():
    op=0
    while op!=7:
        print('-----------AGENDA TELEFÓNICA------------- \n',
        '1. Crear contacto \n'
        '2. Buscar contacto \n',
        '3. Ver contactos \n',
        '4. Modificar contactos \n',
        '5. Eliminar contacto\n'
        '6. Reporte en HTML\n',
        '7. Salir del programa\n')
        op=int(input('Ingrese una opción del menú: '))
        if op==1:
            nombre=input('Ingrese nombre: ')
            numero=int(input('Ingrese número de telefono: '))
            direccion=input('Ingrese direccion cliente: ')
            NuevoContacto(nombre, numero, direccion)
            print('contacto creado')
            print('----------------------------------------------\n')

        elif op==2:
            nombre=input('ingrese nombre del contacto: ')
            BuscarContacto(nombre)
        
        elif op==3:
            MostrarContactos()
            print('--------------------------------------\n')
        
        elif op==4:
            nombre=input('Ingrese el nombre del cliente: ')
            nuevadireccion=input('Ingrese nueva dirección: ')
            print(ModificarContacto(nombre,nuevadireccion))
            print('----------------contacto modificado--------------------')
            print('------------------------------------------------------\n')
        
        elif op==5:
            nombre=input('Ingrese el nombre del cliente: ')
            print(EliminarContacto(nombre))
            print('------------------contacto eliminado-----------------')
            print('------------------------------------------------------\n')

        elif op==6:
            crearReporte()


        elif op==7:
            print('################# FIN DEL PROGRAMA ##################')
        else:
            print('Número de opción no válido')
        
main()