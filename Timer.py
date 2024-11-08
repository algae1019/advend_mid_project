#from B_Moore
import time
from src.notepad import notepad
from Hash_Table import Hash

# def
def execution_Time(script):
    start_time = time.time()
    hash_table = Hash(notepad)
    hash_table.create_Hash()
    end_time = time.time()

    total_time = end_time - start_time
    print(f"실행 시간 : {total_time:.5f}초")

if __name__ == "__main__":
    execution_Time("Hash_Table.py")