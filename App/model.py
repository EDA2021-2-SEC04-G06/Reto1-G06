"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
# Construccion de modelos


def newCatalog():
    catalog = {'artworks': None,
               'artists': None}

    catalog['artworks'] = lt.newList()
    catalog['artists'] = lt.newList('ARRAY_LIST',
                                    cmpfunction=compareauthors)

    return catalog

# Funciones para agregar informacion al catalogo


def addArtworks(catalog, artwork):
    lt.addLast(catalog['artworks'], artwork)

    """constitutent_ids = artwork['ConstituentID'].split(",")
    for constitutentid in constitutent_ids:
        addArtworkArtist(catalog, constitutentid.strip(), artwork)
def addArtworkArtist(catalog, constitutentid, artwork):
    constitutent_id_lista = catalog['artists']
    posterior_id = lt.isPresent(constitutent_id_lista, constitutentid)
    if posterior_id > 0:
        constitutent_id_agregar = lt.getElement(constitutent_id_lista, posterior_id)
    else:
        constitutent_id_agregar = newArtista(constitutentid)
        lt.addLast(constitutent_id_lista, constitutent_id_agregar)
    lt.addLast(constitutent_id_agregar['artworks'], artwork)"""


def addArtists(catalog, artist):
    lt.addLast(catalog['artists'], artist)


# Funciones para creacion de datos

def newArtista(constitutentid):
    datos_artista = {'ConstituentID': "", 'DisplayName': None, 'ArtistBio': None, 'Nationality': None,
                     'Gender': None, 'BeginDate': None, 'EndDate': None, 'Wiki QID': None, 'ULAN': None,
                     'artworks': None}
    datos_artista['ConstituentID'] = constitutentid
    datos_artista['artworks'] = lt.newList('ARRAY_LIST')
    return datos_artista


# Funciones de consulta

def getLastArtists(catalog, number):
    """
    Retorna los ultimos artistas
    """
    artistas = catalog['artists']
    lastArtists = lt.newList()
    for cont in range(1, number+1):
        artist = lt.getElement(artistas, cont)
        lt.addLast(lastArtists, artist)
    return lastArtists

# Funciones utilizadas para comparar elementos dentro de una lista


def compareauthors(authorname1, author):
    if (authorname1.lower() in author['name'].lower()):
        return 0
    return -1

# Funciones de ordenamiento
