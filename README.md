# Coding Challenge

El problema de las n-reinas creando un entorno de desarrollo usando python3, sqlalchemy, pytest y docker.
Esta implementación en python con base en el algoritmo propuesto por Martin Richards, ref: (http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.51.7113&rep=rep1&type=pdf). El algoritmo es muy eficiente porque implementa el uso de los operadores bitwise. Tambien se tomo como referencia el siguiente blog post: (http://gregtrowbridge.com/a-bitwise-solution-to-the-n-queens-problem-in-javascript/).
Esta solucion resuelve el ejercicio para n>= 8 hasta 15. El ejercicio de prueba esta con 8 y 9.


## Getting Started

El proyecto cuenta con una configuración en Travis CI, puedes descargarlo del siguiente repositorio: (https://github.com/Gleekzone/Test) y agregarlo a tu GitHub para ejecutarlo con Travis. 
Si deseas probarlo en tu maquina local solo necesitas docker y docker-compose.

### Prerequisites

###Para instalar docker 

```
$ apt-get update
``` 

```
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

```
$ add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" 
``` 

```
$ apt-get update 
``` 
```
$ apt-cache policy docker-ce
``` 

```
$ apt-get install docker-ce
```

```
$ newgrp docker
```

###Para instalar docker-compose

```
$ sudo curl -L https://github.com/docker/compose/releases/download/1.22.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
```
```
$ sudo chmod +x /usr/local/bin/docker-compose
```
### Installing

### docker
Crear imagenes

```
$ docker build -t name-app .
```

Entrar el contenedor
```
$ docker run --name name-app -it --rm name-app
```

Ejecutar python del contenedor y lo borra
```
$ docker run --name name-app -it --rm name-app python3 test.py
```

Ver el log del test
```
$ docker logs name-app-test
```
# DOCKER COMPOSE

Crear imagenes
```
$ docker-compose build
```

Ejecutar contenedores
```
$ docker-compose up -d
```

Ver estado de contenedores 
```
$ docker-compose ps
```

Ejecuta (default test) contenedor y lo borra 
```
$ docker-compose run --rm app
```

Ejecuta contenedor y lo borra 
```
$ docker-compose run --rm app python3 test.py
```

## Cambiar valores 

Si deseas cambiar el rango del ejercicio de prueba en el archivo queens.py, es la siguiente linea:

```
for n in range(8, 10):
```

Si deseas aplicar los test para el rango (8, 16), quita los comentarios del archivo queens_test.py

```
 def test_10():

    sl = SolutionQ()
    assert sl.nqueens(10) == 724
```

## Author

* **Glenda Lopez** -  - [Gleekzone](https://github.com/Gleekzone)

