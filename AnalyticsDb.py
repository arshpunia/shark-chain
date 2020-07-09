import mysql.connector
from datetime import datetime 
from dotenv import load_dotenv
import os

def connect_to_db():
    load_dotenv()
    db_username = os.getenv('db_username')
    db_password = os.getenv('db_password')
    
    mydb = mysql.connector.connect(
        host = "localhost",
        user = db_username,
        password = db_password,
        database = "shark_coin_analytics"
    )
    ##cursor = mydb.cursor()
    
    return mydb

def insert_additional_task(task_description):
    cn = connect_to_db()
    cursor = cn.cursor()
    insertion_command = "INSERT INTO additional_tasks (date, time, task_description) VALUES (%s,%s,%s)"
    today_date = datetime.now().strftime("%Y-%m-%d")
    time_now = datetime.now().strftime("%H:%M:%S")
    vals = (today_date, time_now, task_description)
    cursor.execute(insertion_command,vals)
    cn.commit()
    
def query_daily_report():
    cn = connect_to_db()
    cursor = cn.cursor()
    query = ("SELECT * FROM daily_report;")
    cursor.execute(query)
    
    result = cursor.fetchall()
    
    for row in result:
        print(row[0])
    
def insert_work_task(task):
    """
    Inserts a work-related task into the work_tasks table
    """
    cn = connect_to_db()
    cursor = cn.cursor()
    insertion_command = "INSERT INTO work_tasks (date, time, task_description, is_completed, added_to_ledger) VALUES (%s,%s,%s,%s,%s)"
    today_date = datetime.now().strftime("%Y-%m-%d")
    time_now = datetime.now().strftime("%H:%M:%S")
    vals = (today_date,time_now,task,False,False)
    cursor.execute(insertion_command, vals)
    cn.commit()
    
    
def  populate_work_task_table():
    load_dotenv()
    task_file = os.getenv('TASK_FILE')
    
    with open(task_file) as tf:
        file_lines = tf.readlines()
        for line in file_lines:
            insert_work_task(line.strip('\n'))

def main():
    ##query_daily_report()
    ##insert_additional_task("Wrote additional task insertion method")
    populate_work_task_table()
if __name__ == "__main__":
    main()