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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros


def initCatalog(estructura):
    catalog = model.newCatalog(estructura)
    return catalog

# Funciones para la carga de datos


def loadData(catalog):
    loadArtworks(catalog)
    loadArtists(catalog)
    loadObrasPorArtistas(catalog)
    loadArtistasPorObras(catalog)
    loadnacionalidades(catalog)


def loadArtists(catalog):
    artistsfile = cf.data_dir + 'Artists-utf8-10pct.csv'
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtists(catalog, artist)


def loadArtworks(catalog):
    artworksfile = cf.data_dir + 'Artworks-utf8-10pct.csv'
    input_file = csv.DictReader(open(artworksfile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtworks(catalog, artwork)


def loadObrasPorArtistas(catalog):
    model.addObrasPorArtistas(catalog)


def loadArtistasPorObras(catalog):
    model.addArtistasPorObras(catalog)


def loadnacionalidades(catalog):
    model.addNacionalidades(catalog)

# Funciones de ordenamiento


def sortArtwork(catalog, anho_inicial, anho_final):
    return model.sortArtwork(catalog, anho_inicial, anho_final)


def sortArtist(catalog, anho_inicial, anho_final):
    artistas_rango = model.sortArtist(
        catalog, anho_inicial, anho_final)
    return artistas_rango

# Funciones de consulta sobre el catálogo


def getLastArtists(catalog, number):
    """
    Retorna los ultimos artistas
    """
    lastArtists = model.getLastArtists(catalog, number)
    return lastArtists


def obrasPorTecnica(catalog, nombre):
    id1 = model.obrasPorTecnica(catalog, nombre)
    return id1


def obrasPorNacionalidad(catalog):
    obrasnacionalidad = model.obrasPorNacionalidad(catalog)
    return


def transportarObras(catalog, depto, algoritmo):
    costo = model.transportarObras(catalog, depto, algoritmo)
    return costo
