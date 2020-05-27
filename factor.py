tmplist = []
tmplist2 = []

x=int(input())
y=int(input())

    
for i in range(1, x + 1):
        if x % i == 0:
            tmplist.append(i)
            


           
for j in range(1, y + 1):
        if y % j == 0:
            tmplist2.append(j)
c=list(set(tmplist).intersection(set(tmplist2)))
print(len(c))
