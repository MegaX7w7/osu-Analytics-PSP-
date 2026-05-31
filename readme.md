# Documentación de Arquitectura y Pipeline ETL para osu!Analytics

## 1.Resumen

osu!Analytics es la plataforma para registrar puntajes obtenidos en el cliente oficial de osu!(lazer).

Registra, compara y sigue tu progreso en el juego.

Este módulo opera como un dashboard híbrido: automatiza la extracción de datos  desde archivos locales y se combina con el ingreso manual de métricas no almacenadas en crudo (como el Unstable Rate), permitiendo un seguimiento detallado de la consistencia rítmica.

## 2. Flujo de Datos (ETL)

### 2.1 Extracción

* **Fuente:** Repeticiones locales de Osu! en su formato `.osr`.
* **Herramientas:** Se hace uso de `osrparse` para poder extraer los metadatos de las repeticiones de los archivos `.osr` (Python).
* **Proceso:** Se obtiene el archivo de repetición válido (`.osr`), el sistema usa la libreria `osrparse` usando su clase `replay` para obtener la metadata de la replay (`count_300`, `count_100`, `count_50`, `count_miss`) y el Combo Máximo.

### 2.2 Transformación

Trabajo en curso

##

Trabajo en curso.
