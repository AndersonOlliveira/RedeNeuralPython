import pymysql
conn = pymysql.connect(host='localhost', user='andersonOliveira',passwd='123456', db='suporte_visium',cursorclass=pymysql.cursors.DictCursor)
with conn:
    with conn.cursor() as cursor: 
# cursor = connection.cursor()
       sql = "INSERT INTO tb_solucoes (titulo,assunto) VALUES (%s, %s)"
       cursor.execute(sql,('teste', 'teste'))
    #    conn.commit()
    #    conn.close()
    
    
    with conn.cursor() as cursor:
        sql = "SELECT id,usuario, grupo FROM tb_uservisium where grupo = %s"
        cursor.execute(sql,('interno',))
        result = cursor.fetchone()
        print(result)


