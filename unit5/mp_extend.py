original = [1,2,3]
extension = [4,5,6]
o = original
e = extension
def expand(o,e):
    for storage  in e:
        o.append(storage)

expand(o,e)
print(o)

    
