print (" LET's CALCULATE LEAST COMMON MULTIPLER 🤓🧐")

first = int ( input (" Please enter first number : "))
second = int ( input (" Please enter second number : "))

a_multipler = []
b_multipler = []

if first <= second :
    a = first
    b = second

elif first > second :
    a = second
    b = first

for i in range ( 1 , b + 1 ) :
    a_multipler.append ( a * i )
    b_multipler.append ( b * i )

    n = i - 1 

    if a_multipler[n] in b_multipler :
        LCM = a_multipler[n]
        break

print (" The Least Cmmon Multipler of these two numbers is : ", LCM)