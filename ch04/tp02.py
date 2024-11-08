l = ["Valeur 01","Valeur 02","Valeur 03","Valeur 04"]

print(l)


print(l[0])
print(l[1])
print(l[2])
print(l[3])

for value in l:
    print(value)
print(50*'-')
for i in range(len(l)):
    print(str(i)+" "+l[i])
    print(i,l[i])
    
r = list(range(len(l)))
print(r)