# Enhanced Bank Account Management System
# 🏦 Data Structures to Store Information
from datetime import datetime
account_holders = []  # Account names
accounts = [] # Account numbers (added by mе)
balances = []   # Account balances
transaction_histories = []  # Account transaction logs
loans = []            # Account loan details

MAX_LOAN_AMOUNT = 10000
INTEREST_RATE = 0.03

def display_menu():
    """Main menu for banking system."""
    print("\n🌟 Welcome to Enhanced Bank System 🌟")
    print("1️⃣ Create Account")
    print("2️⃣ Deposit Money")
    print("3️⃣ Withdraw Money")
    print("4️⃣ Check Balance")
    print("5️⃣ List All Accounts")
    print("6️⃣ Transfer Funds")
    print("7️⃣ View Transaction History")
    print("8️⃣ Apply for Loan")
    print("9️⃣ Repay Loan")
    print("🔟 Identify Credit Card Type")
    print("0️⃣ Exit")

def create_account(first, middle, last, account, balance):
    """1. Create a new account."""
    current_time = datetime.now()
    trans_time = current_time.strftime('%D, %H:%M:%S')
    gen_trans = [account, f"{trans_time}, debit account opened"]
    transaction_histories.append(gen_trans)
    gen_name = [f'{last}, {first} {middle}', account]
    account_holders.append(gen_name)
    accounts.append(account)
    gen_bal = [account, balance]
    balances.append(gen_bal)
    loans.append([account, 'Loan balance, term, principal, '
                           'min. payment:',0, 0, 0, 0])
    # initial account balance should be $0.00
    print(f'Account holder: {first} {middle} {last}')
    print(f'Account number: {account}')
    print(f'Initial balance: ${balance:.2f}')

def deposit(account, money_in):
    """2. Deposit money into an account."""
    current_time = datetime.now()
    trans_time = current_time.strftime('%D, %H:%M:%S')
    gen_trans = [account, f'{trans_time}, ${money_in:.2f}, deposit']
    if account in accounts and money_in > 0:
        for i, item in enumerate(balances):
            if item[0] == account:
                item[1] = item[1] + money_in
                balance = item[1]
                transaction_histories.append(gen_trans)
                print(f'Deposit: ${money_in:.2f}')
                print(f'Balance: ${balance:.2f}')
                break
    else:
        if account not in accounts:
            print('❌ Invalid account number.')
        elif account in accounts and money_in <= 0:
            print('❌ Invalid deposit amount.')

def withdraw(account, money_out):
    """3. Withdraw money from an account."""
    current_time = datetime.now()
    trans_time = current_time.strftime('%D, %H:%M:%S')
    gen_trans = [account, f'{trans_time}, ${money_out:.2f}, withdrawal']
    if account in accounts and money_out > 0:
        for i, item in enumerate(balances):
            if item[0] == account and money_out <= item[1]:
                item[1] = item[1] - money_out
                balance = item[1]
                transaction_histories.append(gen_trans)
                print(f'Withdrawal: ${money_out:.2f}')
                print(f'Balance: ${balance:.2f}')
                break
            elif item[0] == account and money_out > item[1]:
                print('❌ Insufficient funds.')
                break
    else:
        if account not in accounts:
            print('❌ Invalid account number.')
        elif account in accounts and money_out <= 0:
            print('❌ Invalid withdrawal amount.')

def check_balance(account):
    """4. Check balance of an account."""
    if account in accounts:
        current_time = datetime.now()
        trans_time = current_time.strftime('%D, %H:%M:%S')
        gen_trans = [account, f'{trans_time}, balance check']
        for i, item in enumerate(balances):
            if item[0] == account:
                balance = item[1]
                transaction_histories.append(gen_trans)
                print(f'Account balance: ${balance:.2f}\n{trans_time}')
                break
    else:
        print('❌ Invalid account number.')

def list_accounts(message):
    """5. List all account holders and details."""
    the_list = []
    for account in accounts:
        for i, name in enumerate(account_holders):
            for ind, bal in enumerate(balances):
                if name[1] == account and bal[0] == account:
                    balance = bal[1]
                    the_list.append(f'{name[0]}, Debit account: {account}, '
                                    f'Balance: ${balance:.2f}')
    sorted_list = sorted(the_list, key=lambda x: x[0])
    message = 'Accounts and balances:'
    print(message)
    print(*sorted_list, sep='\n')

def transfer_funds(sender_account, recipient_account, transfer_amount):
    """6. Transfer funds between two accounts."""
    if sender_account in accounts and transfer_amount > 0:
        current_time = datetime.now()
        trans_time = current_time.strftime('%D, %H:%M:%S')
        gen_trans = [sender_account, f'{trans_time}, ${transfer_amount:.2f}, '
                                     f'transfer sent']
        insufficient_funds = False
        for i, item in enumerate(balances):
            if sender_account == item[0] and transfer_amount <= item[1]:
                item[1] = item[1] - transfer_amount
                balance = item[1]
                transaction_histories.append(gen_trans)
                print(f'Transfer amount sent: ${transfer_amount:.2f}.')
                print(f'Sender\'s account balance: ${balance:.2f}')
                break
            elif sender_account == item[0] and transfer_amount > item[1]:
                insufficient_funds = True
                print('❌ Insufficient funds.')
                break
        for i, item in enumerate(balances):
            if insufficient_funds:
                break
            if recipient_account in accounts and recipient_account == item[0]:
                # for internal bank transfers
                item[1] = item[1] + transfer_amount
                balance = item[1]
                transaction_histories.append(gen_trans)
                print(f'Transfer amount received: ${transfer_amount:.2f}.')
                print(f'Recipient\'s account balance: ${balance:.2f}')
                break
            elif recipient_account not in accounts:  # for transfers between banks
                print('Interbank transfer')
                break
    else:
        if sender_account not in accounts:
            print('❌ Invalid sender account number.')
        if sender_account in accounts and transfer_amount <= 0:
            print('❌ Invalid transfer amount')

def view_transaction_history(account):
    """7. View transactions for an account."""
    if account in accounts:
        for i, item in enumerate(transaction_histories):
            if item[0] == account:
                trans = item[1]
                print(trans, sep='\n')
    else:
        print('❌ Invalid account number.')

def apply_for_loan(account, loan_amount, loan_term):
    """8. Allow user to apply for a loan."""
    current_time = datetime.now()
    trans_time = current_time.strftime('%D, %H:%M:%S')
    interest = loan_amount * INTEREST_RATE * loan_term
    if account in accounts and loan_amount <= MAX_LOAN_AMOUNT:
        for i, item in enumerate(loans):
            if item[0] == account:
                loan_balance = item[2] + loan_amount + interest
                item[2] = loan_balance
                item[3] = loan_term
                item[4] = loan_amount
                min_monthly_payment = loan_balance / loan_term / 12
                item[5] = min_monthly_payment
                gen_trans = [account, f'{trans_time}, loan application approved, '
                                      f'loan amount: ${loan_amount:.2f}']
                transaction_histories.append(gen_trans)
                print('Application approved.')
                print(f'Principal: ${loan_amount:.2f}')
                print(f'Interest: ${interest:.2f}')
                print(f'Total loan amount: ${loan_balance:.2f}')
                print(f'Minimum monthly payment: ${min_monthly_payment:.2f}')
                break
    else:
        if account not in accounts:
            print('❌ Please create a deposit account first.')
        elif account in accounts and loan_amount > MAX_LOAN_AMOUNT:
            gen_trans = [account, f'{trans_time}, loan application denied']
            transaction_histories.append(gen_trans)
            print('❌ Loan application denied - loan amount too high.')

def repay_loan(account, payment):
    """9. Allow user to repay a loan."""
    pass  # TODO: Add logic

def identify_card_type():
    """10. Identify type of credit card."""
    pass  # TODO: Add logic

def main():
    """Run the banking system."""
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        # Map choices to functions
        if choice == 1:
            create_account(first=input('Enter the first name: ').strip().capitalize(),
                           middle=input('Enter the middle name: ').strip().capitalize(),
                           last=input('Enter the last name: ').strip().capitalize(),
                           account=input('Enter the account number: ').strip(),
                           balance=float(input('Enter the initial balance: ').strip()))
        elif choice == 2:
            deposit(account=input('Enter the deposit account: ').strip(),
                    money_in=float(input('Enter the deposit amount: ').strip()))
        elif choice == 3:
            withdraw(account=input('Enter the withdrawal account: ').strip(),
                     money_out=float(input('Enter the withdrawal amount: ').strip()))
        elif choice == 4:
            check_balance(account=input('Enter the account: ').strip())
        elif choice == 5:
            list_accounts('Accounts and balances:')
        elif choice == 6:
            transfer_funds(sender_account=input("Enter sender's account: ").strip(),
                           recipient_account=input("Enter recipient's account: ").strip(),
                           transfer_amount=float(input('Enter transfer amount: ').strip()))
        elif choice == 7:
            view_transaction_history(account=input('Enter the account: ').strip())
        elif choice == 8:
            apply_for_loan(account=input("Enter applicant's debit account: ").strip(),
                           loan_amount=float(input('Enter loan amount: ').strip()),
                           loan_term=int(input('Enter loan term in years: ').strip()))
        elif choice == 9:
            repay_loan(account=input("Enter applicant's debit account: ").strip(),
                       payment=float(input('Enter payment amount: ').strip()))
        elif choice == 10:
            identify_card_type()
        elif choice == 0:
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Try again!")

if __name__ == "__main__":
    main()