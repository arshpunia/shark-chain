import AnalyticsEngine as ae 

def update_metrics_tables():
    """
    Calls on methods from AnalyticsEngine to populate all three metrics tables. 
    """
    ae.insert_task_metric()
    ae.update_time_metrics_table()
    ae.update_ratios()
    
def main():
    update_metrics_tables()
        
if __name__ == "__main__":
    main()
