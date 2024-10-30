def display_hash(hashTable):
    for i in range(len(hashTable)):
        print(i,end=" ")
        for j in hashTable[i]:
            print("-->",end=" ")
            print(j,end=" ")
        print()
HashTable=[[]for _ in range(10)]
def insert(HashTable,keyvalue,value):
    hash_key=keyvalue%len(HashTable)
    HashTable[hash_key].append(value)
insert(HashTable,30,'Saranathan')
insert(HashTable,25,'Tamilnadu')
insert(HashTable,10,'Clg')
insert(HashTable,9,'Trichy')
insert(HashTable,21,'AI')
insert(HashTable,41,'DS')
display_hash(HashTable)