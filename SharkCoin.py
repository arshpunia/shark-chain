import UnconfirmedTransactions as uct
import AddBlocks as ab
import SqlTableMgmt as stm
import sys
import os 
from dotenv import load_dotenv
from datetime import datetime
import AnalyticsEngine as ae




def analysis_upon_completion():
    work_tasks_targeted = ae.get_work_tasks_targeted()
    work_tasks_achieved = ae.get_work_tasks_achieved()
    t_ratio = work_tasks_achieved/work_tasks_targeted
    w_ratio, num_days = ae.get_weekly_ratio()
    pw_ratio = (float(w_ratio)+t_ratio)/(num_days+1)
    print("Your WCT ratio for today is: "+format(t_ratio,'.2f'))
    print("Your weekly ratio thus far is: "+format(pw_ratio,'.2f'))
    ae.get_donut_chart()
    
    
def shc_ecosystem(completed_task):
    load_dotenv()
    uct.add_uct(completed_task)
    uct_file = os.getenv('UNCONFIRMED_TRANSACTION_FILE')
    task_uct_file = os.getenv('UNCONFIRMED_TASK_TRANSACTION_FILE')
    
    mined_file = os.getenv('MINED_FILE')
    
    print("Transaction successfully recorded!")
    
    if uct.is_possible_block(uct_file):
        print("5 transactions recorded! Will now start mining process")
        ab.mine(mined_file,ab.proof_of_work(uct_file))
        print("Mining process complete")
        os.remove(uct_file)
    
    if uct.is_possible_block(task_uct_file):
        print("5 work-related transactions recorded! will now start mining process")
        ab.mine(mined_file,ab.proof_of_work(uct_file))
        print("Mining process complete")
        os.remove(task_uct_file)

def shc_work_ecosystem(completed_task):
    uct.mark_wuct(completed_task)
    is_block, w_list = stm.check_for_work_task_block()
    if is_block:
        uct.mine_work_block(w_list,'work_tasks')
    else:
    
        print(str(len(w_list))+" unconfirmed work tasks currently awaiting addition to the ledger")
    analysis_upon_completion()
    
def add_task_on_the_fly(taskname):
    """
    Method to add a work task to the TODO list after the task file has been submitted  
    """
    t_date = datetime.now().strftime("%Y-%m-%d")
    
    stm.insert_work_task(t_date,"00:00:00",taskname)
    print("Inserted new task in today's TODO list: "+taskname)

def query_captured_tasks():
    stm.get_captured_tasks()
 
def query_pending_tasks():
    """
    Method to print the remaining TODO taks for the day
    """
    stm.get_remaining_tasks()
    
def shc_aux_ecosystem(completed_task):
    
    uct.add_auct(completed_task)
    is_block, a_list = stm.check_for_auxiliary_task_block()
    if is_block:
        uct.mine_block(a_list,'auxiliary_tasks')
    else:
        print(str(len(a_list))+" unconfirmed auxiliary tasks currently awaiting addition to the ledger")
    
    analysis_upon_completion()
    
def capture_task(task_name):
    stm.insert_captured_task(task_name)
    print("Captured new task: "+task_name)

def validate_date_string(date_text):
##Adapted from https://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python
    is_valid_string = False
    try:
        datetime.strptime(date_text,'%Y-%m-%d')
        is_valid_string = True
    except ValueError:
        raise ValueError("Incorrect date format. Please use YYYY-MM-DD format")
        is_valid_string = False
        
    return is_valid_string

def invoke_shc(flag, task):
    if flag == "-w":
        shc_work_ecosystem(task)
        
    elif flag == "-a":
        shc_aux_ecosystem(task)
    
    elif flag == "-t":
        t_date = datetime.now().strftime("%Y-%m-%d")
        time_now = datetime.now().strftime("%H:%M:%S")
        stm.populate_work_task_table(t_date, "00:00:00", task)
    
    elif flag == "-nt":
        add_task_on_the_fly(task)
    
    elif flag == "-c":
        capture_task(task)
    else:
        print("Unsupported flag\nPlease use one of the supported flags as follows: ")
        print("--> -w <work-task-name>")
        print("--> -a <auxiliary-task-name>")
        print("--> -t <work-target-file>")
        print("--> -nt <new-task>")
        print("--> -c <captured-task>")
        print("--> -ft <YYYY-MM-DD> <work-target-file>")
        print("--> -q")
def main():
    
    if len(sys.argv) == 3:
        invoke_shc(sys.argv[1],sys.argv[2])
    
    elif len(sys.argv) == 4 and sys.argv[1] == "-ft" and len(sys.argv[2]) == 10:
        if validate_date_string(sys.argv[2]):
            stm.populate_work_task_table(sys.argv[2],"00:00:00",sys.argv[3])
        else:
            print("Improper invocation\nPlease invoke  future task mode as: ")
            print("--> -ft <YYYY-MM-DD> <work-target-file>")
        
    elif len(sys.argv) ==2 and sys.argv[1] == "-q":
        query_pending_tasks()
    
    elif len(sys.argv) ==2 and sys.argv[1] == "-cq":
        query_captured_tasks()
    
    else:
        print("Improper invocation\nPlease use one of the supported flags as follows: ")
        print("--> -w <work-task-name>")
        print("--> -a <auxiliary-task-name>")
        print("--> -t <work-target-file>")
        print("--> -ft <task-date> <work-target-file>")
        print("--> -nt <new-task>")
        print("--> -q")
    
    
if __name__ == "__main__":
    main()