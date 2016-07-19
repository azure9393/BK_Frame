while 1:
    a=0
    b=0
    c = input("input : ")

    while a<c:
        a=a+1
        print "*"*a+" "*(c+1-a)+"*"*(c+1-a)
    while b<c:
        b=b+1
        print " "*(c-b)+"*"*b + " "*(b)+"*"*(c+1-b)
