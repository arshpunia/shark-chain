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

##*******************Methods for time metrics********************
def get_time_dict():
    time_dict = {'05:00:00':0,'06:00:00':0,'07:00:00':0,'08:00:00':0,'09:00:00':0,'10:00:00':0,'11:00:00':0,'12:00:00':0,'13:00:00':0,'14:00:00':0,'15:00:00':0,'16:00:00':0,'17:00:00':0,'18:00:00':0,
    '19:00:00':0,'20:00:00':0,'21:00:00':0,'22:00:00':0}
    
    return time_dict

def get_work_time_metrics():
    time_ranges = get_time_dict()
    cn = stm.connect_to_db()
    cursor = cn.cursor()
    
    sql_query_statement = "SELECT * FROM work_tasks WHERE date = (%s) and is_completed = (%s)"
    t_date = datetime.now().strftime("%Y-%m-%d")
    sql_vals = (t_date, True)
    cursor.execute(sql_query_statement, sql_vals)
    
    query_result = cursor.fetchall()
    for row in query_result:
        ##rounded_time = row[1].split(':')[0]+":00:00"  ##Rounding the timestamp down to its hourly value 
        
        rounded_time = (datetime.min+row[1]).time().strftime("%H:00:00")
        if rounded_time != '00:00:00':
            time_ranges[rounded_time] = time_ranges[rounded_time]+1
    return time_ranges


def get_aux_time_metrics():
    time_ranges = get_time_dict()
    cn = stm.connect_to_db()
    cursor = cn.cursor()
    
    sql_query_statement = "SELECT * FROM auxiliary_tasks WHERE date = (%s) and is_completed = (%s)"
    t_date = datetime.now().strftime("%Y-%m-%d")
    sql_vals = (t_date, True)
    cursor.execute(sql_query_statement, sql_vals)
    
    query_result = cursor.fetchall()
    for row in query_result:
        
        rounded_time = (datetime.min+row[1]).time().strftime("%H:00:00")
        if rounded_time != '00:00:00':
            time_ranges[rounded_time] = time_ranges[rounded_time]+1
    return time_ranges    

def insert_time_metric(time, work_metric, aux_metric):
    cn = stm.connect_to_db()
    cursor = cn.cursor()
    
    sql_insertion_statement = "INSERT INTO time_metrics VALUES (NOW(),%s,%s,%s)"
    sql_insertion_vals = (time, work_metric, aux_metric)
    cursor.execute(sql_insertion_statement, sql_insertion_vals)
    cn.commit()

def update_time_metrics_table():
    aux_metrics = get_aux_time_metrics()
    work_metrics = get_work_time_metrics()
    time_list = aux_metrics.keys()
    for timestamp in time_list:
        insert_time_metric(timestamp,work_metrics[timestamp],aux_metrics[timestamp])

##*****************************Methods for ratio_metrics***************************


def main():
    insert_task_metric()
    ##update_time_metrics_table()
    
if __name__ == "__main__":
    main()