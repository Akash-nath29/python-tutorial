#find the triangle weather the triangle is an  acute angle or obtuse angle

A = int(input("enter the number of 1 : "))
B = int(input("enter the number of 2 : "))
C = int(input("enter the number of 3 : "))

if(A+B+C <= 90):
    print("acute angle")
if(  90>A<=180 or 90>B<=180 or 90>C<=180 ):
    print("obtuse angle")
if(A+B+C > 180):
    print("NOT TRIANGLE")
    breakpoint
if(A==90 or B==90 or C==90):
    print("carpenter's triangle")