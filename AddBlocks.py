from hashlib import sha256
"""

"""
def compute_block_hash(contents):
    
    block_hash = sha256(contents.encode()).hexdigest()
    return block_hash


def proof_of_work(UserFile):
    
    with open(UserFile,'r') as task_file:
        user_tasks  = task_file.read()
    
    nonce = 0
    block_appended = user_tasks+str(nonce)
    potential_hash = compute_block_hash(user_tasks)
    while not potential_hash.startswith('0' * 2):
        nonce += 1
        block_appended = block_appended[:-1]+str(nonce)
        potential_hash = compute_block_hash(block_appended)
        
        
    print("The hash was calculated after "+str(nonce)+" tries")
    print(potential_hash)
    return potential_hash

def mine(ledger_file, hashcode):
    with open(ledger_file,'a+') as f:
        f.write(hashcode+"\n")


def count_balance(ledgerfile):
    line_count = 0
    with open(ledgerfile,'r') as f:
        file_lines = f.readlines()
        for line in file_lines:
            line_count+=1
    
    print(str(line_count))
    return line_count


