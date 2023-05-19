import socket
import pyspark.sql as sql
from pyspark.sql import SparkSession
import os
from pyspark.sql.functions import asc, desc
def listening_java():
    HOST = 'localhost'  
    PORT = 8080       
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        data = s.recv(1024)
    return data.decode()
    
def getdata():
    data_dir = "D:/Coding/OOP/Final/auto-mpg.csv"
    spark = SparkSession.builder.appName("Read CSV").getOrCreate()
    df = spark.read.csv(data_dir, header=True, inferSchema=True).cache()
    return df
    
def savedata(df):
    save_dir = "Final/Result"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    df.write.csv(save_dir, header=True)

def sort_up_down(df, collumn):
    option = listening_java().lstrip()
    if option == "soft_up":
        df_sorted = df.sort(asc(collumn))
        df_sorted = df.orderBy(df[collumn].asc_nulls_first())
    elif option == "soft_up":
        df_sorted = df.sort(desc(collumn))
        df_sorted = df.orderBy(df[collumn].desc_nulls_last())
    savedata(df_sorted)

    