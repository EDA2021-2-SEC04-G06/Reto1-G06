
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

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Catalogo cronologico de los artistas")
    print("3- Obras de artista por tecnica")
    print("4- Obras segun nacionalidad del creador")
    print("5- Calcular costo de transportar todas las obras de un departamento")
    print("6- Reglas de transporte")
    print("7- Proponer nueva exposicion en el museo")


def initCatalog():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog()


def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)


catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print('Artistas cargados: ' + str(lt.size(catalog['artworks'])))
        print('Artworks cargados: ' + str(lt.size(catalog['artists'])))

        print('Artistas finales: '+str(lt.getElement(((catalog['artists'])), lt.size(catalog['artists'])))+
                str(lt.getElement(((catalog['artists'])), int(lt.size(catalog['artists']))-1))+
                str(lt.getElement(((catalog['artists'])), int(lt.size(catalog['artists']))-2)))

        print('Artworks finales: '+str(lt.getElement(((catalog['artworks'])), lt.size(catalog['artworks'])))+
                str(lt.getElement(((catalog['artworks'])), int(lt.size(catalog['artworks']))-1))+
                str(lt.getElement(((catalog['artworks'])), int(lt.size(catalog['artworks']))-2)))

        """print('Artista: '+str(lt.getElement(((catalog['artists'])), int(lt.size(catalog['artists'])-1))))
        print('Artista: '+str(lt.getElement(((catalog['artists'])), int(lt.size(catalog['artists'])-2))))"""

        """for artist in lt.iterator(catalog['artists']):
            print('Artista: ' + artist['DisplayName'] +
                    '  Biografia: ' + artist['ArtistBio'])"""

    elif int(inputs[0]) == 2:
        pass

    else:
        sys.exit(0)
sys.exit(0)

