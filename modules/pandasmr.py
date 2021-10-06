#!/usr/bin/env python

"""pandasmr.py: operatoria con pandas dataframes."""

__author__ = "Marco Redondo"
__email__ = "redondomarco@gmail.com"
__status__ = "Devel"

import pandas as pd
from geomr import projmr_to_latlon
from collections import defaultdict, OrderedDict

def reclamos_sua_heatmap(file):
    df_acc = pd.read_excel(file, engine='odf')


def clasifico_por_dia(df):
    data = {}
    for row in df.itertuples():
        time_index = row._8.strftime('%Y-%m-%d')
        lat_long = list(projmr_to_latlon(row._17, row._18))
        data.setdefault(time_index, []).append(lat_long)
    resultado = OrderedDict(sorted(data.items(), key=lambda t: t[0]))
    return resultado
