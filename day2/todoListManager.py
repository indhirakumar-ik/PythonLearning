print("----------Todo List-----------")
list=[]
while True:
    print("1.Add task")
    print("2.View Tasks")
    print("3.Delete task")
    print("4.Quit")
    Input=int(input("Enter your option: "))
    if Input==1:
        a=input("Enter your task: ").strip()
        list.append(a)
        print("Task is Added")
    elif Input==2:
        if list:
            print("------------Your Tasks-------")
            for i in list:
                print(i)
            print("----------Your Tasks----------")
        else:
            print("List is empty")
    elif Input==3:
        if list:
            print("Your Tasks")
            for i,task in enumerate(list,1):
                print(i)
            print("Your task want to delete")
            try:
                dele=int(input("enter your index no: "))-1
                list.pop(dele)
            except:
                print("Invalid Index")
        else:
            print("List is empty")
    elif Input==4:
        print("<-------The program is finished Good Bye------>")
        break
    else:
        print("Invalid Input")
    
        