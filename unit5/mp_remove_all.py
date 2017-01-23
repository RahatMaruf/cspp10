original = [1,5,3,7,8,1,3,0,1]
target = 1

def remove_all(original, target):
    for storage in (original):
        original.remove(storage, target)
        
print (original)