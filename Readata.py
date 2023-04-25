from pyspark.sql import SparkSession

# Tạo một đối tượng SparkSession mới
spark = SparkSession.builder.appName("ReadCSV").getOrCreate()

# Đọc tệp CSV vào DataFrame
dir = "D:/Coding/OOP/Final/danhsach.txt"
df = spark.read.csv(dir, header=True, inferSchema=True)

# Hiển thị DataFrame
df.show()

# Dừng SparkSession
spark.stop()