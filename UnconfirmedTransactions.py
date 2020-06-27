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
    
    with open(task_file, 'r') as tf:
        if task in tf.read():
            print("Task from task file found")
            with open(task_uct_file,'a+') as tuf:
                tuf.write(task+"\n")
            tuf.close()
        else:
            with open(uct_file,'a+') as uf:
                uf.write(task+"\n")
            
            uf.close()
    
    tf.close()
    

    
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
    



