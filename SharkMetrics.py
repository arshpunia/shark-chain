import AnalyticsEngine as ae 

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
    
def main():
    run_report()
        
if __name__ == "__main__":
    main()
