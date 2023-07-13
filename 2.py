print (" print an array ")

import random

n = int ( input (" Please the length of array : "))
array = []

for i in range ( n ) :
    array.append ( random.randint ( 0 , 99 ) )

print (" the array is : ", array )