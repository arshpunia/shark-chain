from dotenv import load_dotenv
import os
##uct: unconfirmed transaction

def add_uct(task):
    load_dotenv()
    uct_file = os.getenv('UNCONFIRMED_TRANSACTION_FILE')
    
    with open(uct_file,'a+') as uf:
        uf.write(task+"\n")
        
    uf.close()
    
def is_possible_block(uct_file):
    line_count=0
    is_block = False    
    with open(uct_file,'r') as f:
        file_lines = f.readlines()
        for line in file_lines:
            line_count+=1
    ##f.close()
    ##print(str(line_count))
    if line_count == 5:
        is_block = True
    
    return is_block

