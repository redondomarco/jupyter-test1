Fuente:

https://docs.docker.com/engine/install/ubuntu/



Uninstall old versions

```
sudo apt-get remove docker docker-engine docker.io containerd runc
```


Instalo paquetes previos necesarios:

```
sudo apt-get update
```

```
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```

Instalo llave gpg y fuente:

```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

```
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```


Instalo paquetes

```
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io

```

Agrego grupo y permisos para ejecutar comandos docker con mi usuario

```
sudo groupadd docker

sudo service docker restart

```

```
sudo usermod -a -G docker $TUSUARIO
```
