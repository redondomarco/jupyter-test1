# Jupyter

Previamente se requiere instalar docker

https://gitlab.rosario.gob.ar/dgi/jupyter/-/blob/main/Docker.md

y algunas dependencias

```bash
apt install git make
```

Para instalar el proyecto

```bash
git clone https://gitlab.rosario.gob.ar/dgi/jupyter.git

cd jupyter

make install

```

Luego para controlar el estado del contenedor

```bash
make [ start | stop | restart ]
```

Util:

```bash
make ipython3
```

corre la consola interactiva de python dentro del contenedor, con el mismo acceso a modulos y archivos
























