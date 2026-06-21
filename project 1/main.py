# expense tracker project

expensesList = [] # list of all expenses

print(" Welcome to Expense Tracker : Kharcha kam kiya karo ... ")

while True:
    print(" ======== MENU ========")
    print(" 1. Add Expenses ")
    print(" 2. View All Expenses ")
    print(" 3. View Total Expenses ")
    print(" 4. Exit ")

    choice = int(input("Plese Enter Our Choice : "))

# 1. add expenses :
    if(choice == 1):
        date = input("Enter the Date : ")
        category = input("Enter the Category (Food, Travel, Mackup,... ) :")
        description = input("Enter Short Detials... : ")
        amount = float(input("Enter the Amount : "))

        expense = {
            "date" : date,
            "category" : category,
            "description" : description,
            "amount" : amount
        }

        expensesList.append(expense)

        print(" \n DONE, Expense is add Succesfully...")

# 2. View All Expense
    elif(choice == 2):
        if( len( expensesList ) == 0  ):
            print("No Expense Added...")
        else:
            print(" ======== All Expense ======== ")
            count = 1 
            for eachKarcha in expensesList: 
                print(f" Kharcha Number  {count}. : {eachKarcha["date"]}, {eachKarcha["category"]}, {eachKarcha["description"]}, {eachKarcha["amount"]} ")
                count = count + 1

# 3. View Total Expense 

    elif(choice == 3):
        total = 0 
        for eachKarcha in expensesList:
            total = total + eachKarcha["amount"]

        print("\n Total Kharcha : ",total)

# 4. Exit

    elif(choice == 4):
        print(" Dhanyawad used to System.... ")
        break

    else:
        print("Invalid Choice & Try Again.....")
        