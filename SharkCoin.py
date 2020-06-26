import UnconfirmedTransactions as uct
import AddBlocks as ab
import sys
import os 
from dotenv import load_dotenv

def shc_ecosystem(completed_task):
    load_dotenv()
    uct.add_uct(completed_task)
    uct_file = os.getenv('UNCONFIRMED_TRANSACTION_FILE')
    task_uct_file = os.getenv('UNCONFIRMED_TASK_TRANSACTION_FILE')
    
    mined_file = os.getenv('MINED_FILE')
    if uct.is_possible_block(uct_file):
        print("5 transactions recorded! Will now start mining process")
        ab.mine(mined_file,ab.proof_of_work(uct_file))
        os.remove(uct_file)
    else:
        print("Keep going soldier")
    
    
    if uct.is_possible_block(task_uct_file):
        print("5 work-related transactions recorded! will now start mining process")
        ab.mine(mined_file,ab.proof_of_work(uct_file))
    else:
        print("need to accomplish more work-tasks")
        
def main():
    shc_ecosystem(sys.argv[1])
    
if __name__ == "__main__":
    main()