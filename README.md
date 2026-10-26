# Tarea 3 - Procesamiento Batch y Streaming (Big Data)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Apache Spark](https://img.shields.io/badge/Apache_Spark-E25A1C?style=for-the-badge&logo=apache-spark&logoColor=white)
![Apache Kafka](https://img.shields.io/badge/Apache_Kafka-231F20?style=for-the-badge&logo=apache-kafka&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)

**Estudiante:** Santiago Nieto Gómez  
**Universidad:** Universidad Nacional Abierta y a Distancia (UNAD)  
**Programa:** Ingeniería de Sistemas  

---

## Descripción del Proyecto
Este repositorio contiene los scripts desarrollados para la sustentación de la Tarea 3 del curso de Big Data. Se implementó una arquitectura de procesamiento de datos utilizando dos enfoques principales dentro de una máquina virtual Ubuntu:

*    **Procesamiento Batch:** Análisis estático de un dataset de conexiones a internet (`internet.csv`) utilizando **PySpark** para agrupar y ordenar tecnologías de red (`analisis_batch.py`).
*    **Procesamiento Streaming (Tiempo Real):** Simulación de tráfico de datos continuos mediante un Productor de **Apache Kafka** (`kafka_producer.py`) y lectura mediante un Consumidor de **Spark Streaming** procesando micro-lotes en vivo (`spark_streaming_consumer.py`).

## Entorno de Ejecución
*   Sistema Operativo: Ubuntu Linux (VirtualBox)
*   Mensajería: Apache Kafka y ZooKeeper
*   Procesamiento: Apache Spark y PySpark
*   Lenguaje: Python 3

## Sustentación en Video
A continuación, se presenta la demostración técnica de la ejecución del entorno completo:

[![Sustentación Tarea 3](https://img.youtube.com/vi/xpHKvPg3RWA/hqdefault.jpg)](https://youtu.be/xpHKvPg3RWA)

*(Haz clic en la imagen superior para ver el video en YouTube)*
