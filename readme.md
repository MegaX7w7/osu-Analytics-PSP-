# Documentación de Arquitectura y Pipeline ETL para osu!Analytics

## 1.Resumen

osu!Analytics es la plataforma para registrar puntajes obtenidos en el cliente oficial de osu!(lazer).

Registra, compara y sigue tu progreso en el juego.

Este módulo opera como un dashboard híbrido: automatiza la extracción de datos  desde archivos locales y se combina con el ingreso manual de métricas no almacenadas en crudo (como el Unstable Rate), permitiendo un seguimiento detallado de la consistencia rítmica.

## 2. Flujo de Datos (ETL)

### 2.1 Extracción

* **Fuente:** Repeticiones locales de Osu! en su formato `.osr` dentro de una ruta en específico.
* **Herramientas:** Se hace uso de `osrparse` para poder extraer los metadatos de las repeticiones de los archivos `.osr` (Python).
* **Proceso:** Se obtiene el archivo de repetición válido (`.osr`), el sistema usa la libreria `osrparse` usando su clase `replay` para obtener la metadata de la replay (`count_300`, `count_100`, `count_50`, `count_miss`) y el Combo Máximo.
* **Almacenamiento:** Los datos guardados son procesados y almacenados dentro de un json temporal (`replayData.json`) usando hash maps para una complejidad constante $O(1)$  . Cada mapa esta identificado con un hash único, donde se agrupan todas las estadísticas de repeticiones dentro del mismo beatmap.

### 2.2 Transformación

Trabajo en curso

##

Trabajo en curso.
