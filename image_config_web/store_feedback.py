import pymysql
from datetime import date

def submit_feedback(rating, comment, log_file):
    try:
        today_date = date.today()
        connection = pymysql.connect(host='mysql',
                                user='user',
                                password='password',
                                db='feedback_db')
        with connection.cursor() as cursor:
            sql = "insert into `feedback_table` (rating, comment, date, log_content ) values ('{a}','{b}','{c}','{d}')".format(a=rating,b=comment,c=today_date,d=log_file)
            print(sql)
            cursor.execute(sql)
        connection.commit()

        with connection.cursor() as cursor:
            sql = "select * from feedback_table;"
            cursor.execute(sql)
            values = cursor.fetchall()
        connection.close()
        print(values)
        response = {"status": 200, "msg": "Successfully inserted feedback", "values": values}
        return response

    except Exception as e:
        print(e)