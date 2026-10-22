import csv
from datetime import date

def menu():
    print("===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total")
    print("4. Category Total")
    print("5. Exit")

def save_data(_date,_category,_amount):
    with open("expenses.csv" , "a",newline="") as file:
        writer = csv.writer(file)
        row=[_date,_category,_amount]
        writer.writerow(row)
                   

def load_data(expenses):
    try:
        with open("expenses.csv", "r",newline="") as file:
            lines=csv.reader(file)
            for line in lines:
                try:
                    expense_date,category,amount=line
                    date_object=date.fromisoformat(expense_date)
                    expense={"Date": date_object,"Category":category,"Amount":int(amount)}
                    expenses.append(expense)
                except ValueError:
                    print("Skipping invalid row")
    except FileNotFoundError:
        pass

def add_expense(expenses):
    category=input("Select Category:").lower().strip()

    while not category:
        print("Category can't be empty")
        category=input("Select Category:").lower().strip()
    while True: 
        try:
            amount=int(input("Enter Amount:"))
        except ValueError:
                print("Amount must be Integer")
                continue
        if amount<=0:
                print("Amount must be greater than zero")
                continue
        break

    _date=date.today()   
    expenses.append({"Date":_date,"Category":category,"Amount":amount})
    save_data(_date,category,amount)
        
def view_expenses(expenses):
    if len(expenses)==0:
        print("No expenses have been recorded")
    else:
        for e in expenses:
            print(f" Date : {e['Date']} Category: {e['Category']}  Amount : {e['Amount']} PKR")

def calculate_total(expenses):
  return sum(e["Amount"] for e in expenses)


def category_total(expenses):
    totals={}
    for e in expenses:
        category=e["Category"]
        totals[category]=totals.get(category,0)+e["Amount"]

    if len(expenses)==0:
            print("No expenses have been recorded")
    else:
        for category,amount in totals.items():
            print(f"Category : {category} Amount: {amount} PKR")


def show_total(expenses):
    print(f"Total Amount Spend : {calculate_total(expenses)} PKR" )
    print("Total Expenses :", len(expenses))
    print(f"Average : {show_average(expenses):.2f}")

def show_average(expenses):
    if(len(expenses)>0):
        return calculate_total(expenses)/len(expenses)
    return 0

def main():
    expenses=[]
    load_data(expenses)
    while(True):
        menu()
        try:
            choice=int(input("Choose an option:"))
        except ValueError:
            print("Choose Between 1-5")
        else:
            if choice==1:
                add_expense(expenses)
            elif choice==2:
                view_expenses(expenses)
            elif choice==3:
                show_total(expenses)
            elif choice==4:
                category_total(expenses)
            elif choice==5:
                print("Exiting.......")
                break
            else:
                print("Invalid Choice!")
    
if __name__ == "__main__":
    main()