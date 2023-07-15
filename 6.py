print (" LET's CALCULATE LEAST COMMON MULTIPLER 🤓🧐")

first = int ( input (" Please enter first number : "))
second = int ( input (" Please enter second number : "))

first_divisor = []
second_divisor = []
all_divisors = []
LCM = 1

for i in range ( 1 , first + 1 ) :
    if first % i == 0 :
        first_divisor.append ( i )

print (" First number's divisors are : ", first_divisor )

for i in range ( 1 , second + 1 ) :
    if second % i == 0 :
        second_divisor.append ( i )

print (" Second number's divisors are : ", second_divisor )



print (" The Least Cmmon Multipler of these two numbers is : ", LCM)