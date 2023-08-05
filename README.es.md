# Steam AppID Changer

Steam AppID Changer es un sencillo script de utilidad que te permite cambiar el AppID de un juego de Steam y ejecutarlo con un AppID modificado. El script está diseñado para ejecutarse como un ejecutable independiente (.exe) en Windows.

You can also read this in [English](https://github.com/Kioraga/steam-appid-changer/blob/main/README.md).

## Primeros pasos

Para utilizar el Steam AppID Changer, sigue estos pasos:

1.  Descarga la última versión del script como un ejecutable independiente desde la sección de [Releases](https://github.com/Kioraga/steam-appid-changer/releases) de este repositorio.

2.  Antes de ejecutar el script, asegúrate de tener un archivo `config.ini` en el mismo directorio que el ejecutable. El archivo de configuración debe especificar los detalles necesarios, como la ruta de instalación del juego, el nombre, el nombre del proceso y el AppID deseado para parchear.

3.  Haz doble clic en el ejecutable para iniciar el Steam AppID Changer.

Si deseas ver la salida en la terminal durante la ejecución, puedes utilizar el archivo ejecutable con la bandera `--show-output`. De lo contrario, la interfaz gráfica del script estará oculta.

## Configuración

El archivo `config.ini` contiene las siguientes secciones y opciones:

```ini
[Objetivo del Juego]
path = Ruta al directorio de instalación del juego
name = Nombre del juego
process = Nombre del proceso ejecutable del juego
appid = AppID original de Steam para el juego

[Parche]
patch_appid = Nuevo AppID de Steam para usar temporalmente
```

Asegúrate de configurar correctamente el archivo `config.ini` con los valores apropiados antes de ejecutar el script.

## Dependencias

El ejecutable de Steam AppID Changer no requiere dependencias externas para funcionar. Es un script autocontenido que interactúa con el archivo de appid de Steam y el ejecutable del juego.

## Licencia

Este proyecto está bajo la [Licencia MIT](https://github.com/Kioraga/steam-appid-changer/blob/main/LICENSE).

## Descargo de responsabilidad

Este script modifica archivos de juego y está destinado únicamente con fines educativos y de prueba. Úsalo de manera responsable y bajo tu propio riesgo. El autor y los colaboradores no se hacen responsables de los daños causados por el uso de este script.
