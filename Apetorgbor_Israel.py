a=int(input("number : "))
b=int(input("till : "))
count=0
while count<b:
    count=count+1
    table=count*a
    print(a, '*',count, '*',table)
    if count=='b':
        input("Enter any key to quit : ")