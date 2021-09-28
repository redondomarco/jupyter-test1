#!/usr/bin/env python

"""Foobar.py: Description of what foobar does."""

__author__ = "Marco Redondo"
__email__ = "redondomarco@gmail.com"
__status__ = "Devel"

import pyproj
from geopy.geocoders import Nominatim

# https://datosabiertos.rosario.gob.ar/dataset/parcelas-formato-csv

def projmr_to_latlon(x1, y1):
    """transforma coordenadas usados en sistemas de proyeccion de MR(x,y)
    en (latitud, longitud)"""
    proj = pyproj.Transformer.from_crs(22185, 4326, always_xy=True)
    x2, y2 = proj.transform(x1, y1)
    # devuelvo tupla(latitud, longitud) absoluta
    return (y2, x2)


def location_rosario():
    """devuelve location de la ciudad de Rosario (latitud,longitud)"""
    locator = Nominatim(user_agent="myGeocoder")
    location = locator.geocode("Rosario, Santa Fe, Argentina")
    return (location.latitude, location.longitude)