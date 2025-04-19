import json
import os
import sys

TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

def add_task(tasks):
    desc = input("Введіть опис задачі: ").strip()
    if desc:
        tasks.append({ 'description': desc, 'done': False })
        save_tasks(tasks)
        print(f"Задача '{desc}' додана.")
    else:
        print("Опис не може бути порожнім.")

def view_tasks(tasks):
    if not tasks:
        print("Список задач порожній.")
        return
    print("\nПоточні задачі:")
    for idx, task in enumerate(tasks, 1):
        status = "+" if task['done'] else "-"
        print(f"{idx}. [{status}] {task['description']}")

def mark_done(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Введіть номер задачі для зміни статусу: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]['done'] = not tasks[num-1]['done']
            save_tasks(tasks)
            state = 'виконана' if tasks[num-1]['done'] else 'не виконана'
            print(f"Задача '{tasks[num-1]['description']}' позначена як {state}.")
        else:
            print("Неправильний номер.")
    except ValueError:
        print("Введіть, будь ласка, число.")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Введіть номер задачі для видалення: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)
            save_tasks(tasks)
            print(f"Задача '{removed['description']}' видалена.")
        else:
            print("Неправильний номер.")
    except ValueError:
        print("Введіть, будь ласка, число.")

def tasks_menu(tasks):
    while True:
        view_tasks(tasks)
        print("\n1. Додати завдання")
        print("2. Позначити як виконане/невиконане")
        print("3. Видалити завдання")
        print("4. Повернутись до головного меню")

        choice = input("Оберіть дію (1-4): ").strip()
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            mark_done(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            break
        else:
            print("Введене некоректне значення.")

def main():
    tasks = load_tasks()
    while True:
        print("TO-DO LIST")
        print("Ласкаво просимо! Для початку роботи введіть відповідне число в консоль для виклику функції.\n")

        print("1. Переглянути задачі")
        print("2. Вийти")

        choice = input("Оберіть дію (1-2): ").strip()
        if choice == '1':
            tasks_menu(tasks)
        elif choice == '2':
            print("Дякую за використання додатку. Гарного дня!")
            sys.exit()
        else:
            print("Введене некоректне значення.")

if __name__ == '__main__':
    main()
