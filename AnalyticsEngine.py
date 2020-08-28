import SqlTableMgmt as stm
from datetime import datetime 
import matplotlib.pyplot as plt

##----------Methods for the task_metrics table--------------

def get_work_tasks_targeted():
    cn = stm.connect_to_db()
    cursor = cn.cursor()
    query_statement = "SELECT COUNT(*) FROM work_tasks WHERE date = (%s)"
    t_date = datetime.now().strftime("%Y-%m-%d")
    sql_val = (t_date, )
    ##sql_val = ('2020-08-01', )
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
    ##sql_vals = ('2020-08-01', True)
    cursor.execute(query_statement,sql_vals)
    
    query_result = cursor.fetchall()
    
    num_completed = query_result[0][0]
    
    return num_completed
    
def get_aux_tasks_achieved():
    cn = stm.connect_to_db()
    cursor = cn.cursor()
    
    query_statement = "SELECT COUNT(*) FROM auxiliary_tasks WHERE date = (%s) AND is_completed = (%s)"
    t_date = datetime.now().strftime("%Y-%m-%d")
    sql_vals = (t_date, True)
    ##sql_vals = ('2020-08-01', True)
    cursor.execute(query_statement,sql_vals)
    
    query_result = cursor.fetchall()
    
    num_completed = query_result[0][0]
    return num_completed

def get_coins_from_work():
    cn = stm.connect_to_db()
    cursor = cn.cursor()
    
    query_statement = "SELECT COUNT(*) FROM hash_records WHERE date = (%s) AND hash LIKE (%s)"
    t_date = datetime.now().strftime("%Y-%m-%d")
    wildcard = '333%'
    sql_vals = (t_date, wildcard)
    ##sql_vals = ('2020-08-01', wildcard)
    
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
    ##sql_vals = ('2020-08-01', wildcard)
    cursor.execute(query_statement, sql_vals)
    query_result = cursor.fetchall()
    
    num_aux_coins = query_result[0][0]
    return num_aux_coins   

def insert_task_metric():
    "Initializing task metrics analysis...."
    num_work_targets = get_work_tasks_targeted()
    print(str(num_work_targets)+" work tasks were targeted")
    num_work_achieved = get_work_tasks_achieved()
    print(str(num_work_achieved)+ " work tasks were achieved")
    num_aux_tasks = get_aux_tasks_achieved()
    print(str(num_aux_tasks)+" auxiliary tasks were completed")
    num_work_coins = get_coins_from_work()
    print(str(num_work_coins)+" SharkCoins were earned from completing work-related tasks")
    num_aux_coins = get_coins_from_aux_tasks()
    print(str(num_aux_coins) + " SharkCoins were earned from completing auxiliary tasks")
    cn = stm.connect_to_db()
    cursor = cn.cursor()
    t_date = datetime.now().strftime("%Y-%m-%d")
    sql_insertion_statement = "INSERT INTO task_metrics VALUES (%s,%s,%s,%s,%s,%s)"
    sql_vals = (t_date, num_work_targets, num_work_achieved, num_aux_tasks, num_work_coins, num_aux_coins)
    ##sql_vals = ('2020-08-01', num_work_targets, num_work_achieved, num_aux_tasks, num_work_coins, num_aux_coins)
    cursor.execute(sql_insertion_statement,sql_vals)
    cn.commit()
    print("Completed task metrics analysis!")
    
def delete_todays_metrics():
    cn = stm.connect_to_db()
    cursor = cn.cursor()
    t_date = datetime.now().strftime("%Y-%m-%d")
    sql_deletion_statement = "DELETE FROM task_metrics WHERE date = (%s)"
    sql_deletion_value = (t_date, )
    ##sql_deletion_value = ('2020-08-01', )
    cursor.execute(sql_deletion_statement, sql_deletion_value)
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
    ##sql_vals = ('2020-08-01', True)
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
    ##sql_vals = ('2020-08-01', True)
    cursor.execute(sql_query_statement, sql_vals)
    
    query_result = cursor.fetchall()
    for row in query_result:
        
        rounded_time = (datetime.min+row[1]).time().strftime("%H:00:00")
        if rounded_time != '00:00:00':
            time_ranges[rounded_time] = time_ranges[rounded_time]+1
    return time_ranges    

def time_metrics_for_visualization():
    time_dict = get_time_dict()
    
    cn = stm.connect_to_db()
    cursor = cn.cursor()
    
    sql_query_statement = "SELECT * FROM time_metrics"
    cursor.execute(sql_query_statement)
    
    query_result = cursor.fetchall()
    for row in query_result:
        time_val = str(row[1])
        formatted_time = (datetime.min+row[1]).time().strftime("%H:00:00")
        time_dict[formatted_time] = time_dict[formatted_time]+row[2]
    
    return time_dict
    
def insert_time_metric(time, work_metric, aux_metric):
    cn = stm.connect_to_db()
    cursor = cn.cursor()
    
    sql_insertion_statement = "INSERT INTO time_metrics VALUES (NOW(),%s,%s,%s)"
    ##sql_insertion_statement = "INSERT INTO time_metrics VALUES (%s,%s,%s,%s)"
    sql_insertion_vals = (time, work_metric, aux_metric)
    ##sql_insertion_vals = ('2020-08-01',time, work_metric, aux_metric)
    cursor.execute(sql_insertion_statement, sql_insertion_vals)
    cn.commit()

def update_time_metrics_table():
    print("Initializing time metrics analysis....")
    aux_metrics = get_aux_time_metrics()
    work_metrics = get_work_time_metrics()
    time_list = aux_metrics.keys()
    for timestamp in time_list:
        insert_time_metric(timestamp,work_metrics[timestamp],aux_metrics[timestamp])
    
    print("Completed time metrics analysis!")
def delete_todays_time_metrics():
    cn = stm.connect_to_db()
    cursor = cn.cursor()
    t_date = datetime.now().strftime("%Y-%m-%d")
    sql_deletion_statement = "DELETE FROM time_metrics WHERE date = (%s)"
    sql_deletion_value = (t_date, )
    ##sql_deletion_value = ('2020-08-01', )
    cursor.execute(sql_deletion_statement, sql_deletion_value)
    cn.commit()
    

##*****************************Methods for ratio_metrics***************************

def get_weekly_ratio():
    cn = stm.connect_to_db()
    cursor = cn.cursor()
    sql_query_statement = "SELECT date,w_ct FROM ratio_metrics WHERE YEARWEEK(date) = YEARWEEK(NOW());"
    cursor.execute(sql_query_statement)
    query_results = cursor.fetchall()
    t_date = datetime.now().strftime("%Y-%m-%d")
    
    ratio_sum = 0
    count = 0
    for row in query_results:
        if not(str(row[0]) == t_date):
            
            ratio_sum+= row[1]
            count+=1
    
    return (ratio_sum, count)

def get_weekly_ratio_list():
    cn = stm.connect_to_db()
    cursor = cn.cursor()
    sql_query_statement = "SELECT date,w_ct FROM ratio_metrics WHERE YEARWEEK(date) = YEARWEEK(NOW());"
    cursor.execute(sql_query_statement)
    query_results = cursor.fetchall()
    dates_list = []
    ratios_list = []
    for row in query_results:
        dates_list.append(str(row[0])[5:])
        ratios_list.append(row[1])
    
    return (dates_list, ratios_list)

def insert_ratios(wct_ratio, apw_ratio): ##wct = work completed to targeted; apw = aux per work 
    cn = stm.connect_to_db()
    cursor = cn.cursor()
    sql_insertion_statement = "INSERT INTO ratio_metrics VALUES (NOW(), %s, %s)"
    ##sql_insertion_statement = "INSERT INTO ratio_metrics VALUES (%s, %s, %s)"
    sql_vals = (wct_ratio, apw_ratio)
    ##sql_vals = ('2020-08-01',wct_ratio, apw_ratio)
    cursor.execute(sql_insertion_statement, sql_vals)
    cn.commit()
    
def update_ratios():
    cn = stm.connect_to_db()
    cursor = cn.cursor()
    
    sql_query_statement = "SELECT * FROM task_metrics WHERE date = (%s)"
    t_date = datetime.now().strftime("%Y-%m-%d")
    sql_vals = (t_date,)
    ##sql_vals = ('2020-08-01',)
    cursor.execute(sql_query_statement, sql_vals)
    query_result = cursor.fetchall()
    wct = 0
    apw = 0
    if len(query_result) == 1:
        print("Initializing ratio metrics analysis....")
        work_target = int(query_result[0][1])
        work_completed = int(query_result[0][2])
        aux_completed = int(query_result[0][3])
        
        wct = work_completed/work_target
        print(str(wct) +" is the wct ratio")
        apw = aux_completed/work_completed
        print(str(apw)+" is the apw ratio")
        insert_ratios(wct, apw)
        print("Completed ratio metrics analysis!")
    else:
        print("Validation error. Please check the table for any duplicate records from today and delete them")

def delete_todays_ratio_metrics():
    cn = stm.connect_to_db()
    cursor = cn.cursor()
    t_date = datetime.now().strftime("%Y-%m-%d")
    sql_deletion_statement = "DELETE FROM ratio_metrics WHERE date = (%s)"
    sql_deletion_value = (t_date, )
    ##sql_deletion_value = ('2020-08-01', )
    cursor.execute(sql_deletion_statement, sql_deletion_value)
    cn.commit()

#########Methods for data visualization################

def get_donut_chart():
    cn = stm.connect_to_db()
    cursor = cn.cursor()
    work_targeted = get_work_tasks_targeted()
    work_achieved = get_work_tasks_achieved()
    work_remaining = work_targeted - work_achieved
    names=['Tasks remaining', 'Tasks Completed']
    donut_params = [work_remaining, work_achieved]
    plt.pie(donut_params, labels = names, autopct='%1.1f%%', startangle=90)
    middle_circle = plt.Circle((0,0),0.7, color='white')
    p = plt.gcf()
    p.gca().add_artist(middle_circle)
    plt.show()
  


def get_weekly_performance_chart():
    dates_list, ratios_list = get_weekly_ratio_list()
    ##weekly_plot = plt.plot(dates_list, ratios_list)
    return (dates_list, ratios_list)
    
def get_time_metrics_chart():
    time_list = []
    num_list = []
    time_metrics = time_metrics_for_visualization()
    for key in time_metrics:
        time_list.append(key[0:5])
        num_list.append(time_metrics[key])
    
    ##print(str(time_metrics))
    return (time_list, num_list)
    
    
    
    
    
    
    
    