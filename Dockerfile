FROM jupyterhub/jupyterhub

RUN adduser --disabled-password --gecos "" jupyter --home /srv/jupyterhub

RUN echo jupyter:jupyter | chpasswd jupyter

RUN pip install notebook pandas odfpy geopandas geopy folium pyproj numpy

RUN chown -R jupyter:jupyter /srv/jupyterhub