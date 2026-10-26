import csv
from datetime import date

def menu():
    print("===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total")
    print("4. Category Total")
    print("5. Delete")
    print("6. Exit")

def rewrite_file(expenses):
    with open("expenses.csv" , "w",newline="") as file:
            writer = csv.writer(file)
            for e in expenses:
                row=[e["Date"],e["Category"],e["Amount"],e["Note"]]
                writer.writerow(row)


def load_data(expenses):
    try:
        with open("expenses.csv", "r",newline="") as file:
            lines=csv.reader(file)
            for line in lines:
                try:
                    if(len(line)==4):
                        expense_date,category,amount,note=line
                    elif(len(line)==3):
                         expense_date,category,amount=line
                         note="-"
                    else:
                        print("Skipping invalid row")
                        continue
                    date_object=date.fromisoformat(expense_date)
                    expense={"Date": date_object,"Category":category,"Amount":int(amount),"Note":note}
                    expenses.append(expense)
                except ValueError:
                    print("Skipping invalid row")
    except FileNotFoundError:
        pass

def add_expense(expenses):
    today_date=date.today()
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
    note=input("Write note: ").strip()
    if not note:
         note="-"

    while True: 
            try:
                date_text=(input("Enter Date(YYYY-MM-DD, Enter for today):").strip())
                if not date_text:
                     _date=today_date
                else:
                    _date= date.fromisoformat(date_text)
            except ValueError:
                    print("Incorrect Date")
                    continue
            if _date>today_date:
                    print("Can't add future date")
                    continue
            break

    expenses.append({"Date":_date,"Category":category,"Amount":amount,"Note":note})
    expenses.sort(key=lambda e :e['Date'])
    rewrite_file(expenses)
        
def view_expenses(expenses):
    expenses.sort(key=lambda e :e['Date'])
    if len(expenses)==0:
        print("No expenses have been recorded")
    else:
        for index,e in enumerate(expenses,start=1):
            print(f"{index}) {e['Date']} Category: {e['Category']}  Amount : {e['Amount']} PKR , Note : {e['Note']}")

def calculate_total(expenses):
  return sum(e["Amount"] for e in expenses)


def category_total(expenses):
    if len(expenses)==0:
        print("No expenses have been recorded")
        return
    
    totals={}
    for e in expenses:
        category=e["Category"]
        totals[category]=totals.get(category,0)+e["Amount"]
    
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

def delete_expense(expenses):
    if len(expenses)==0:
            print("No expenses have been recorded")
            return
    
    view_expenses(expenses)
    while True:
            try:
                index=int(input("Enter Index to delete expense:"))
            except ValueError:
                    print("Index must be Integer")
                    continue
            if index<=0 or index>len(expenses):
                    print(f"Enter a number between 1 and {len(expenses)}")
                    continue
            break
    confirmation=input(f"Are you sure to delete an expense at #{index} (y/n): ").strip().lower()
    if(confirmation=="y"):
        expenses.pop(index-1)
        rewrite_file(expenses)
        print(f"Expense deleted at #{index}")
    else:
         print("Cancelled")
    


def main():
    expenses=[]
    load_data(expenses)
    while(True):
        menu()
        try:
            choice=int(input("Choose an option:"))
        except ValueError:
            print("Choose Between 1-6")
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
                delete_expense(expenses)
            elif choice==6:
                print("Exiting.......")
                break
            else:
                print("Invalid Choice!")
    
if __name__ == "__main__":
    main()