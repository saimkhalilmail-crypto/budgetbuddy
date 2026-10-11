"""Core BudgetBuddy logic: transactions, balance, and small helpers."""
import datetime

def get_transactions(data):
    return data["transactions"]


def add_transaction(data, description, amount, category="general"):
    today = datetime.date.today()
    today_string = str(today)
    
    new_id = max((t["id"] for t in data["transactions"]), default=0) + 1
    tx = {"id": new_id, "description": description, "amount": amount, "category": category, "date": today_string}
    data["transactions"].append(tx)
    return tx


def balance(data):
    return round(data["starting_balance"] + sum(t["amount"] for t in data["transactions"]), 2)


def list_transactions(transactions, show=print):
    for t in transactions:
        show(str(t["id"]) + ". " + t["description"] + " (" + str(t["amount"]) + ")")


def transactions_by_category(transactions, category):
    return [t for t in transactions if t["category"] == category]


def count_by_category(transactions):
    counts = {}
    for t in transactions:
        name = t["category"]
        counts[name] = counts.get(name, 0) + 1
    return counts


def last_transaction(transactions):
    return transactions[len(transactions) - 1]


def total_spent(transactions):
    return round(sum(-t["amount"] for t in transactions if t["amount"] < 0), 2)


def average_transaction(transactions):
    if not transactions:
        return 0
    return round(sum(t["amount"] for t in transactions) / len(transactions), 2)
    
def monthly_summary(data):
    summary_report = {}
    all_transactions = data["transactions"]
    
    for t in all_transactions:
        month = t["date"]
        year = int(month.split("-")[0])
        month = int(month.split("-")[1])
        if (year, month) not in summary_report:
            summary_report[(year, month)] = {"income": 0, "spending": 0}
        if(t["amount"] >= 0):            
            summary_report[(year, month)]["income"] += t["amount"];
        else:
            summary_report[(year, month)]["spending"] += t["amount"]
    
    return summary_report
        