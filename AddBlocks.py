from hashlib import sha256
import csv
from dotenv import load_dotenv
from datetime import datetime
import os 
"""

"""
def compute_block_hash(contents):
    
    block_hash = sha256(contents.encode()).hexdigest()
    return block_hash

def work_pow(tasks):
    nonce = 0
    block_appended = tasks+str(nonce)
    potential_hash = compute_block_hash(tasks)
    while not potential_hash.startswith('3' * 3):
        nonce += 1
        block_appended = block_appended[:-1]+str(nonce)
        potential_hash = compute_block_hash(block_appended)
        
        
    print("The hash was calculated after "+str(nonce)+" tries")
    print(potential_hash)
    return potential_hash
    
def proof_of_work(tasks):
        
    nonce = 0
    block_appended = tasks+str(nonce)
    potential_hash = compute_block_hash(tasks)
    while not potential_hash.startswith('1' * 3):
        nonce += 1
        block_appended = block_appended[:-1]+str(nonce)
        potential_hash = compute_block_hash(block_appended)
        
        
    print("The hash was calculated after "+str(nonce)+" tries")
    print(potential_hash)
    return potential_hash

def mine(ledger_file, hashcode):
    with open(ledger_file,'a+') as f:
        f.write(hashcode+"\n")
    ##deposit_shc()

def deposit_shc():
    load_dotenv()
    ap_acct = os.getenv('MINING_RECORDS_FILE')
    t_date = datetime.now().strftime("%Y-%m-%d")
    date_found = False
    
    if not os.path.isfile(ap_acct):
        with open(ap_acct,'a') as acct:
            print("Account file created")
        acct.close()
    
    with open(ap_acct,"r+",newline='') as acct:
        ##deposit_records = acct.readlines()
        deposit_records = csv.reader(acct, delimiter = ',')
        
        for dates in deposit_records:
            
            if (t_date in dates):
                date_found = True
                print("t_date found")
                with open(ap_acct,"r+",newline='') as acct_edit:
                    account_writer = csv.writer(acct_edit, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    dates[1] = int(dates[1])+1
                    account_writer.writerow(dates)
                    print("updated today's date")
                    ##update_shc_account_records(t_date, deposit_records, acct_edit)
                break
            
            
        if date_found == False:
            account_writer = csv.writer(acct, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            account_writer.writerow([t_date.strip('\n'),'1'.strip('\n')])
            print("written today's date")
    acct.close()

   
def count_balance(ledgerfile):
    line_count = 0
    with open(ledgerfile,'r') as f:
        file_lines = f.readlines()
        for line in file_lines:
            line_count+=1
    
    print(str(line_count))
    return line_count


