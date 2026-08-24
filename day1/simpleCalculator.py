boolean=True
while boolean:
    print("----------Calculator---------")
    a=int(input("Enter your 1 number: "))
    b=int(input("Enter your 2 number: "))
    c=input("Choose your operator {+,-,*,/}: ")
    result=0
    if c=='+':
        result=a+b
    elif c=='-':
        result=a-b
    elif c=='*':
        result=a*b
    elif c=='/':
        result=a/b
    else:
        print("invalid input")

    print(f"result {a} {c} {b} ={result}")

    print("--------Calculator----------")
    cont=input("do you want continue ot not Y(or)N: ")
    if cont=='N' or cont=='n':
        boolean=False
