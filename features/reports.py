"""Reporting helpers for BudgetBuddy.

Heads up: this module is half-built on purpose. `account_summary` works, but
`category_report` is still a stub with a clear seam to finish (see the tickets).
"""


def account_summary(data):
    return data["account_name"] + ": " + str(len(data["transactions"])) + " transactions"


def category_report(data):
    # TODO(ticket): tally each transaction into a {category: total amount} dict and return it.
    # For now this returns an empty report so the menu never crashes.
    report = {}
    return report

def monthly_summary(data):
    summary_report = {}
    all_transactions = data["transactions"]
    
    for t in all_transactions:
        if "date" not in t:
            continue
        
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
        