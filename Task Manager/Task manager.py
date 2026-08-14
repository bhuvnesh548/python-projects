#Task manager
def task():
    tasks=[]
    i=True
    print("welcome to the task manager ")
    while i:
        print("\nMenu:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Exit")
        choice=int(input("Enter your choice: "))
        if choice==1:
            task_num=int(input("how many task you want to add : "))
            for i in range(1,task_num+1):
                task=input(f"{i}-Enter the task: ")
                tasks.append(task)
                print("Task added successfully")
        elif choice==2:
            if len(tasks)==0:
                print("No tasks available")
            else:
                for i in range(len(tasks)):
                    print(f"{i+1}. {tasks[i]}")
        elif choice==3:
            if len(tasks)==0:
                print("No tasks available to delete")
            else:
                for i in range(len(tasks)):
                    print(f"{i+1}. {tasks[i]}")
                del_task=int(input("Enter the task number to delete: "))
                if del_task>0 and del_task<=len(tasks):
                    tasks.pop(del_task-1)
                    print("Task deleted successfully")
                else:
                    print("Invalid task number")
        elif choice==4:
            i=False
            print("Exiting the task manager")
        else:
            print("Invalid choice")
task()