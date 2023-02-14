a=(input("Introduceti numarul= "))
if not a.isnumeric() or int(a)<=0:
    print("Date invalide - introduceti un numar pozitiv, diferit de 0")
    exit()
a=int(a)
f=1   
i=1
while i<=a:
    f=f*i
    i+=1
print(a,"! = ",f)
