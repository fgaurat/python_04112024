

d = {
    "name":"GAURAT",
    "first_name":"Fred",
    "job":"dev"
}

print(d)
print(d['name'])

for k in d:
    print(k,':',d[k])# name : GAURAT,...
    
for k,v in d.items():
    print( k,v)
    
l = [10,20,30,40]

for i,v in enumerate(l):
    print(i,v)