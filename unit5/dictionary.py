from pprint import pprint
d = {}
choose = input("[Add]\n[Remove Key]\n[Remove Value]\n[Update]\n[Exit]\n choose one. ")
if choose == ("Add"):
    key = input("Enter a key. ")
    value = input("Enter a value. ")
    d[key] = value 
pprint(d)