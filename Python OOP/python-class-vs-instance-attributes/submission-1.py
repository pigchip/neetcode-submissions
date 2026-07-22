class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_accounts = 0
    total_balance = 0

    def __init__(self,name,balance) -> None:
        self.name = name
        self.__balance = balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance
        return

    @property
    def get_name(self):
        return f"{self.name}'s balance: {self.__balance}"

        

# TODO: Create two accounts
# TODO: Print the information using the mentioned format
a1 = BankAccount("Alice", 1000)
a2 = BankAccount("Bob", 2000)

print(a1.get_name)
a2.get_name

