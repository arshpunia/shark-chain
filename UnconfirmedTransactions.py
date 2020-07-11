from dotenv import load_dotenv
import os
import AnalyticsDb as adb
import AddBlocks as blocks
from datetime import datetime 
##uct: unconfirmed transaction
   

def return_work_tasks_list():
    cn = adb.connect_to_db()
    cursor = cn.cursor()
    t_date = datetime.now().strftime('%Y-%m-%d')
    
    query_work_tasks = "SELECT * FROM work_tasks WHERE date = (%s)"
    sql_val = (t_date,)
    cursor.execute(query_work_tasks, sql_val)
    
    query_result = cursor.fetchall()
    todays_work_tasks = []
    for row in query_result:
        todays_work_tasks.append(row[2])
    
    return todays_work_tasks
    
def mark_wuct(completed_work_task):
    ##Marks a work-related task as completed, but unconfirmed
    todays_work_tasks = return_work_tasks_list()
    task_is_work_related = False 
    for work_task in todays_work_tasks:
        if work_task == completed_work_task:
            task_is_work_related = True
            adb.update_completed_work_task(completed_work_task)
            print(completed_work_task+" was found and has been marked as completed!")
            break
    if task_is_work_related == False:
        print("Could not find "+completed_work_task+" in the database.\nHere are a few suggestions:\n--> Check if the work task was actually added to the database\n--> Maybe "+completed_work_task+" is an auxiliary task?")

def add_auct(completed_aux_task):
    todays_work_tasks = return_work_tasks_list()
    task_is_work_related = False 
    for work_task in todays_work_tasks:
        if work_task == completed_aux_task:
            task_is_work_related = True
            print("\'"+completed_aux_task+"\' is a work-related task. Please invoke the script as SharkCoin.py -w \'"+completed_aux_task+"\'\nTask was not marked as unconfirmed")
            break
     
    if task_is_work_related == False:
        adb.insert_auxiliary_task(completed_aux_task)

def mine_work_block(uct_list):
    ##Putting the strings all together
    combined_string = ""
    for work_task in uct_list:
        combined_string = combined_string + work_task
    ##Proof of work
    computed_hash = blocks.proof_of_work(combined_string)
    adb.add_block_to_ledger_database(computed_hash)
    adb.ledgerify_block(uct_list)
    
def is_possible_block(uct_file):
    line_count=0
    is_block = False    
    
    ##Creating file if one does not already exist 
    
    if not os.path.exists(uct_file):
        open(uct_file,"w")
    
    with open(uct_file,'r') as f:
        file_lines = f.readlines()
        for line in file_lines:
            line_count+=1
    ##f.close()
    ##print(str(line_count))
    if line_count == 5:
        is_block = True
    
    return is_block
    

def main():
    is_block, w_list = adb.check_for_work_task_block()
    if is_block:
        mine_work_block(w_list)
    else:
        print("keeep going soldier")
if __name__ == "__main__":
    main()

