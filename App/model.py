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


from os import times
import config as cf
from DISClib.ADT import list as lt
import time
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as si
from DISClib.Algorithms.Sorting import mergesort as sm
from DISClib.Algorithms.Sorting import quicksort as sq
from datetime import datetime
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
# Construccion de modelos


def newCatalog(estructura):
    catalog = {'artworks': None,
               'artists': None}
    
    if estructura == "A":
        catalog['artworks'] = lt.newList()
        catalog['artists'] = lt.newList('ARRAY_LIST')
    
    elif estructura == "L":
        catalog['artworks'] = lt.newList()
        catalog['artists'] = lt.newList('SNGLE_LIST')
                                    
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

'''def requerimiento_1(catalog,anho_inicial,anho_final):
    artistas=catalog['artists']
    artistas_rango=lt.newlist()
    for artista in artistas:
        nacimiento=artista['BeginDate']
        if nacimiento>=anho_inicial and nacimiento<=anho_final:'''
            
# Funciones utilizadas para comparar elementos dentro de una lista
def cmpArtworkByDateAcquired(artwork1, artwork2):
    fecha_artwork1=str(artwork1['DateAcquired'])
    fecha_artwork2=str(artwork2['DateAcquired'])
    if len(fecha_artwork1)<10:
        fecha_artwork1=str(datetime.today())
    if len(fecha_artwork2)<10:  
        fecha_artwork2=str(datetime.today())

    anho_artwork1=float(fecha_artwork1[:4])
    mes_artwork1=float(fecha_artwork1[5:7])
    dia_artwork1=float(fecha_artwork1[8:10])
    anho_artwork2=float(fecha_artwork2[:4])
    mes_artwork2=float(fecha_artwork2[5:7])
    dia_artwork2=float(fecha_artwork2[8:10])
    if fecha_artwork1==fecha_artwork2:
        return 0
    elif anho_artwork1<anho_artwork2:
        return 1
    elif anho_artwork1>anho_artwork2:
        return 0
    elif anho_artwork1==anho_artwork2:
        if mes_artwork1<mes_artwork2:
            return 1
        elif mes_artwork1>mes_artwork2:
            return 0
        elif dia_artwork1==mes_artwork2:
            if dia_artwork1<dia_artwork2:
                return 1
            elif dia_artwork1>dia_artwork2:
                return 0




# Funciones de ordenamiento

def sortArtwork(catalog, muestra, algoritmo):
    sub_list=lt.subList(catalog['artworks'],1,muestra)
    sub_list=sub_list.copy()
    if algoritmo == "I":
        start_time = time.process_time()
        sorted_list=si.sort(sub_list,cmpArtworkByDateAcquired)
        stop_time = time.process_time()
        elapsed_time_mseg=(stop_time - start_time)*1000
    elif algoritmo=="S":
        start_time=time.process_time()
        sorted_list=sa.sort(sub_list,cmpArtworkByDateAcquired)
        stop_time=time.process_time
        elapsed_time_mseg=(stop_time - start_time)*1000
    elif algoritmo == "M":
        start_time=time.process_time()
        sorted_list=sm.sort(sub_list,cmpArtworkByDateAcquired)
        stop_time=time.process_time
        elapsed_time_mseg=(stop_time - start_time)*1000
    elif algoritmo == "Q":
        start_time=time.process_time()
        sorted_list=sq.sort(sub_list,cmpArtworkByDateAcquired)
        stop_time=time.process_time()
        elapsed_time_mseg=(stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list

