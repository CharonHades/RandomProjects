tasks = []

def addTask():
    task = input("Enter a new task: ")
    tasks.append({"task":task, "completed":False})
    print("Task added!")

def viewTask():
    if not tasks:
        print("No tasks to show")
    else:
        print("\nHere are the tasks:\n")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task['task']} - {'Done' if task['completed'] else 'Not Done'}")

def markTask():
    viewTask()
    try:
        task_num = int(input("Enter the task number to mark as done: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]["completed"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number")
    except ValueError:
        print("Invalid input")

def deleteTask():
    viewTask()
    try:
        task_num = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks.pop(task_num)
            print("Task deleted!")
        else:
            print("Invalid task number")    
    except ValueError:
        print("Invalid input")
    
def main():
    while True:
        print("\n1. Add Task\n2. View Task\n3. Mark Task as Done\n4. Delete Task\n5. Exit")
        choice = input("Enter your choice: ")

        if choice=="1":
            addTask()
        elif choice=="2":
            viewTask()
        elif choice=="3":
            markTask()
        elif choice=="4":
            deleteTask()
        elif choice=="5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, Please Try Again!")
        
if __name__ == "__main__":
    main()