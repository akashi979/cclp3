test = [] 
f = int(input("enter no. of elements : ")) 
for i in range(0, f): 
    user = int(input()) 
    test.append(user) 
def selecsort(list1):
   for first in range(len(list1)):
       maxval=0
       for index in range(1,first+1):
           if list1[index]>list1[maxval]:
               maxval = index
       k = list1[first]
       list1[first] = list1[maxval]
       list1[maxval] = k
print("Your list is : ",*test)
selecsort(test)
print("Sorted list is : ",*test)
