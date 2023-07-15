print (" SORTING ARRAY ")
print (" Please enter number as aray sentece as much as you want ")
print (" when your sentences are finish enter 'done' as input ")

array = []

while True : 
    vurudi = input (" Please enter the input : ")

    if vurudi == "done" :
        break

    else :
        n = int ( vurudi )
        array.append ( n )

array.sort ()
print ( array )