### Page ###
class Page():
    def __init__(self, hash_table):
        self.content = []

        self.create_Page(hash_table)

    def create_Page(self, ht):
        for index in range(len(ht.hash_Table.keys())):
            self.content.append(ht.get_HashTable_data(index))