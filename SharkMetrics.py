import AnalyticsEngine as ae 
import SqlTableMgmt as stm
from datetime import datetime

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

#####Query Methods

def query_task_metrics():
    cn = stm.connect_to_db()
    cursor = cn.cursor()
    t_date = datetime.now().strftime("%Y-%m-%d")
    sql_query_task_metrics = "SELECT * FROM task_metrics WHERE date = (%s)"
    sql_query_value = (t_date, )
    cursor.execute(sql_query_task_metrics, sql_query_value)
    
    query_result = cursor.fetchall()
    if len(query_result) == 1:
        print("Work tasks targeted: "+query_result[0][1])
    
    
    
def main():
    ##run_report()
    query_task_metrics()    
if __name__ == "__main__":
    main()
