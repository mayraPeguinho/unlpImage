import os

directorio_padre = os.path.dirname((os.path.abspath(__file__)))

ruta_imagenes_perfil=os.path.join(directorio_padre,'imagenes','imagenes_perfil')

ruta_imagen_por_defecto= os.path.join(directorio_padre,'imagenes','imagenes_perfil', 'avatar.png')

ruta_directorio_collages=os.path.join(directorio_padre,'imagenes','directorio_collages')

ruta_directorio_memes=os.path.join(directorio_padre,'imagenes','directorio_memes')

ruta_diseños_collages=os.path.join(directorio_padre,'imagenes','diseños_collages')

ruta_repositorio_imagenes=os.path.join(directorio_padre,'imagenes','repositorio_imagenes')

ruta_directorio_fuentes=os.path.join(directorio_padre,'fuentes')

archivo_perfiles_json = os.path.join(directorio_padre,'datos','nuevo_perfil.json')

archivo_configuracion_json= os.path.join(directorio_padre,'datos','configuracion.json')

archivo_imagenes_etiquetadas_csv= os.path.join(directorio_padre,'datos','imagenes_etiquetadas.csv')

archivo_logs_csv=os.path.join(directorio_padre,'logs','logs.csv')

archivo_tenmplates_json=os.path.join(directorio_padre,'datos','templates.json')