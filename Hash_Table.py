from src.notepad import notepad
from LinkedList.LinkedList import LinkedList
import re

### HashTable ###
class Hash:
    def __init__(self, notepad):
        self.hash_Table = {}
        self.notepad    = notepad

        self.create_Hash()

    # Hash 테이블 구성
    def create_Hash(self):
        for line_num, line in enumerate(self.notepad, start = 1):
            words = re.findall(r'\b[a-zA-Z]+\b', line.lower())

            for word in words:
                hashKey = len(word)

                if hashKey not in self.hash_Table:
                    self.hash_Table[hashKey] = LinkedList()

                self.hash_Table[hashKey].listAppend(line_num, word)

    def get_HashTable_data(self, index):
        key = sorted(self.hash_Table.keys())[index]
        entries = sorted(self.hash_Table[key].toList(), key=lambda x: x[1])
        fentries = [f"Line {line_num:<3}  -  {word}" for line_num, word in entries]
        return "\n".join(fentries)