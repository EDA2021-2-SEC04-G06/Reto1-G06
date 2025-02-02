﻿"""
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


from DISClib.DataStructures.arraylist import subList
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
               'artists': None,
               'obrasPorArtistas': None,
               'artistasPorObras': None,
               'nacionalidades': None}

    if estructura == "A":
        catalog['artworks'] = lt.newList()
        catalog['artists'] = lt.newList('ARRAY_LIST')
        catalog['obrasPorArtistas'] = lt.newList(
            'ARRAY_LIST', cmpfunction=cmpConstituentID)
        catalog['artistasPorObras'] = lt.newList(
            "ARRAY_LIST", cmpfunction=cmpConstituentID)
        catalog['nacionalidades'] = lt.newList(
            'ARRAY_LIST', cmpfunction=cmpNacionalidad)

    elif estructura == "L":
        catalog['artworks'] = lt.newList()
        catalog['artists'] = lt.newList('SNGLE_LINKED')
        catalog['obrasPorArtistas'] = lt.newList(
            'SINGLE_LINKED', cmpfunction=cmpConstituentID)
        catalog['artistasPorObras'] = lt.newList(
            "SINGLE_LINKED", cmpfunction=cmpConstituentID)
        catalog['nacionalidades'] = lt.newList(
            'SINGLE_LINKED', cmpfunction=cmpNacionalidad)

    return catalog
# Funciones para agregar informacion al catalogo


def addArtworks(catalog, artwork):
    lt.addLast(catalog['artworks'], artwork)
    artwork = newArtwork(artwork['ConstituentID'], artwork['Title'], artwork["Date"], artwork["Medium"], artwork["Dimensions"],
                         artwork['CreditLine'], artwork['Classification'], artwork['Department'], artwork['DateAcquired'],
                         artwork['ObjectID'], artwork['Diameter (cm)'], artwork['Height (cm)'], artwork['Length (cm)'],
                         artwork['Weight (kg)'], artwork['Width (cm)'], artwork["Seat Height (cm)"])
    lt.addLast(catalog['artistasPorObras'], artwork)


def addArtists(catalog, artist):
    lt.addLast(catalog['artists'], artist)
    artist = newArtist(artist['ConstituentID'], artist['DisplayName'], artist['Nationality'], artist['Gender'],
                       artist['BeginDate'], artist['EndDate'])
    lt.addLast(catalog['obrasPorArtistas'], artist)


def addObrasPorArtistas(catalog):
    for obras in lt.iterator(catalog['artworks']):
        artistas = str(obras['ConstituentID'])
        artistas = artistas[1:len(artistas)-1]
        artistas = artistas.split()
        for artista in artistas:
            addObraArtista(catalog, artista.strip(), obras)


def addObraArtista(catalog, constituentid, obras):
    artistas = catalog['obrasPorArtistas']
    posartista = lt.isPresent(artistas, constituentid)
    if posartista > 0:
        artista = lt.getElement(artistas, posartista)
    else:
        artista = newArtist2(constituentid)
        lt.addLast(artistas, artista)
    lt.addLast(artista['artworks'], obras)


def addArtistasPorObras(catalog):
    for artista in lt.iterator(catalog['artists']):
        constituentid = str(artista['ConstituentID'])
        addArtistaObra(catalog, constituentid, artista)


def addArtistaObra(catalog, constituentid, artista):
    obras = catalog['artistasPorObras']
    posartista = lt.isPresent(obras, constituentid)
    if posartista > 0:
        artwork = lt.getElement(obras, posartista)
        lt.addLast(artwork['artists'], artista)


def addNacionalidades(catalog):
    for obra in lt.iterator(catalog['artistasPorObras']):
        for artista in lt.iterator(obra['artists']):
            nacionalidad = str(artista['Nationality'])
            if nacionalidad == '':
                nacionalidad = 'Nationality unknown'
            addNationality(catalog, nacionalidad, obra)


def addNationality(catalog, nacionalidad, obra):
    nacionalidades = catalog['nacionalidades']
    posnacionalidad = lt.isPresent(nacionalidades, nacionalidad)
    if posnacionalidad > 0:
        nacionalidad2 = lt.getElement(nacionalidades, posnacionalidad)
        lt.addLast(nacionalidad2['obrasyArtistas'], obra)
        nacionalidad2['conteo'] = nacionalidad2['conteo']+1
    else:
        nacionalidad2 = newNationality(nacionalidad)
        lt.addLast(nacionalidades, nacionalidad2)
        lt.addLast(nacionalidad2['obrasyArtistas'], obra)

# Funciones para creacion de datos


def newArtwork(constituentid, title, date, medium, dimensions, creditline, classification, department, dateacqu, objectid,
               diam, height, length, weight, width, seat):
    artwork = {'ConstituentID': "", 'Title': "", "Date": "", "Medium": "", "Dimensions": "",
               'CreditLine': "", 'Classification': "", "Department": "", 'DateAcquired': "",
               'ObjectId': "", 'Diameter (cm)': "", 'Height (cm)': "", 'Lenght (cm)': "",
               'Weight (kg)': "", 'Width (cm)': "", "Seat Height (cm)": "", 'artists': {}}
    artwork['ConstituentID'] = constituentid
    artwork['Title'] = title
    artwork['Date'] = date
    artwork['Medium'] = medium
    artwork['Dimensions'] = dimensions
    artwork['CreditLine'] = creditline
    artwork['Classification'] = classification
    artwork['Department'] = department
    artwork['DateAcquired'] = dateacqu
    artwork['ObjectId'] = objectid
    artwork['Diameter (cm)'] = diam
    artwork['Height (cm)'] = height
    artwork['Lenght (cm)'] = length
    artwork['Weight (kg)'] = weight
    artwork['Width (cm)'] = width
    artwork['Seat Height (cm)'] = seat
    artwork['artists'] = lt.newList("ARRAY_LIST")
    return artwork


def newArtist(constituentid, displayname, nationality, gender, begindate, enddate):
    artist = {'ConstituentID': "", 'DisplayName': "", 'Nationality': "", 'Gender': "", 'BeginDate': "", "EndDate": "",
              "artworks": {}}
    artist['ConstituentID'] = constituentid
    artist['DisplayName'] = displayname
    artist['Nationality'] = nationality
    artist['Gender'] = gender
    artist['BeginDate'] = begindate
    artist['EndDate'] = enddate
    artist['artworks'] = lt.newList("ARRAY_LIST")

    return artist


def newArtist2(constituentid):
    artist = {'ConstituentID': "", 'DisplayName': "", 'Nationality': "", 'Gender': "", 'BeginDate': "", "EndDate": "",
              "artworks": {}}
    artist['ConstituentID'] = constituentid
    artist['artworks'] = lt.newList("ARRAY_LIST")
    return artist


def newNationality(nacionalidad):
    nacionalidadAgregar = {'Nationality': "",
                           'conteo': 1, 'obrasyArtistas': {}}
    nacionalidadAgregar['Nationality'] = nacionalidad
    nacionalidadAgregar['obrasyArtistas'] = lt.newList('ARRAY_LIST')
    return nacionalidadAgregar

# Funciones utilizadas para comparar elementos dentro de una lista


def cmpConstituentID(id1, lista):
    if id1 in str(lista['ConstituentID']):
        return 0
    return -1


def cmpNacionalidad(nacionalidad1, lista):
    if nacionalidad1 == str(lista['Nationality']):
        return 0
    return 1


def cmpArtistByBeginDate(artist1, artist2):
    fecha_artist1 = int(artist1['BeginDate'])
    fecha_artist2 = int(artist2['BeginDate'])
    if fecha_artist1 < fecha_artist2:
        return 1
    else:
        return 0


def cmpArtworkByDateAcquired(artwork1, artwork2):
    fecha_artwork1 = str(artwork1['DateAcquired'])
    fecha_artwork2 = str(artwork2['DateAcquired'])
    if len(fecha_artwork1) != 10:
        fecha_artwork1 = str(datetime.today())
    if len(fecha_artwork2) != 10:
        fecha_artwork2 = str(datetime.today())

    anho_artwork1 = float(fecha_artwork1[:4])
    mes_artwork1 = float(fecha_artwork1[5:7])
    dia_artwork1 = float(fecha_artwork1[8:10])
    anho_artwork2 = float(fecha_artwork2[:4])
    mes_artwork2 = float(fecha_artwork2[5:7])
    dia_artwork2 = float(fecha_artwork2[8:10])
    if fecha_artwork1 == fecha_artwork2:
        return 0
    elif anho_artwork1 < anho_artwork2:
        return 1
    elif anho_artwork1 > anho_artwork2:
        return 0
    elif anho_artwork1 == anho_artwork2:
        if mes_artwork1 < mes_artwork2:
            return 1
        elif mes_artwork1 > mes_artwork2:
            return 0
        elif dia_artwork1 == mes_artwork2:
            if dia_artwork1 < dia_artwork2:
                return 1
            elif dia_artwork1 > dia_artwork2:
                return 0


def cmpObrasNacionalidad(nacionalidad1, nacionalidad2):
    conteo1 = nacionalidad1['conteo']
    conteo2 = nacionalidad2['conteo']
    if conteo1 > conteo2:
        return 1
    else:
        return 0

# Funciones de ordenamiento


def sortArtwork(catalog, fecha_inicial, fecha_final):
    sub_list = catalog['artistasPorObras'].copy()
    final_lista = int(lt.size(sub_list))
    '''if algoritmo == "I":
        start_time = time.process_time()
        sorted_list = si.sort(sub_list, cmpArtworkByDateAcquired)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time) * 1000
    elif algoritmo == "S":
        start_time = time.process_time()
        sorted_list = sa.sort(sub_list, cmpArtworkByDateAcquired)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time) * 1000
    elif algoritmo == "M":
        start_time = time.process_time()
        sorted_list = sm.sort(sub_list, cmpArtworkByDateAcquired)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time) * 1000
    elif algoritmo == "Q":
        start_time = time.process_time()
        sorted_list = sq.sort(sub_list, cmpArtworkByDateAcquired)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time) * 1000'''

    start_time = time.process_time()
    sorted_list = sm.sort(sub_list, cmpArtworkByDateAcquired)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time) * 1000

    i = 1
    while i <= final_lista:
        obra = lt.getElement(sorted_list, i)
        fecha_adquirda = obra['DateAcquired']
        if len(fecha_adquirda) == 10:
            anho_adquirido = float(fecha_adquirda[0:4])
            mes_adquirido = float(fecha_adquirda[5:7])
            dia_adquirido = float(fecha_adquirda[8:10])
            anho_inicial = float(fecha_inicial[0:4])
            mes_inicial = float(fecha_inicial[5:7])
            dia_inicial = float(fecha_inicial[8:10])
            if anho_adquirido > anho_inicial:
                pos_inicial = i
                i += final_lista
            elif anho_adquirido == anho_inicial:
                if mes_adquirido > mes_inicial:
                    pos_inicial = i
                    i += final_lista
                elif mes_adquirido == mes_inicial:
                    if dia_adquirido >= dia_inicial:
                        pos_inicial = i
                        i += final_lista
        i += 1

    j = 1
    while j <= final_lista:
        obra = lt.getElement(sorted_list, j)
        fecha_adquirda = obra['DateAcquired']
        if len(fecha_adquirda) == 10:
            anho_adquirido = float(fecha_adquirda[0:4])
            mes_adquirido = float(fecha_adquirda[5:7])
            dia_adquirido = float(fecha_adquirda[8:10])
            anho_final = float(fecha_final[0:4])
            mes_final = float(fecha_final[5:7])
            dia_final = float(fecha_final[8:10])
            if anho_adquirido < anho_final:
                pos_final = j
            elif anho_adquirido == anho_final:
                if mes_adquirido < mes_final:
                    pos_final = j
                elif mes_adquirido == mes_final:
                    if dia_adquirido <= dia_final:
                        pos_final = j
        j += 1

    sorted_list2 = lt.subList(
        sorted_list, pos_inicial, pos_final-pos_inicial+1)

    contador = 0

    for obra in lt.iterator(sorted_list2):
        tipoCompra = obra['CreditLine']
        if "Purchase" in tipoCompra:
            contador += 1
        elif 'purchase' in tipoCompra:
            contador += 1

    tamanhoSortedList2 = lt.size(sorted_list2)

    return elapsed_time_mseg, sorted_list2, tamanhoSortedList2, contador


def sortArtist(catalog, anho_inicial, anho_final):
    sub_list = catalog['artists'].copy()
    final_lista = int(lt.size(sub_list))
    '''if algoritmo == "I":
        start_time = time.process_time()
        sorted_list = si.sort(sub_list, cmpArtistByBeginDate)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time) * 1000
    elif algoritmo == "S":
        start_time = time.process_time()
        sorted_list = sa.sort(sub_list, cmpArtistByBeginDate)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time) * 1000'''
    '''elif algoritmo == "M":
        start_time = time.process_time()
        sorted_list = sm.sort(sub_list, cmpArtistByBeginDate)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time) * 1000'''
    '''elif algoritmo == "Q":
        start_time = time.process_time()
        sorted_list = sq.sort(sub_list, cmpArtistByBeginDate)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time) * 1000'''

    start_time = time.process_time()
    sorted_list = sm.sort(sub_list, cmpArtistByBeginDate)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time) * 1000

    i = 1
    while i <= final_lista:
        artista = lt.getElement(sorted_list, i)
        fecha_nacimiento = int(artista['BeginDate'])
        if fecha_nacimiento >= int(anho_inicial):
            pos_inicial = i
            i += final_lista
        i += 1

    j = 1
    while j <= final_lista:
        artista = lt.getElement(sorted_list, j)
        fecha_nacimiento = int(artista['BeginDate'])
        if fecha_nacimiento <= int(anho_final):
            pos_final = j
        j += 1

    sorted_list_2 = lt.subList(
        sorted_list, pos_inicial, pos_final-pos_inicial+1)

    tamanhoSortedList2 = lt.size(sorted_list_2)

    return elapsed_time_mseg, sorted_list_2, tamanhoSortedList2


def mayorConteo(sub_list):
    '''if algoritmo == "I":
        start_time = time.process_time()
        sorted_list = si.sort(sub_list, cmpObrasNacionalidad)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time) * 1000
    elif algoritmo == "S":
        start_time = time.process_time()
        sorted_list = sa.sort(sub_list, cmpObrasNacionalidad)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time) * 1000
    elif algoritmo == "M":
        start_time = time.process_time()
        sorted_list = sm.sort(sub_list, cmpObrasNacionalidad)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time) * 1000
    elif algoritmo == "Q":
        start_time = time.process_time()
        sorted_list = sq.sort(sub_list, cmpObrasNacionalidad)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time) * 1000'''

    start_time = time.process_time()
    sorted_list = sm.sort(sub_list, cmpObrasNacionalidad)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time) * 1000

    return elapsed_time_mseg, sorted_list


# Funciones de consulta


def obrasPorTecnica(catalog, nombre):
    sub_list = catalog['artists'].copy()
    listaArtists = sub_list['elements']
    sub_list2 = catalog['obrasPorArtistas'].copy()
    listaArtworks = sub_list2['elements']
    id = ''
    totalObras = 0
    totalTecnicaslist = []
    totalTecnicas = 0
    tecnicaMasUsada = ''
    obrasTecnicaMasUsada = []
    tecnica = ''

    for each in listaArtists:
        if each['DisplayName'] == nombre:
            id = each['ConstituentID']

    for each in listaArtworks:
        if each['ConstituentID'] == id:
            lista = each['artworks']
            artworks = lista['elements']
            for cadaObra in artworks:
                totalObras += 1
                tecnica = cadaObra['Medium']
                if tecnica not in totalTecnicaslist:
                    totalTecnicas += 1
                totalTecnicaslist.append(tecnica)

    tecnicaMasUsada = max(set(totalTecnicaslist), key=totalTecnicaslist.count)
    for obras in artworks:
        if obras['Medium'] == tecnicaMasUsada:
            info = {'Titulo': obras['Title'],
                    'Fecha': obras['Date'],
                    'Medio': obras['Medium'],
                    'Dimensiones': obras['Dimensions']}
            obrasTecnicaMasUsada.append(info)

    return totalObras, totalTecnicas, tecnicaMasUsada, obrasTecnicaMasUsada


def obrasPorNacionalidad(catalog):
    subList = catalog['nacionalidades'].copy()
    sortedList = mayorConteo(subList)

    return sortedList[1]


def transportarObras(catalog, depto, algoritmo):
    sub_list2 = catalog['artistasPorObras'].copy()

    if algoritmo == "I":
        start_time = time.process_time()
        lista = si.sort(sub_list2, cmpArtworkByDateAcquired)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time) * 1000
    elif algoritmo == "S":
        start_time = time.process_time()
        lista = sa.sort(sub_list2, cmpArtworkByDateAcquired)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time) * 1000
    elif algoritmo == "M":
        start_time = time.process_time()
        lista = sm.sort(sub_list2, cmpArtworkByDateAcquired)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time) * 1000
    elif algoritmo == "Q":
        start_time = time.process_time()
        lista = sq.sort(sub_list2, cmpArtworkByDateAcquired)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time) * 1000

    listaArtworks = lista['elements']

    totalObras = 0
    costoTotal = 0
    pesoTotal = 0
    for obra in listaArtworks:

        if depto == obra['Department']:
            totalObras += 1
            #h = obra['Height (cm)']
            if obra['Height (cm)'] != '':
                if obra['Width (cm)'] != '':
                    if float(obra['Height (cm)']) > 0:
                        if float(obra['Width (cm)']) > 0:
                            cm_a_metro_h = float(obra['Height (cm)']) / 100
                            cm_a_metro_w = float(obra['Width (cm)']) / 100
                            costoObra = 72.00 / (cm_a_metro_h * cm_a_metro_w)

            if obra['Width (cm)'] == '':
                if obra['Height (cm)'] == '':
                    if obra['Weight (kg)'] != '':
                        if float(obra['Weight (kg)'] > 0):
                            costoObra = 72.00 / float(obra['Weight (kg)'])
                            pesoTotal += float(obra['Weight (kg)'])

            else:
                costoObra = 48.00

            costoTotal += costoObra

    return totalObras, costoTotal, pesoTotal, elapsed_time_mseg
