original = [1,5,3,7,8,1,3,0,1]
to_replace = 1
replace_with = 4

def replace_all(original, to_replace, replace_with):
    for x in range (len(original)):
        if original[x] == to_replace:
            original[x] = replace_with
        
replace_all(original, to_replace, replace_with)
        
        
print (original)



