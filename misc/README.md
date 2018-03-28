# README
28/03/2018

## Datos

Descarga el [dump de la Wikipedia en español](https://dumps.wikimedia.org/eswiki/20180320/) 
más reciente. 

El fichero que contiene el texto de los artículos se llama `eswiki-FECHA-pages-articles-multistream.xml.bz2` y comprimido
con bzip2 ocupa unos 2.6 GB.

Lo descargamos en el volumen de datos persistente:

    cd ~/eswiki
    wget https://dumps.wikimedia.org/eswiki/20180320/eswiki-20180320-pages-articles-multistream.xml.bz2


## Preprocesado: de xml a ficheros individuales txt

El dump se distribuye en un único fichero XML. Para eliminar las etiquetas de
MediaWiki, limpiar el formato, extraer el contenido y guardarlo en un fichero por 
artículo, se puede usar la herramienta
[wikiextractor](https://github.com/attardi/wikiextractor). 

La [documentación explica todas las opciones
disponibles](https://github.com/attardi/wikiextractor/blob/master/README.md). Yo he 
usado:

    ./WikiExtractor.py --processes 8 --output ~/eswiki/txt --compress --sections --lists--filter_disambig_pages --no-templates --discard_elements gallery,timeline,noinclude ~/eswiki/eswiki-20180320-pages-articles-multistream.xml


## Entrenando los vectores

Para entrenar vectores de palabra con word2vec se puede lanzar el script `text-word2vec.py`. 
Por ejemplo, para lanzarlo sobre la colección de Wikipedia en español con 250 dimensiones, 
8 hilos y un umbral para crear el vocabulario de 10 ocurrencias, ejecuta:

    ./text-word2vec.py -i ~/eswiki/txt -s 250 -w 8 -c 10 -n eswiki

