print (" 🐍 PRINT SNAKE 🐍 ")

length = int ( input (" please enter the length of snake : "))
n  = length % 2 

if  n == 0 :
    tekrar = int ( length / 2 )
    for i in range ( tekrar ) :
        print ("*", end = "#" )

else :
    tekrar = int ( length / 2 )
    for i in range (tekrar) :
        print ("*", end = "#")
    print ("*")