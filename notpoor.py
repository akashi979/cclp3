a=input("enter a sentence: ")
b=input("enter a another one: ")
def notpoor(str1):
   strnot = str1.find(' not ')
   poor = str1.find(' poor')
  

   if poor > strnot and strnot>0 and poor>0:
    str1 = str1.replace(str1[strnot:(poor+5)], ' good')
    return str1
   else:
    return str1
print(notpoor(a))
print(notpoor(b))
