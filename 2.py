print (" print an array ")
print (" 💯 the maximum length of array is 100 💯 ")

import random

n = int ( input (" Please the length of array : "))
array = []

while n > 100 :
    print (" 📌 ERROR 📌 ")
    print (" please enter lower  number ")
    n = int ( input (" your number must 100 or lower : "))

while len ( array ) < n :
    x = random.randint ( 0 , 99)
    if x in array :
        array.remove ( x )

    array.append ( x )

print (" the array is : ", array )