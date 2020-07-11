from dotenv import load_dotenv
import os
import AnalyticsDb as adb
from datetime import datetime 
##uct: unconfirmed transaction

def mark_aux_task_unconfirmed(task):
    cn = adb.connect_to_db()
    cursor = cn.cursor()
    update_command = "UPDATE auxiliary_tasks SET is_completed = True WHERE task_description = (%s)"
    sql_val = (task,)
    cursor.execute(update_command,sql_val)
    cn.commit()    

def mark_work_task_unconfirmed(task):
    cn = adb.connect_to_db()
    cursor = cn.cursor()
    update_command = "UPDATE work_tasks SET is_completed = True WHERE task_description = (%s)"
    sql_val = (task,)
    cursor.execute(update_command,sql_val)
    cn.commit()    

def add_uct(completed_task):
    load_dotenv()
    task_file = os.getenv('TASK_FILE')
    
    cn = adb.connect_to_db()
    cursor = cn.cursor()
    t_date = datetime.now().strftime('%Y-%m-%d')
    print(str(t_date))
    query_work_tasks = "SELECT * FROM work_tasks WHERE date = (%s)"
    sql_val = (t_date,)
    cursor.execute(query_work_tasks, sql_val)
    
    query_result = cursor.fetchall()
    todays_work_tasks = []
    for row in query_result:
        todays_work_tasks.append(row[2])
        
    
    
    task_is_work_related = False 
    for work_task in todays_work_tasks:
        if work_task == completed_task:
            task_is_work_related = True
            mark_work_task_unconfirmed(completed_task)
            break
     
    if task_is_work_related == False:
        mark_aux_task_unconfirmed(completed_task)

"""       
def add_uct(task):
    load_dotenv()
    uct_file = os.getenv('UNCONFIRMED_TRANSACTION_FILE')
    task_file = os.getenv('TASK_FILE')
    task_uct_file = os.getenv('UNCONFIRMED_TASK_TRANSACTION_FILE')
    
    ##Checking if the task is in the task file.
    ##If yes, it is pushed to the another file, also known as the unconfirmed task transaction file. 
    ##Daily tasks are processed independently of other tasks. This aids analysis of overall efficiency. 
    task_found = False
    with open(task_file,"r+") as tf:
        task_file_lines = tf.readlines()
        for line in task_file_lines:
            if line.strip('\n') == task:
                task_found = True
                print("Task from task file found")
                with open(task_uct_file,'a+') as tuf:
                    tuf.write(task+"\n")
                tuf.close()
                with open(task_file,"w") as tfe:
                    mark_task_as_done(line,task_file_lines,tfe)
                break
    tf.close()
    
    if not task_found:
        with open(uct_file,'a+') as uf:
            uf.write(task+"\n")
            
        uf.close()
            
    
"""
def mark_task_as_done(task,task_file_lines,tf):

    load_dotenv()
    uct_file = os.getenv('UNCONFIRMED_TRANSACTION_FILE')
    task_file = os.getenv('TASK_FILE')
    task_uct_file = os.getenv('UNCONFIRMED_TASK_TRANSACTION_FILE')


    for line in task_file_lines:
        if line != task:
            tf.write(line)
        else:
            print("Marking transaction as done!")
            tf.write("[x]"+line)
    
 
def is_possible_block():
    load_dotenv()
    

    
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
    add_uct('analytics engine')
if __name__ == "__main__":
    main()

