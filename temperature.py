print("Temperature Conversion")
print("1.To Fahrenheit ")
print("2.To Celsius")

n=int(input())
if n==1:
    
    c = float(input("Enter temperature in celsius: "))
    f = 9/5 * c + 32
    print("Temperature in Fahrenheit is: ",f)
elif n==2:
         f = float(input("Enter temperature in fahrenheit: "))
         c = (f - 32) * 5/9
         print("Temperature in celsius is: ",c)
else:
        print("Invalid Input")
        
