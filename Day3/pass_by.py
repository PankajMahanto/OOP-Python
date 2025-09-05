
def change(L):
    print(id(L))
    L.append(4)
    print(id(L))


L1 = [1,2,5]
print(id(L1))
print(L1)

#! Outside of the function change the function value
#! for that reason we always passing the 
#! Jodi segula mutable Data hoy 
#! inmutable data does not any problem
change(L1)
print(L1)

L1 = [1,2,5]
print(id(L1))
print(L1)
change(L1[:])
print(L1)