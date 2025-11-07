def add_task(task):
    with open("todo.txt", "a") as file:
        file.write(f"{task}\n")

def show_tasks():
    with open("todo.txt", "r") as file:
        tasks = file.readlines()
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task.strip()}")

add_task("Finish Python project")
show_tasks()
