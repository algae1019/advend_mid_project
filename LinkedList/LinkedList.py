### Node ###
class Node:
    def __init__(self, line_num, word):
        self.data = (line_num, word)
        self.next = None



### LinkedList ###
class LinkedList:
    def __init__(self):
        self.head = None

    # 연결리스트에 추가
    def listAppend(self, line_num, word):
        if not self.head:
            self.head = Node(line_num, word)
        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = Node(line_num, word)

    # 연결리스트 -> 리스트
    def toList(self):
        result  = []
        current = self.head

        while current:
            result.append(current.data)
            current = current.next

        return result