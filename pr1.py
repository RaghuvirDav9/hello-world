import time
import psycopg2

# main function .It establishes connection with DB and inserts whole filedata as a row in db.
if __name__ == '__main__':
    start_time = time.clock()
    conn = psycopg2.connect(database="postgres", user="docker", password="docker", host="localhost", port="8000")
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS line_fun")
    sql = '''CREATE TABLE line_fun(NUMBER int,DATA varchar(10485760))'''
    cursor.execute(sql)
    conn.commit()

    file= open('try.csv','rt')
    str1=file.read()
    str2=str1.replace('"','')
    str3=str1.replace('\n','')
    q=cursor.execute("insert into line_fun values(1,'"+str(str3)+"');")
    file.close()
    conn.commit()
    conn.close()
    print(time.clock() - start_time, "seconds")
