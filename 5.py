print (" LET'S CALCULATE GREATEST COMMON DIVISOR 🤓🧐 ")

first = int ( input (" Please enter first number : "))
second = int ( input (" Please enter second number : "))

first_divisor = []
second_divisor = []
common_divisor = []
GCD = 1

for i in range ( 1 , first + 1 ) :
    if first % i == 0 :
        first_divisor.append ( i )
    
print (" First number's divisors are : ", first_divisor )

for i in range ( 1 , second + 1 ) :
    if second % i == 0 :
        second_divisor.append ( i )

print (" Second number's divisors are : ", second_divisor )

for i in range ( len( first_divisor )) :
    if first_divisor[ i ] in second_divisor :
        common_divisor.append ( first_divisor[ i ] )

for i in range ( len ( common_divisor )) :
    GCD = GCD * common_divisor[ i ]

print (" The Greatest Cmmon Divisor of these two numbers is : ", GCD)