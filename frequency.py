from collections import Counter, OrderedDict
class frequency(Counter, OrderedDict):
    pass
x  =int(input("Enter the number of words you wsh to put: "))
y  = frequency(input("enter the word: ") for _ in range(x))
print("The number of distinct words is: ",len(y))
print("Frequency of the words in the order they were entered: ",*y.values())
