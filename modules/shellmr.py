#!/usr/bin/env python

"""shellmr.py: importa modulos y ejecuta sentencias para trabajar con datos en ipython3."""

__author__ = "Marco Redondo"
__email__ = "redondomarco@gmail.com"
__status__ = "Devel"

import numpy as np
import pandas as pd
import folium
from folium import plugins
from folium.plugins import HeatMap

from geomr import location_rosario, projmr_to_latlon
from pandasmr import clasifico_por_dia
