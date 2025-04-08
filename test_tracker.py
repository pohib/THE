import unittest
from tracker import ExpenseTracker

class TestExpenseTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = ExpenseTracker()
    
    def test_add_expense(self):
        self.tracker.add_expense(100, "Еда", "Обед")
        self.assertEqual(len(self.tracker.get_expenses()), 1)
        
        with self.assertRaises(ValueError):
            self.tracker.add_expense(-50, "Транспорт")
    
    def test_get_total(self):
        self.tracker.add_expense(100, "Еда")
        self.tracker.add_expense(200, "Транспорт")
        self.assertEqual(self.tracker.get_total(), 300)
    
    def test_get_by_category(self):
        self.tracker.add_expense(100, "Еда", "Обед")
        self.tracker.add_expense(50, "Еда", "Кофе")
        self.tracker.add_expense(200, "Транспорт")
        
        food_expenses = self.tracker.get_by_category("Еда")
        self.assertEqual(len(food_expenses), 2)
        self.assertEqual(sum(e['amount'] for e in food_expenses), 150)

if __name__ == "__main__":
    unittest.main()