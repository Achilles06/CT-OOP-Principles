class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget

    # Getter for category_name
    @property
    def category_name(self):
        return self.__category_name

    # Setter for category_name
    @category_name.setter
    def category_name(self, name):
        if isinstance(name, str) and name:
            self.__category_name = name
        else:
            raise ValueError("Category name must be a non-empty string")

    # Getter for allocated_budget
    @property
    def allocated_budget(self):
        return self.__allocated_budget

    # Setter for allocated_budget
    @allocated_budget.setter
    def allocated_budget(self, budget):
        if isinstance(budget, (int, float)) and budget > 0:
            self.__allocated_budget = budget
            self.__remaining_budget = budget  # Reset remaining budget to new allocated budget
        else:
            raise ValueError("Budget must be a positive number")

    # Method to add an expense
    def add_expense(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            if amount <= self.__remaining_budget:
                self.__remaining_budget -= amount
            else:
                raise ValueError("Expense amount exceeds remaining budget")
        else:
            raise ValueError("Expense amount must be a positive number")

    # Method to display budget category summary
    def display_category_summary(self):
        print(f"Category: {self.__category_name}")
        print(f"Allocated Budget: ${self.__allocated_budget:.2f}")
        print(f"Remaining Budget: ${self.__remaining_budget:.2f}")

# Example usage
food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()
