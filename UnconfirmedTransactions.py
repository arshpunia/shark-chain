from dotenv import load_dotenv
import os
##uct: unconfirmed transaction

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
    



