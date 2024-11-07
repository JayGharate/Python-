import json

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)

def show_tasks(tasks):
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task['task']} - {'Done' if task['done'] else 'Pending'}")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "done": False})
    print("Task added.")

def mark_task_done(tasks):
    show_tasks(tasks)
    try:
        task_idx = int(input("Enter the task number to mark as done: ")) - 1
        tasks[task_idx]['done'] = True
        print("Task marked as done.")
    except IndexError:
        print("Invalid task number.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        task_idx = int(input("Enter the task number to delete: ")) - 1
        tasks.pop(task_idx)
        print("Task deleted.")
    except IndexError:
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n1. Show tasks\n2. Add task\n3. Mark task as done\n4. Delete task\n5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
