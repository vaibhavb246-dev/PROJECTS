file_name="task.txt"
def load_tasks():
    tasks=[]
    try:
        with open(file_name,"r") as f:
            for line in f:
                line=line.strip()
                if line:
                    title,done=line.strip("|")
                    tasks.append({"title":title,"done":done==True})
    except FileNotFoundError:
        pass
    return tasks


def save_tasks(tasks):
    "write al tasks to the file "
    with open (file_name,"w") as f:
        for task in tasks:
            f.write(f"{task["title"]}|{task["done"]}\n")

def show_tasks(tasks):
    if not tasks:
        print("\n no tasks yet.")
        return
    print("\n -----your task-----")
    for i,task in enumerate(tasks,start=1):
        mark="[x]" if task["done"] else"[]"
        print(f"{i}.{mark} {task['title']}")

def add_tasks(tasks):
    title=input("Enter the task:").strip()
    if title=="":
        print("task cannot be empty.")
        return
    tasks.append({"title":title, "done":False})
    print("Task added")

def get_task_number(tasks):
    try:
        num= int(input("Enter the task number:"))
        if 1<=num <=len(tasks):
            return num-1
        print("Number out of range.")
    except ValueError:
        print("please enter the valid number.")

    return None

def complete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    index=get_task_number(tasks)
    if index is not None:
        tasks[index]["done"]=True
        print("Marked as done.")

def delete_tasks(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    index=get_task_number(tasks)
    if index is not None:
        removed=tasks.pop(index)
        print(f"Deleted:{removed['title']}")


def show_summary(tasks):
    total = len (tasks)
    done=sum(1 for t in tasks if t["done"])
    print(f"\n total: {total}| Done: {done}|pending: {total-done}")


def main():
    tasks=load_tasks()
    while True:
        print("\n=====TO DO MANAGER=======")
        print("1. view tasks")
        print("2.Add tasks")
        print("3,Mark task as done")
        print("4.Delete tasks")
        print("5.Summary")
        print("6.Save & exit")

        choice=input("Enter the choice(1-6):").strip()

        if choice=="1":
            show_tasks(tasks)
        elif choice=="2":
            add_tasks(tasks)
        elif choice=="3":
            complete_task(tasks)
        elif choice=="4":
            delete_tasks(tasks)
        elif choice=="5":
            show_summary(tasks)
        elif choice=="6":
            save_tasks(tasks)
            print("Saved.GoodBye")
            break
        
        else:
            print("Invalid choice try again.")

    

if __name__== "__main__":
    main()






