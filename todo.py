tasks = []

while True:
    task = input("Enter a task (or type 'done' to stop): ")

    if task == "done":
        break

    tasks.append(task)

print("\nYour Tasks:")

for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")
