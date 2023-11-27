nombres = ["Jorge Rayo", "Oier Ganadero", "Moha Rata", "Bryan Pelotero"]
apellidonombre = []

def OrdenarNombre(lista, nueva_lista):
    """
    Esta función recibe un nombre y apellido y devuelve apellido, nombre
    Parámetros:
        -Nombre en el formato Nombre Apellido
    Salida:
        -Nombre en el formato Apellido, Nombre
    """
    for i in lista:
        Nombre, Apellido = i.split()
        nuevo = (format(Apellido,Nombre))
        nueva_lista.append(nuevo)

def ListaNombres(lista2):
    """
    La función recibe una lista de nombres y la ordena por apellidos en orden alfabético.
    Parámetros: 
        -Lista de nombres
    Salida:
        -Lista de nombres ordenados alfabéticamente
    """
OrdenarNombre (nombres, apellidonombre)
print (apellidonombre)

