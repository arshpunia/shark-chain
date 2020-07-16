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

def insert_auxiliary_task(task_description):
    cn = connect_to_db()
    cursor = cn.cursor()
    insertion_command = "INSERT INTO auxiliary_tasks (date, time, task_description,is_completed,added_to_ledger) VALUES (%s,%s,%s,%s,%s)"
    today_date = datetime.now().strftime("%Y-%m-%d")
    time_now = datetime.now().strftime("%H:%M:%S")
    vals = (today_date, time_now, task_description,True,False)
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

def check_for_work_task_block():
    cn = connect_to_db()
    cursor = cn.cursor()
    t_date = datetime.now().strftime("%Y-%m-%d")
    block_query = "SELECT * FROM work_tasks WHERE is_completed = (%s) AND added_to_ledger = (%s)"
    query_parameters = (True,False)
    cursor.execute(block_query,query_parameters)
    query_result = cursor.fetchall()
    wuct_list = []
    is_block = False
    for task in query_result:
        wuct_list.append(task[2])
    
    if len(wuct_list) == 5:
        is_block = True 
    
    return (is_block, wuct_list)


def check_for_auxiliary_task_block():
    cn = connect_to_db()
    cursor = cn.cursor()
    t_date = datetime.now().strftime("%Y-%m-%d")
    block_query = "SELECT * FROM auxiliary_tasks WHERE date = (%s) AND is_completed = (%s) AND added_to_ledger = (%s)"
    query_parameters = (t_date, True,False)
    cursor.execute(block_query,query_parameters)
    query_result = cursor.fetchall()
    auct_list = []
    is_block = False
    for task in query_result:
        auct_list.append(task[2])
    
    if len(auct_list) == 5:
        is_block = True 
    
    return (is_block, auct_list)

def ledgerify_task(task, table_name):
    """
    Marks the added_to_ledger column for work_task as True. 
    """
    cn = connect_to_db()
    cursor = cn.cursor()
    t_date = datetime.now().strftime("%Y-%m-%d")
    update_command = "UPDATE "+table_name +" SET added_to_ledger = True WHERE task_description = (%s) AND is_completed = (%s) AND added_to_ledger = (%s)"
    sql_params = (task,True, False)
    cursor.execute(update_command, sql_params)
    cn.commit()

def ledgerify_block(uct_list, table_name):
    for task in uct_list:
        ledgerify_task(task, table_name)
    
"""
def insert_work_task(task):
    
    ##Inserts a work-related task into the work_tasks table
    
    cn = connect_to_db()
    cursor = cn.cursor()
    insertion_command = "INSERT INTO work_tasks (date, time, task_description, is_completed, added_to_ledger) VALUES (%s,%s,%s,%s,%s)"
    today_date = datetime.now().strftime("%Y-%m-%d")
    time_now = datetime.now().strftime("%H:%M:%S")
    vals = (today_date,time_now,task,False,False)
    cursor.execute(insertion_command, vals)
    cn.commit()
"""
def insert_work_task(date, time, task):
    cn = connect_to_db()
    cursor = cn.cursor()
    insertion_command = "INSERT INTO work_tasks (date, time, task_description, is_completed, added_to_ledger) VALUES (%s,%s,%s,%s,%s)"
    ##task_date = date.strftime("%Y-%m-%d")
    task_date = date
    task_time = time 
    vals = (task_date,task_time,task,False,False)
    cursor.execute(insertion_command, vals)
    cn.commit()

def update_completed_work_task(task):
    cn = connect_to_db()
    cursor = cn.cursor()
    t_date = datetime.now().strftime("%Y-%m-%d")
    update_command = "UPDATE work_tasks SET is_completed = True, time = NOW() WHERE task_description = (%s) AND date = (%s)"
    sql_val = (task,t_date)
    cursor.execute(update_command,sql_val)
    cn.commit()     
    
def  populate_work_task_table(date, time, task_file):
    print("Populating work_tasks table with "+task_file+"...")
    ##task_file = os.getenv('TASK_FILE')
    print("Tasks pertain to "+date)
    with open(task_file) as tf:
        file_lines = tf.readlines()
        for line in file_lines:
            
            insert_work_task(date, time,line.strip('\n'))
    
    print("Updated work_tasks table!")
def add_block_to_ledger_database(hashcode):
    
    cn = connect_to_db()
    cursor = cn.cursor()
    today_date = datetime.now().strftime("%Y-%m-%d")
    time_now = datetime.now().strftime("%H:%M:%S")
    ledger_insertion_command = "INSERT INTO hash_records VALUES (%s,%s,%s,%s)"
    insertion_values = (today_date, time_now, hashcode, str(1))
    cursor.execute(ledger_insertion_command, insertion_values)
    cn.commit()

def main():
    check_for_work_task_block()
if __name__ == "__main__":
    main()