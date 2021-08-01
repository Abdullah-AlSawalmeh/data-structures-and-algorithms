# from data_structures_and_algorithms_python.data_structures.hashtable.hashtable import Hashtable

# A problem with import
class Hashtable:
    def __init__(self, size):
        self.size = size
        self.map = [None]*size

    def add(self, key, value):
        idx = self.hash(key)

        if not self.map[idx]:
            self.map[idx] = [[key, value],]
        else:
            self.map[idx].append([key, value])

    def get(self, key):
        idx = self.hash(key)


        if self.map[idx]:
            for el in self.map[idx]:
                if el[0] == key:
                    return el[1]
        else:
            return None
            
    def contains(self, key):
        idx = self.hash(key)

        if self.map[idx]:
            for el in self.map[idx]:
                if el[0] == key:
                    return True
        return False

    def hash(self, key):
        ascii_total = 0

        for ch in key:
            ascii_total += ord(ch)
        hashed = ascii_total * 17
        hashed = hashed % self.size

        return hashed

############################################################        

def left_join(hash1,hash2):
    output = []

    for element in hash1.map:

        if element != None:

            for e in element:
                element_list = []
                element_list.append(e[0])
                element_list.append(e[1])
        
                if hash2.contains(e[0]):
                    element_list.append(hash2.get(e[0]))
                else:
                    element_list.append(None)
        
                output.append(element_list)
       
    return output

############################################################        

if __name__ == "__main__":
    h1 = Hashtable(1024)
    h1.add('fond','enamored')        
    h1.add('wrath', 'anger')          
    h1.add('diligent', 'employed')    
    h1.add('outfit', 'garb')           
    h1.add('guide', 'usher')

    h2 = Hashtable(1024)
    h2.add('fond', 'averse')
    h2.add('wrath', 'delight')
    h2.add('diligent', 'idle')
    h2.add('guide', 'follow')
    h2.add('flow', 'jam')


    print(left_join(h1,h2))