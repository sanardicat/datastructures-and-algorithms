class HashTable:
    ## WRITE HT CONSTRUCTOR HERE ##
    def __init__(self, size = 7) -> None:
        self.data_map = [None] * size
      
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            # 23 is a prime number. Any prime number 
            # can be used here. Dividing by modulus using % gives the remainder.
            # remainder of any number devided by length 7 would be 0 to 6
            # so we have 6 spaces in the hashmap
            # and each my_hash will point to a space in the hashmap.
            
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash  

    def print_table(self):
        for i, val in enumerate(self.data_map): 
            print(i, ": ", val)

        
my_hash_table = HashTable()

my_hash_table.print_table()


"""
    EXPECTED OUTPUT:
    ----------------
    0 :  None
    1 :  None
    2 :  None
    3 :  None
    4 :  None
    5 :  None
    6 :  None

"""