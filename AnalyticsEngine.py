import SqlTableMgmt as stm
from datetime import datetime 

##----------Methods for the task_metrics table--------------

def  get_work_tasks_targeted():
    cn = stm.connect_to_db()
    cursor = cn.cursor()
    query_statement = "SELECT COUNT(*) FROM work_tasks WHERE date = (%s)"
    t_date = datetime.now().strftime("%Y-%m-%d")
    sql_val = (t_date, )
    cursor.execute(query_statement, sql_val)
    
    query_result = cursor.fetchall()
    num_targeted = query_result[0][0]
    
    return num_targeted
    
def get_work_tasks_achieved():
    cn = stm.connect_to_db()
    cursor = cn.cursor()
    
    query_statement = "SELECT COUNT(*) FROM work_tasks WHERE date = (%s) AND is_completed = (%s)"
    t_date = datetime.now().strftime("%Y-%m-%d")
    sql_vals = (t_date, True)
    cursor.execute(query_statement,sql_vals)
    
    query_result = cursor.fetchall()
    
    num_completed = query_result[0][0]
    print(num_completed)
    return num_completed
    
def get_aux_tasks_achieved():
    cn = stm.connect_to_db()
    cursor = cn.cursor()
    
    query_statement = "SELECT COUNT(*) FROM auxiliary_tasks WHERE date = (%s) AND is_completed = (%s)"
    t_date = datetime.now().strftime("%Y-%m-%d")
    sql_vals = (t_date, True)
    cursor.execute(query_statement,sql_vals)
    
    query_result = cursor.fetchall()
    
    num_completed = query_result[0][0]
    print(num_completed)
    return num_completed

def get_coins_from_work():
    cn = stm.connect_to_db()
    cursor = cn.cursor()
    
    query_statement = "SELECT COUNT(*) FROM hash_records WHERE date = (%s) AND hash LIKE (%s)"
    t_date = datetime.now().strftime("%Y-%m-%d")
    wildcard = '333%'
    sql_vals = (t_date, wildcard)
    
    cursor.execute(query_statement, sql_vals)
    query_result = cursor.fetchall()
    
    num_work_coins = query_result[0][0]
    
    return num_work_coins

def get_coins_from_aux_tasks():
    cn = stm.connect_to_db()
    cursor = cn.cursor()
    
    query_statement = "SELECT COUNT(*) FROM hash_records WHERE date = (%s) AND hash LIKE (%s)"
    t_date = datetime.now().strftime("%Y-%m-%d")
    wildcard = '111%'
    sql_vals = (t_date, wildcard)
    
    cursor.execute(query_statement, sql_vals)
    query_result = cursor.fetchall()
    
    num_aux_coins = query_result[0][0]
    
    print(num_aux_coins)
    return num_aux_coins   

def insert_task_metric():
    num_work_targets = get_work_tasks_targeted()
    num_work_achieved = get_work_tasks_achieved()
    num_aux_tasks = get_aux_tasks_achieved()
    num_work_coins = get_coins_from_work()
    num_aux_coins = get_coins_from_aux_tasks()
    
    cn = stm.connect_to_db()
    cursor = cn.cursor()
    t_date = datetime.now().strftime("%Y-%m-%d")
    sql_insertion_statement = "INSERT INTO task_metrics VALUES (%s,%s,%s,%s,%s,%s)"
    sql_vals = (t_date, num_work_targets, num_work_achieved, num_aux_tasks, num_work_coins, num_aux_coins)
    cursor.execute(sql_insertion_statement,sql_vals)
    cn.commit()

def main():
    insert_task_metric()

if __name__ == "__main__":
    main()