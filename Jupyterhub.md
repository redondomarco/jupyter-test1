https://hub.docker.com/r/jupyterhub/singleuser



https://hub.docker.com/r/jupyterhub/jupyterhub



Instalacion en localhost

```
docker run -p 8000:8000 -d --name jupyterhub jupyterhub/jupyterhub jupyterhub
```

Para entrar en la consola del contenedor en ejecucion

```
docker exec -it jupyterhub bash
```

Para controlar el estado del contenedor

docker stop jupyterhub

docker start jupyterhub

docker restart jupyterhub

docker ps



(Necesario) Dentro del contenedor instalar:

pip install notebook


