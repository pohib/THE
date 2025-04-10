from tracker import ExpenseTracker

def display_menu():
    """Функция выводит в консоль главное меню приложения"""
    print("\nМеню:")
    print("1. Добавить расход")
    print("2. Показать все расходы")
    print("3. Показать общую сумму")
    print("4. Показать расходы по категории")
    print("5. Выйти")

def handle_add_expense(tracker: ExpenseTracker):
    """Функция обрабатывает добавление нового расхода"""
    try:
        amount = float(input("Введите сумму: "))
        category = input("Введите категорию: ")
        description = input("Введите описание (необязательно): ")
        tracker.add_expense(amount, category, description)
        print("Расход успешно добавлен!")
    except ValueError as e:
        print(f"Ошибка: {e}")

def handle_show_all_expenses(tracker: ExpenseTracker):
    """Функция отображает все расходы"""
    expenses = tracker.get_expenses()
    if not expenses:
        print("Нет добавленных расходов.")
    else:
        print("\nВсе расходы:")
        for i, exp in enumerate(expenses, 1):
            print(f"{i}. {exp['category']}: {exp['amount']:.2f} - {exp['description']}")

def handle_show_total(tracker: ExpenseTracker):
    """Функция отображает общую сумму расходов"""
    total = tracker.get_total()
    print(f"\nОбщая сумма расходов: {total:.2f}")

def handle_show_by_category(tracker: ExpenseTracker):
    """Функция отображает расходы по выбранной категории"""
    category = input("Введите категорию: ")
    expenses = tracker.get_by_category(category)
    if not expenses:
        print(f"Нет расходов в категории '{category}'")
    else:
        print(f"\nРасходы в категории '{category}':")
        total = 0
        for i, exp in enumerate(expenses, 1):
            print(f"{i}. {exp['amount']:.2f} - {exp['description']}")
            total += exp['amount']
        print(f"Итого: {total:.2f}")

def main():
    """Основная функция, запускающая приложение"""
    tracker = ExpenseTracker()
    print("Добро пожаловать в трекер расходов!")
    
    handlers = {
        "1": lambda: handle_add_expense(tracker),
        "2": lambda: handle_show_all_expenses(tracker),
        "3": lambda: handle_show_total(tracker),
        "4": lambda: handle_show_by_category(tracker)
    }
    
    while True:
        display_menu()
        choice = input("Выберите действие: ")
        
        if choice in handlers:
            handlers[choice]()
        elif choice == "5":
            print("До свидания!")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()