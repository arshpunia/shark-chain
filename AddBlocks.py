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
        
        ##Need to figure a way out for the proof of work
    print("The hash was calculated after "+str(nonce)+" tries")
    print(potential_hash)
    return potential_hash

def add_to_ledger(ledger_file, hashcode):
    with open(ledger_file,'a+') as f:
        f.write(hashcode+"\n")


def mine(ledgerfile):
    line_count = 0
    with open(ledgerfile,'r') as f:
        file_lines = f.readlines()
        for line in file_lines:
            line_count+=1
    
    print(str(line_count))
    return line_count
    
def main():
    ##proof_of_work('tst_tasks.txt')
    add_to_ledger('shc.txt',proof_of_work('tst_tasks.txt'))
    mine('shc.txt')
    
if __name__=="__main__":
    main()
         