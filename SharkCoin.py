import UnconfirmedTransactions as uct
import AddBlocks as ab
import sys


def shc_ecosystem(completed_task):
    uct.add_uct(completed_task)
    
    if uct.is_possible_block('shc-uct.txt'):
        print("5 transactions recorded! Will now start mining process")
        ab.mine('shc.txt',ab.proof_of_work('shc-uct.txt'))
    else:
        print("Keep going soldier")

def main():
    shc_ecosystem(sys.argv[1])
    
if __name__ == "__main__":
    main()