

sid = [45,78,57,96,4,5,7,1,5,]

sid.reverse() #reverse sorting
print(sid)

sid.sort() #sorting in ascending order
sid.remove(1) #remove item '1' from list
print(sid)

sid.insert(4,100) #add 100 at index 4
print(sid)

sid.pop(5) #delete index 5 and return next value
print(sid)

print(sid.pop(5))
value = sid.pop(5)
print(value)