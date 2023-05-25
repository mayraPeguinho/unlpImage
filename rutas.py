import os

directorio_padre = os.path.dirname(__file__)

ruta_imagenes_perfil=os.path.join(directorio_padre,'imagenes','imagenes_perfil')

ruta_directorio_collages=os.path.join(directorio_padre,'imagenes','directorio_collages')

ruta_directorio_memes=os.path.join(directorio_padre,'imagenes','directorio_memes')

ruta_repositorio_imagenes=os.path.join(directorio_padre,'imagenes','repositorio_imagenes')

archivo_perfiles_json = os.path.join(directorio_padre,'datos','nuevo_perfil.json')

archivo_configuracion_json= os.path.join(directorio_padre,'datos','configuracion.json')

archivo_imagenes_etiquetadas_csv= os.path.join(directorio_padre,'datos','imagenes_etiquetadas.csv')