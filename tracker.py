from typing import List, Dict

class ExpenseTracker:
    def __init__(self):
        """Функция инициализирует трекер расходов с пустым списком"""
        self.expenses: List[Dict] = []
    
    def add_expense(self, amount: float, category: str, description: str = "") -> None:
        """Функция добавляет новый расход в трекер
        
        Args:
            amount: Сумма расхода (должна быть положительной)
            category: Категория расхода (например "Еда", "Транспорт")
            description: Описание расхода (необязательное)
        
        Raises:
            ValueError: Если сумма не положительная
        """
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        
        expense = {
            'amount': amount,
            'category': category,
            'description': description
        }
        self.expenses.append(expense)
    
    def get_expenses(self) -> List[Dict]:
        """Функция возвращает копию списка всех расходов
        
        Returns:
            Список словарей с информацией о расходах
        """
        return self.expenses.copy()
    
    def get_total(self) -> float:
        """Функция вычисляет и возвращает общую сумму всех расходов
        
        Returns:
            Сумма всех расходов в виде числа с плавающей точкой
        """
        return sum(expense['amount'] for expense in self.expenses)
    
    def get_by_category(self, category: str) -> List[Dict]:
        """Функция фильтрует расходы по указанной категории
        
        Args:
            category: Категория для фильтрации (регистронезависимая)
        
        Returns:
            Список расходов только из указанной категории
        """
        return [exp for exp in self.expenses if exp['category'].lower() == category.lower()]