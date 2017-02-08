class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def compute_hash(self,key):
        return key%len(self.slots)
        
    def compute_rehash(self,oldhash):
        return (oldhash+1)%len(self.slots)
                
    def put(self,key,value):
        hashOfKey = self.compute_hash(key)
        
        if not self.slots[hashOfKey]:
            self.slots[hashOfKey] = key
            self.data[hashOfKey] = value
        else:
            # Replace existing values
            if self.slots[hashOfKey] == key:
                self.data[hashOfKey] = value
            # Handle collision
            else:
                nextSlot = self.compute_rehash(hashOfKey) 
                while self.slots[nextSlot] and self.slots[nextSlot] != key:
                    nextSlot = self.compute_rehash(nextSlot)
                if not self.slots[nextSlot]:
                    self.slots[nextSlot] = key
                    self.data[nextSlot] = value 
                else:
                    self.data[nextSlot] = value 
        
    def get(self,key):
        hashOfKey = self.compute_hash(key)
        startSlot = hashOfKey
        # Key is found without collision
        if self.slots[hashOfKey] == key:
            return self.data[hashOfKey]
        # Handle collision through 'open resolution' and 'linear probing'
        else:
            nextSlot = self.compute_rehash(hashOfKey) 
            # Loop until you either find the key or run out of entries in the hash table
            while self.slots[nextSlot] != key and nextSlot != startSlot:
                if self.slots[nextSlot] == key:
                    return self.data[nextSlot]
                else:
                    if nextSlot != startSlot:
                        nextSlot = self.compute_rehash(nextSlot)
                    else:
                        return None
                        #raise KeyError("The key %s is not found in the dictionary/hash table." % (key))
                
    def __getitem__(self,key):
        return self.get(key)
        
    def __setitem__(self,key,value):
        return self.put(key,value)
        
H=HashTable()
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
H[22]="penguin"
H[20]='duck'
print(H.slots)
print(H.data)
print(H[99])
