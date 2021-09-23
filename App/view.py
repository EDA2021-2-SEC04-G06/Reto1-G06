
"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

from datetime import datetime
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
sys.setrecursionlimit(1000*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("\nBienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Catálogo cronológico de los artistas")
    print("3- Catálogo cronológico por fecha de adquisición de obras")
    print("4- Obras de artista por tecnica")
    print("5- Obras segun nacionalidad del creador")
    print("6- Calcular costo de transportar todas las obras de un departamento")
    print("7- Reglas de transporte")
    print("8- Proponer nueva exposicion en el museo")


def initCatalog(estructura):
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog(estructura)


def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)


def printPrimeros3Artistas(lista, size):
    if size >= 3:
        print("Los primeros 3 Artistas son: ")
        i = 1
        while i <= 3:
            artistas = lt.getElement(lista, i)
            nombre = artistas['DisplayName']
            anho_nacimiento = artistas['BeginDate']
            anho_fallecido = artistas['EndDate']
            nacionalidad = artistas['Nationality']
            genero = artistas['Gender']
            if anho_fallecido == "0":
                anho_fallecido = "Sigue vivo o se desconoce su muerte"
            print(str(i)+". " + "Artista: " + nombre + ", Año de Nacimiento: "
                  + anho_nacimiento + ", Año de Fallecimiento: " + anho_fallecido
                  + ", Nacionalidad: " + nacionalidad + ", Genero: " + genero)
            i += 1
        print("...")

    elif size >= 1:
        if size == 1:
            print("El primer Artista es: ")
        if size == 2:
            print("Los primeros 2 Artistas son: ")
        i = 1
        while i <= size:
            artistas = lt.getElement(lista, i)
            nombre = artistas['DisplayName']
            anho_nacimiento = artistas['BeginDate']
            anho_fallecido = artistas['EndDate']
            nacionalidad = artistas['Nationality']
            genero = artistas['Gender']
            if anho_fallecido == "0":
                anho_fallecido = "Sigue vivo o se desconoce su muerte"
            print(str(i)+". " + "Artista: " + nombre + ", Año de Nacimiento: "
                  + anho_nacimiento + ", Año de Fallecimiento: " + anho_fallecido
                  + ", Nacionalidad: " + nacionalidad + ", Genero: " + genero)
        print("...")

    else:
        return None


def ultimos3Artistas(lista, size):
    if size >= 3:
        print("Los últimos 3 Artistas son: ")
        i = size-2
        while i <= size:
            artistas = lt.getElement(lista, i)
            nombre = artistas['DisplayName']
            anho_nacimiento = artistas['BeginDate']
            anho_fallecido = artistas['EndDate']
            nacionalidad = artistas['Nationality']
            genero = artistas['Gender']
            if anho_fallecido == "0":
                anho_fallecido = "Sigue vivo o se desconoce su muerte"
            print(str(i)+". " + "Artista: " + nombre + ", Año de Nacimiento: "
                  + anho_nacimiento + ", Año de Fallecimiento: " + anho_fallecido
                  + ", Nacionalidad: " + nacionalidad + ", Genero: " + genero)
            i += 1

    elif size >= 1:
        if size == 1:
            print("El último Artista es: ")
        if size == 2:
            print("Los últimos 2 Artistas son: ")
        i = 1
        while i <= size:
            artistas = lt.getElement(lista, i)
            nombre = artistas['DisplayName']
            anho_nacimiento = artistas['BeginDate']
            anho_fallecido = artistas['EndDate']
            nacionalidad = artistas['Nationality']
            genero = artistas['Gender']
            if anho_fallecido == "0":
                anho_fallecido = "Sigue vivo o se desconoce su muerte"
            print(str(i)+". " + "Artista: " + nombre + ", Año de Nacimiento: "
                  + anho_nacimiento + ", Año de Fallecimiento: " + anho_fallecido
                  + ", Nacionalidad: " + nacionalidad + ", Genero: " + genero)
    else:
        return None


def printprimeros3artistasyobras(lista, size):
    if size >= 3:
        print("Las primeras 3 Obras son: ")
        i = 1
        while i <= 3:
            obra = lt.getElement(lista, i)
            titulo = obra['Title']
            fecha = obra['Date']
            medio = obra['Medium']
            dimensiones = obra['Dimensions']
            cadenaArtista = ""
            for artistas in lt.iterator(obra['artists']):
                artista = artistas['DisplayName']
                if cadenaArtista == "":
                    cadenaArtista += artista
                else:
                    cadenaArtista += ", "+artista
            if fecha == "":
                fecha = "Unknown"
            if medio == "":
                medio = "Unknown"
            if dimensiones == "":
                dimensiones = 'Unknown'
            if cadenaArtista == "":
                cadenaArtista = "Unknown"

            print(str(i)+". " + "Titulo: " + titulo + ", Artista(s): " + cadenaArtista + ", Fecha: "
                  + fecha + ", Medio: " + medio
                  + ", Dimensiones: " + dimensiones)
            i += 1
        print('...')

    elif size >= 1:
        if size == 1:
            print("La primera obra es: ")
        if size == 2:
            print("Las primeras 2 Artistas son: ")
        i = 1
        while i <= size:
            obra = lt.getElement(lista, i)
            titulo = obra['Title']
            fecha = obra['Date']
            medio = obra['Medium']
            dimensiones = obra['Dimensions']
            cadenaArtista = ""
            for artistas in lt.iterator(obra['artists']):
                artista = artistas['DisplayName']
                if cadenaArtista == "":
                    cadenaArtista += artista
                else:
                    cadenaArtista += ", "+artista

            if fecha == "":
                fecha = "Unknown"
            if medio == "":
                medio = "Unknown"
            if dimensiones == "":
                dimensiones = 'Unknown'
            if cadenaArtista == "":
                cadenaArtista = "Unknown"

            print(str(i)+". " + "Titulo:" + titulo + ", Artista(s): " + cadenaArtista + ", Fecha: "
                  + fecha + ", Medio: " + medio
                  + ", Dimensiones: " + dimensiones)
            i += 1
        print('...')

    else:
        return None


def printUltimos3ArtistasyObras(lista, size):
    if size >= 3:
        print("Los últimos 3 Artistas son: ")
        i = size-2
        while i <= size:
            obra = lt.getElement(lista, i)
            titulo = obra['Title']
            fecha = obra['Date']
            medio = obra['Medium']
            dimensiones = obra['Dimensions']
            cadenaArtista = ""
            for artistas in lt.iterator(obra['artists']):
                artista = artistas['DisplayName']
                if cadenaArtista == "":
                    cadenaArtista += artista
                else:
                    cadenaArtista += ", "+artista

            if fecha == "":
                fecha = "Unknown"
            if medio == "":
                medio = "Unknown"
            if dimensiones == "":
                dimensiones = 'Unknown'
            if cadenaArtista == "":
                cadenaArtista = "Unknown"

            print(str(i)+". " + "Titulo:" + titulo + ", Artista(s): " + cadenaArtista + ", Fecha: "
                  + fecha + ", Medio: " + medio
                  + ", Dimensiones: " + dimensiones)
            i += 1
    elif size >= 1:
        if size == 1:
            print("La última Obra es: ")
        if size == 2:
            print("Los últimos 2 Artistas son: ")
        i = 1
        while i <= size:
            obra = lt.getElement(lista, i)
            titulo = obra['Title']
            fecha = obra['Date']
            medio = obra['Medium']
            dimensiones = obra['Dimensions']
            cadenaArtista = ""
            for artistas in lt.iterator(obra['artists']):
                artista = artistas['DisplayName']
                if cadenaArtista == "":
                    cadenaArtista += artista
                else:
                    cadenaArtista += ", "+artista

            if fecha == "":
                fecha = "Unknown"
            if medio == "":
                medio = "Unknown"
            if dimensiones == "":
                dimensiones = 'Unknown'
            if cadenaArtista == "":
                cadenaArtista = "Unknown"

            print(str(i)+". " + "Titulo:" + titulo + ", Artista(s): " + cadenaArtista + ", Fecha: "
                  + fecha + ", Medio: " + medio
                  + ", Dimensiones: " + dimensiones)
            i += 1
    else:
        None


def printTOP10(lista):
    size = lt.size(lista)
    if size > 10:
        print("\nLos primeros ", str(10),
              " paises ordenados por su número de obras son: ")
        i = 1
        while i <= 10:
            nacionalidades = lt.getElement(lista, i)
            nacionalidad = nacionalidades['Nationality']
            conteo = nacionalidades['conteo']
            print(str(i)+"." + nacionalidad + ': ' + str(conteo))
            i += 1


def printPrimeras3ObrasNacionalidad(lista):
    primeraNacionalidad = lt.getElement(lista, 1)
    print('\nEn el primer lugar se encuentra la nacionalidad '+primeraNacionalidad['Nationality']+' con un total de ' +
          str(primeraNacionalidad['conteo'])+' obras.')
    i = 1
    while i <= 3:
        obra = lt.getElement(primeraNacionalidad['obrasyArtistas'], i)
        titulo = obra['Title']
        fecha = obra['Date']
        medio = obra['Medium']
        dimensiones = obra['Dimensions']
        cadenaArtista = ''
        for artistas in lt.iterator(obra['artists']):
            artista = artistas['DisplayName']
            if cadenaArtista == "":
                cadenaArtista += artista
            else:
                cadenaArtista += ", "+artista
        print(str(i)+'. '+"Titulo: " + titulo + ", Artista(s): " + cadenaArtista + ", Fecha: "
              + fecha + ", Medio: " + medio
              + ", Dimensiones: " + dimensiones)
        i += 1
    print('...')


def printUltimas3obrasNacionalidad(lista):
    primeraNacionalidad = lt.getElement(lista, 1)
    size = lt.size(primeraNacionalidad['obrasyArtistas'])
    i = size-2
    while i <= size:
        obra = lt.getElement(primeraNacionalidad['obrasyArtistas'], i)
        titulo = obra['Title']
        fecha = obra['Date']
        medio = obra['Medium']
        dimensiones = obra['Dimensions']
        cadenaArtista = ''
        for artistas in lt.iterator(obra['artists']):
            artista = artistas['DisplayName']
            if cadenaArtista == "":
                cadenaArtista += artista
            else:
                cadenaArtista += ", "+artista
        print(str(i)+'. '+"Titulo: " + titulo + ", Artista(s): " + cadenaArtista + ", Fecha: "
              + fecha + ", Medio: " + medio
              + ", Dimensiones: " + dimensiones)
        i += 1


catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        estructura = input('Seleccione el tipo de repersentación de lista\n' +
                           '"A" para ARRAY_LIST o "L" para LINKED LIST : ')
        print("Cargando información de los archivos ....")
        catalog = initCatalog(estructura)
        loadData(catalog)
        print('Artistas cargados: ' + str(lt.size(catalog['artists'])))
        print('Artworks cargados: ' + str(lt.size(catalog['artworks'])))
        print('Artistas finales: '+str(lt.getElement(((catalog['artists'])), lt.size(catalog['artists']))) +
              str(lt.getElement(((catalog['artists'])), int(lt.size(catalog['artists']))-1)) +
              str(lt.getElement(((catalog['artists'])), int(lt.size(catalog['artists']))-2)))

        print('Artworks finales: '+str(lt.getElement(((catalog['artworks'])), lt.size(catalog['artworks']))) +
              str(lt.getElement(((catalog['artworks'])), int(lt.size(catalog['artworks']))-1)) +
              str(lt.getElement(((catalog['artworks'])), int(lt.size(catalog['artworks']))-2)))

        """print('Artista: '+str(lt.getElement(((catalog['artists'])), int(lt.size(catalog['artists'])-1))))
        print('Artista: '+str(lt.getElement(((catalog['artists'])), int(lt.size(catalog['artists'])-2))))"""

        """for artist in lt.iterator(catalog['artists']):
            print('Artista: ' + artist['DisplayName'] +
                    '  Biografia: ' + artist['ArtistBio'])"""

    elif int(inputs[0]) == 2:
        anho_inicial = input("\nIngrese el año incial: ")
        anho_final = input("Ingrese el año final: ")
        '''alogritmo = input('Seleccione el tipo de Algoritmo \n'
                          + '"I" para Insertion, "S" para Shell, "M" para Merge o'
                          + '"Q" para Quick sort: ')'''
        resultado = controller.sortArtist(
            catalog, anho_inicial, anho_final)
        print("\nEl número de Artistas nacidos entre " + anho_inicial + " y " + anho_final
              + " es: " + str(resultado[2]))
        printPrimeros3Artistas(resultado[1], resultado[2])
        ultimos3Artistas(resultado[1], resultado[2])

    elif int(inputs[0]) == 3:
        anho_inicial = input("\nIngrese la fecha inicial (AAAA-MM-DD): ")
        anho_final = input("Ingrese la fecha final(AAAA-MM-DD): ")
        '''alogritmo = input('Seleccione el tipo de Algoritmo \n'
                          + '"I" para Insertion, "S" para Shell, "M" para Merge o'
                          + '"Q" para Quick sort: ')'''
        resultado = controller.sortArtwork(
            catalog, anho_inicial, anho_final)
        print('\nNúmero total de obras en el rango: ' + str(resultado[2]))
        print('Número total de compras: '+str(resultado[3]))
        printprimeros3artistasyobras(resultado[1], resultado[2])
        printUltimos3ArtistasyObras(resultado[1], resultado[2])

    elif int(inputs[0]) == 4:
        nombre_artista = input('\nIngrese el nombre del artista: ')
        resultado = (controller.obrasPorTecnica(catalog, nombre_artista))
        print('\nTotal de obras: '+str(resultado[0]))
        print('Total de tecnicas: '+str(resultado[1]))
        print('Tecnica mas utilizada: '+str(resultado[2]))
        print('Listado de obras de la tecnica mas utilizada: ' +
              str(resultado[3]))

    elif int(inputs[0]) == 5:
        '''alogritmo = input('Seleccione el tipo de Algoritmo \n'
                          + '"I" para Insertion, "S" para Shell, "M" para Merge o'
                          + '"Q" para Quick sort: ')'''
        resultado = controller.obrasPorNacionalidad(catalog)
        printTOP10(resultado)
        printPrimeras3ObrasNacionalidad(resultado)
        printUltimas3obrasNacionalidad(resultado)

    elif int(inputs[0]) == 6:
        depto = input('\nIngrese el departamento: ')
        algoritmo = input('Ingrese el algoritmo: ')
        resultado = (controller.transportarObras(catalog, depto, algoritmo))
        print('Total de obras a transportar: '+str(resultado[0]))
        print('Precio estimado del servicio USD: '+str(resultado[1]))
        print('Peso estimado de las obras: '+str(resultado[2]))
        print('Tiempo de ejecucion: ' + str(resultado[3]))

    else:
        sys.exit(0)
sys.exit(0)
