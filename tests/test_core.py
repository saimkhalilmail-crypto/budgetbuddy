"""Example tests for BudgetBuddy. Two small tests to copy from in Lesson 12."""

import unittest

from features import core
from features import reports

class TestCore(unittest.TestCase):
    def test_balance(self):
        data = {"starting_balance": 50.0, "transactions": [
            {"id": 1, "description": "Bus pass", "amount": -2.5, "category": "transport"},
            {"id": 2, "description": "Allowance", "amount": 20.0, "category": "income"},
        ]}
        self.assertEqual(core.balance(data), 67.5)

    def test_add_transaction_gives_a_new_id(self):
        data = {"transactions": [{"id": 1, "description": "t", "amount": 5.0, "category": "general"}]}
        tx = core.add_transaction(data, "New thing", -3.0)
        self.assertEqual(tx["id"], 2)
        self.assertEqual(len(data["transactions"]), 2)

    def test_monthly_summary(self):
        data = {"transactions": [
            {"id": 1, "description": "t1", "amount": 5.0, "category": "general", "date": ("2024-1-5")},
            {"id": 1, "description": "t2", "amount": -8.0, "category": "general", "date": ("2024-1-23")},
            {"id": 1, "description": "t3", "amount": -7.0, "category": "general", "date": ("2024-2-12")},
            {"id": 2, "description": "t4", "amount": 13.0,"category": "general","date": ("2024-2-15")},
        ]}
        summary = reports.monthly_summary(data)
        self.assertIn((2024, 1), summary)
        self.assertIn((2024, 2), summary)
        self.assertEqual(summary[(2024, 1)]["income"], 5.0)
        self.assertEqual(summary[(2024, 1)]["spending"], -8.0)
        self.assertEqual(summary[(2024, 2)]["income"], 13.0)
        self.assertEqual(summary[(2024, 2)]["spending"], -7.0)
if __name__ == "__main__":
    unittest.main()
