import mysql.connector
import pandas as pd 
dbConn = mysql.connector.connect(
	host="localhost", user="root", passwd="123456", database="os "
	)
etlData = pd.read_sql("SELECT * FROM completo_os WHERE fotoAntes=1", dbConn)
print(etlData)

# import pandas as pd 
# from sqlalchemy import create_engine
# dbConn = create_engine("mysql+mysqldb://usrid:password@localhost/etldb")
# etlData = pd.read_sql("SELECT * FROM tableETL WHERE feat01='98103'", dbConn)
# print(etlData)