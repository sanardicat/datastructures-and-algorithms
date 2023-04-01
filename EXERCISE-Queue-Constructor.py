class Node:
    ## WRITE NODE CONSTRUCTOR HERE ##
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        
class Queue:
    ## WRITE QUEUE CONSTRUCTOR HERE ##
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.height = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next




my_queue = Queue(4)

my_queue.print_queue()



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""