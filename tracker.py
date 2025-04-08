from typing import List, Dict

class ExpenseTracker:
    def __init__(self):
        self.expenses: List[Dict] = []
    
    def add_expense(self, amount: float, category: str, description: str = "") -> None:
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        
        expense = {
            'amount': amount,
            'category': category,
            'description': description
        }
        self.expenses.append(expense)
    
    def get_expenses(self) -> List[Dict]:
        return self.expenses.copy()
    
    def get_total(self) -> float:
        return sum(expense['amount'] for expense in self.expenses)
    
    def get_by_category(self, category: str) -> List[Dict]:
        return [exp for exp in self.expenses if exp['category'].lower() == category.lower()]