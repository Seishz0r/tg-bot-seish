from asyncio import tasks


class Task:

    def __init__(self, title, completed = False):
        self.set_task(title, completed)

    def set_task(self, title, completed):
        self.title = title
        self.completed = completed

    def mark_done(self):
        self.completed = True

    def __str__(self):
        status = "[+]" if self.completed else "[ ]"
        return f"{status} {self.title}"

class TaskManager:

    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)

    def show_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def complete_task(self, index):
        try:
            self.tasks[index - 1].mark_done()
        except IndexError:
            print("Задачи с таким номером нет!")

    def save_to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            for task in self.tasks:
                status = "1" if task.completed else "0"
                f.write(f"{status};{task.title}\n")

    def load_from_file(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                self.tasks.clear()
                for line in f:
                    status, title = line.strip().split(";")
                    completed = True if status == "1" else False
                    self.tasks.append(Task(title, completed))
        except FileNotFoundError:
            print("Файл не найден!")


manager = TaskManager()

while True:
    print("\n1 - Добавить")
    print("2 - Показать")
    print("3 - Завершить")
    print("4 - Сохранить")
    print("5 - Загрузить")
    print("0 - Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        title = input("Введите задачу: ")
        manager.add_task(title)

    elif choice == "2":
        manager.show_tasks()

    elif choice == "3":
        try:
            num = int(input("Введите номер задачи: "))
            manager.complete_task(num)
        except ValueError:
            print("Введите число!")

    elif choice == "4":
        filename = input('Введите название файла: ')
        manager.save_to_file(filename)

    elif choice == "5":
        filename = input('Введите название файла: ')
        manager.load_from_file(filename)

    elif choice == "0":
        break

    else:
        print("Неверный выбор!")