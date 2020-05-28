k=int(input("Enter an number:  "))
def sequence(n):
  if n < 1:
    return 0
  else:
    return n + sequence(n - 2)
print(sequence(k))
