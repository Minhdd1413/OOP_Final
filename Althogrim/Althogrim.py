from pyspark.sql import SparkSession

logFile = "D:/Coding/OOP/Final/danhsach.txt"  # Should be some file on your system
spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
logData = spark.read.text(logFile).cache()

numAs = logData.filter(logData.value.contains('a')).count()
numBs = logData.filter(logData.value.contains('h')).count()
numBs += logData.filter(logData.value.contains('H')).count()
print("Lines with a: %i, lines with h: %i" % (numAs, numBs))

spark.stop()