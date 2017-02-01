def remove_all(original,target):
    count = 0
    for x in range(len(original)):
        if original[x] == target:
            count = count + 1
    for remove_count in range(count):
        original.remove(target)
a = [1,5,3,7,8,1,3,0,1]
remove_all(a, 1)
print(a)