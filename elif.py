num1 = input('enter your 1st number:')
num2 = input("enter your 2nd number:")

var1=int(num1)
var2=int(num2)

if (var1>var2):
    print("yes")
    print('1st number greater than 2nd number')
elif(var1==var2):
    print('1st number is equal to 2nd number')
elif(var1<var2):
    print('1st number less than 2nd number')