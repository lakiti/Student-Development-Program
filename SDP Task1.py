#WAP for ADD, MUL, DIV, SUB
a = int(input('Enter the first digit= '))
b = int(input('Enter the second digit= '))
print('Addition= ', a+b)
print('Multiplication= ',a*b)
print('Division= ',a/b)
print('Substraction= ',a-b)


#WAP to calculate simple interest
P = int(input('Enter the Principle amount= '))
R = int(input('Enter the Rate of interest= '))
T = int(input('Enter the Time= '))
si = (P * T * R)/100
print('The Simple Interest is:', si)


#WAP for swapping using third variable
x = int(input('Enter the first digit= '))
y = int(input('Enter the second digit= '))
print('value of x before swapping:',x)
print('value of y before swapping:',y)
temp = x
x = y
y = temp
print('value of x after swapping:', x)
print('value of y after swapping:', y)


#WAP for swapping without using third variable
a = int(input('Enter the first element= '))
b = int(input('Enter the second element= '))
print('value of a before swapping:',a)
print('value of b before swapping:',b)
a = a + b
b = a - b
a = a - b
print('value of a after swapping:', a)
print('value of b after swapping:', b)


#WAP to calculate gross sal from basic sal(HRA=30%, TA=40%, DA=20%)
BS=int(input('Enter basic salary:'))
HRA=BS*0.3
TA=BS*0.4
DA=BS*0.2
gross_sal=BS+HRA+TA+DA
print('gross salary:',gross_sal)


#WAP to find circumference of circle
r=5
pi = 3.14
Circumference = 2*pi*r
print('the circumference of a circle is ', Circumference)


#WAP to find area of circle
r=5
pi = 3.14
Area = pi*r*r
print('The area of a circle is ', Area)


#WAP to enter height of user in feets and convert it into inches and centimiter
height_feet = int(input('Enter Your height= '))
height_inches = height_feet * 12
height_centimeter = height_inches * 2.54
print("The height in inches:", height_inches)
print("The height in centimiters:", height_centimeter)


#WAP to reverse three number 123 = 321
num = 123
rev = 0
while(num > 0):
    a = num % 10
    rev = rev * 10 + a
    num = num // 10
print(rev)


#WAP to  take centigrate temperature and convert it into fahrenheit temperature f=1.8*c+240
centigrate = int(input("Enter the Temperature in Centigrate: "))
Fahrenheit = (1.8*centigrate) + 240
print("Temperature in fahrenheit: ", Fahrenheit)