class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        
        
    def enter_money(self):
        money_to_enter = int(input("Enter the amount of money that you want to deposit: "))
        self.balance = self.balance + money_to_enter

    def withdraw_money(self):
        money_to_withdraw = int(input("Enter the amount of money that you want to withdraw: "))
        self.balance = self.balance - money_to_withdraw

class SavingsAccount(BankAccount):
    def __init__(self, balance, min_balance):
        super().__init__(balance)
        self.min_balance = min_balance


    def withdraw_money(self):
        money_to_withdraw = int(input("Enter the amount of money that you want to withdraw: "))

        if self.balance - money_to_withdraw >= self.min_balance:
            self.balance = self.balance - money_to_withdraw
        else:
            print("You cannot withdraw that amount because it would go below the minimum balance.")


saving_account = SavingsAccount(1000,100)
saving_account.withdraw_money()
print(saving_account.balance)

