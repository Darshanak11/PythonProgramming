class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added.')

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f'Task "{task}" removed.')
        else:
            print(f'Task "{task}" not found.')

    def show_tasks(self):
        print("Tasks:", ", ".join(self.tasks) if self.tasks else "No tasks available.")

if __name__ == "__main__":
    manager = TaskManager()
    while True:
        choice = input("1. Add 2. Remove 3. Show 4. Exit: ")
        if choice == '1':
            manager.add_task(input("Enter task: "))
        elif choice == '2':
            manager.remove_task(input("Enter task to remove: "))
        elif choice == '3':
            manager.show_tasks()
        elif choice == '4':
            break
