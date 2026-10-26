# Iniciar la sesión de Spark
spark = SparkSession.builder.appName("AnalisisInternet").getOrCreate()
spark.sparkContext.setLogLevel("WARN")

# Cargar el archivo CSV
print("Cargando el archivo internet.csv...")
df = spark.read.csv("internet.csv", header=True, inferSchema=True)

# Limpieza de datos (Quitar filas vacías)
df_limpio = df.dropna()

# Transformación: Agrupar por TECNOLOGIA y contar
try:
    resultados = df_limpio.groupBy("TECNOLOGIA").count().orderBy(col("count").desc())
    print("=== TECNOLOGÍAS DE INTERNET MÁS USADAS ===")
    resultados.show()
except Exception as e:
    print("Error con la columna. Mostrando el esquema original:")
    df_limpio.printSchema()

# Detener Spark
spark.stop()
