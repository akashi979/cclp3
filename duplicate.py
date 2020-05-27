string = input("Enter String: ")
result = "".join(dict.fromkeys(string))
print("After removing duplicates: ",result)
