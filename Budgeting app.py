class Category:
    def __init__(self, name):
        self.name = name
        self.category = []

    def withdraw(self, amount, description = ""):
        self.category.append({"amount": -amount, "description": description})

    def deposit(self, amount, description = ""):
        self.category.append({"amount": amount, "description": description})

    def get_balance(self):
        total = 0
        for item in self.category:
          total += item['amount']
        return total

    def transfer(self, amount, budget_category):
        self.withdraw(amount, f"Transfer to {budget_category.name}")
        budget_category.deposit(amount, f"Transfer from {self.name}")

    def __str__(self):
        output = self.balance.center(30, "*") + "\n"
        for item in self.category:
          output += f"{item['description'][:23].ljust(23)}{format(item['amount'], '.2f').rjust(7)}\n"
        output += f"Total: {format(self.check_balance(), '.2f')}"


Food = Category('Food')
Clothing = Category('Clothing')
Entertainment = Category('Entertainment')
Food.deposit(1000, "Posterity")
Food.withdraw(10.15, "Lunch")

print(Food)
print(Clothing)
print(Entertainment)
