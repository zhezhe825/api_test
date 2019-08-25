import pymysql

def select_sql(sql):
    db = pymysql.connect(
        host="47.104.x.x",
        port=3306,
        user="root",
        passwd="root",
        db="django"
    )
    cur = db.cursor()
    cur.execute()
    data = cur.fetchall()
    db.close()
    return data

def qita_sql(sql):
    db = pymysql.connect(
        host="47.104.x.x",
        port=3306,
        user="root",
        passwd="root",
        db="django"
    )
    cur = db.cursor()
    cur.execute()
    db.commit()
    db.close()


if __name__ == '__main__':
    sql2 = "select * from student where id='001'"
    result = select_sql(sql2)
    print(result)
    sql3 = "update student set age='23' where id = '003'"
    qita_sql(sql3)