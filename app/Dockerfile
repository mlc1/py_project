#le decimos con que version queremos que lo ejecute python
FROM python:3.10
#creamos una carpeta dentro del contenedor
#se le puede colocar cualquier nombre 
#normalmente se le llama WORKDIR
WORKDIR /app
#copiamos el archivo de las dependencias
#copiar de un lado a otro solo se hace con un espacio
#el requirements.txt de la izq sera el local y el derecho el contenedor
COPY requirements.txt /app/requirements.txt

#Ahora dejamos listo e instaladas las dependencias.
#con --nocache-dir le decimos que no aplique el cache.
#Otra buena practica es decirle que si agrega uan actualizacion la haga --upgrade

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt


#Ahora hacemos un nuevo COPY por que hasta ahora solo se ha copiado el archivo requirements.
#Y ahora copiamos todo el codigo con . que significa ubicate en esta carpeta 
#y copialo todo y lo llevamos a nuestro espacio de trabajo en este caso app.

COPY . /app

CMD bash -c 'while true; do sleep 1; done'

