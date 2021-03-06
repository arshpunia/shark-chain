import AnalyticsEngine as ae 
import SqlTableMgmt as stm
from datetime import datetime
from prettytable import PrettyTable
import sys
import matplotlib.pyplot as plt

def update_metrics_tables():
    """
    Calls on methods from AnalyticsEngine to populate all three metrics tables. 
    """
    ae.insert_task_metric()
    ae.update_time_metrics_table()
    ae.update_ratios()

def clear_metrics_tables(): ##Clears todays recrods from the respective metrics tables. Method exists for robustness should anyone run the report twice. 
    ae.delete_todays_metrics()
    ae.delete_todays_time_metrics()
    ae.delete_todays_ratio_metrics()

def run_report():
    clear_metrics_tables()
    update_metrics_tables()
    work_tasks_targeted = ae.get_work_tasks_targeted()
    work_tasks_achieved = ae.get_work_tasks_achieved()
    t_ratio = work_tasks_achieved/work_tasks_targeted
    w_ratio, num_days = ae.get_weekly_ratio()
    pw_ratio = (float(w_ratio)+t_ratio)/(num_days+1)
 
    print("Your weekly ratio thus far is: "+format(pw_ratio,'.2f'))
    
    week_dates, daily_ratios = ae.get_weekly_performance_chart()
    time_stamps, tasks_completed = ae.get_time_metrics_chart()
    ##ae.get_weekly_performance_chart()
    ##ae.time_metrics_for_visualization()
    ##fig, axs = plt.subplots(2)
    plt.plot(week_dates, daily_ratios)
    ##axs[1].bar(time_stamps, tasks_completed)
    plt.show()
    
#####Query Methods

def query_task_metrics():
    cn = stm.connect_to_db()
    cursor = cn.cursor()
    t_date = datetime.now().strftime("%Y-%m-%d")
    sql_query_task_metrics = "SELECT * FROM task_metrics WHERE date = (%s)"
    sql_query_value = (t_date, )
    cursor.execute(sql_query_task_metrics, sql_query_value)
    
    task_table = PrettyTable()
    task_table.field_names = ["Date","Work Tasks Targeted","Work Tasks Achieved", "Auxiliary Tasks", "Work Coins", "Auxiliary Coins"]
    query_result = cursor.fetchall()
    if len(query_result) == 1:
        task_row = []
        
        for parameter in query_result[0]:
            task_row.append(parameter)
        print("\n****Task Metrics****")
        task_table.add_row(task_row)
        ##print("Work tasks targeted: "+str(query_result[0][1]))
        print(task_table)
    else:
        print("Validation error")
    
def query_ratio_metrics():
    cn = stm.connect_to_db()
    cursor = cn.cursor()
    t_date = datetime.now().strftime("%Y-%m-%d")
    sql_query_task_metrics = "SELECT * FROM ratio_metrics WHERE date = (%s)"
    sql_query_value = (t_date, )
    cursor.execute(sql_query_task_metrics, sql_query_value)
    
    ratios_table = PrettyTable()
    ratios_table.field_names = ["Date","WCT","APW"]
    query_result = cursor.fetchall()
    if len(query_result) == 1:
        ratio_row = []
        for parameter in query_result[0]:
            ratio_row.append(parameter)
        ratios_table.add_row(ratio_row)
        ##print("Work tasks targeted: "+str(query_result[0][1]))
        print("\n****Ratio Metrics****")
        print(ratios_table)
    else:
        print("Validation error")

def query_time_metrics():
    cn = stm.connect_to_db()
    cursor = cn.cursor()
    t_date = datetime.now().strftime("%Y-%m-%d")
    sql_query_task_metrics = "SELECT * FROM time_metrics WHERE date = (%s)"
    sql_query_value = (t_date, )
    cursor.execute(sql_query_task_metrics, sql_query_value)
    
    time_table = PrettyTable()
    time_table.field_names = ["Date","Time","Work Tasks","Auxiliary Tasks"]
    query_result = cursor.fetchall()
    
    
    for timestamp in query_result:
        time_row = []
        if timestamp[2] > 0 or timestamp[3] > 0:
            time_row.extend([timestamp[0],timestamp[1],timestamp[2],timestamp[3]])
            time_table.add_row(time_row)
    print("\n****Time Metrics****")
    print(time_table)
    

    
def main():
    if len(sys.argv) == 2:
        if sys.argv[1] == "-r":
            run_report()
        elif sys.argv[1] == "-q":
            query_task_metrics()
            query_ratio_metrics()
            query_time_metrics()
        else:
            print("Validation error. Unrecognized flag")
    else:
        print("Incorrect invocation")
    
if __name__ == "__main__":
    main()
