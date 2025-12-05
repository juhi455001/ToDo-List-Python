import sys
tasks=[]
def Show_menu():
    print("--------To-Do List-----")
    print("1 View task\n 2 Add task \n 3 complete task \n 4 remove task \n 5 Exit")
    print("===============")
def view_tasks():
    if not tasks:
        print("No task available!!")    
    for i,t in enumerate(tasks,start=1):
        print(f"{i}. {t}")    
def Add_task():
    task = input("Enter new task")       
    tasks.append(task)
    print("Task added!!")
def Complete_task():
    view_tasks()   
    if not tasks:
        return
    num=int(input("Enter tasks number to mark compelete"))
    if 1<=num<=len(tasks):
        tasks[num-1]=tasks[num-1]+ "  completed"
    else:
        print("Invalid number!!")    
def Delete_task():
    view_tasks()
    num=int(input("Enter task number to delete"))
    if 1<=num<=len(tasks):
        removed=tasks.pop(num-1)
        print(f"Deleted: {removed}")
    else:
        print("Invalid number")    
    

while True:
    Show_menu()
    ch=input("enter your choice!!")    
    if ch=="1":
        view_tasks()
    elif ch=="2":
        Add_task()
    elif ch=="3":
        Complete_task()
    elif ch=="4":
        Delete_task()
    elif ch=="5":
        print("GoodBye")  
        sys.exit()             
    else:
        print("Invalid choice")
            