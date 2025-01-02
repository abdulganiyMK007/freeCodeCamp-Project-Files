##############################
# Build a Budget App Project #
##############################
"""
Complete the Category class. It should be able to instantiate objects based on
different budget categories like food, clothing, and entertainment. When objects
are created, they are passed in the name of the category. The class should have
an instance variable called ledger that is a list. The class should also contain
the following methods:

- A deposit method that accepts an amount and description. If no description is
    given, it should default to an empty string. The method should append an object
    to the ledger list in the form of {'amount': amount, 'description': description}.
- A withdraw method that is similar to the deposit method, but the amount passed
    in should be stored in the ledger as a negative number. If there are not
    enough funds, nothing should be added to the ledger. This method should return
    True if the withdrawal took place, and False otherwise.
- A get_balance method that returns the current balance of the budget category
    based on the deposits and withdrawals that have occurred.
- A transfer method that accepts an amount and another budget category as arguments.
    The method should add a withdrawal with the amount and the description
    'Transfer to [Destination Budget Category]'. The method should then add a
    deposit to the other budget category with the amount and the description
    'Transfer from [Source Budget Category]'. If there are not enough funds,
    nothing should be added to either ledgers. This method should return True
    if the transfer took place, and False otherwise.
- A check_funds method that accepts an amount as an argument. It returns False
    if the amount is greater than the balance of the budget category and
    returns True otherwise. This method should be used by both the withdraw
    method and transfer method.
- When the budget object is printed it should display:
    + A title line of 30 characters where the name of the category is centered
        in a line of * characters.
    + A list of the items in the ledger. Each line should show the description
        and amount. The first 23 characters of the description should be displayed,
        then the amount. The amount should be right aligned, contain two decimal
        places, and display a maximum of 7 characters.
    + A line displaying the category total.

Here is an example usage:

    food = Category('Food')
    food.deposit(1000, 'deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more food for dessert')
    clothing = Category('Clothing')
    food.transfer(50, clothing)
    print(food)

And here is an example of the output:

*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96

"""
"""
Besides the Category class, create a function (outside of the class) called create_spend_chart that
takes a list of categories as an argument. It should return a string that is a bar chart.

    # The chart should show the percentage spent in each category passed in to the function. 
    # The percentage spent should be calculated only with withdrawals and not with deposits. 
    # Down the left side of the chart should be labels 0 - 100. 
    # The 'bars' in the bar chart should be made out of the 'o' character. 
    # The height of each bar should be rounded down to the nearest 10.
    # The horizontal line below the bars should go two spaces past the final bar. 
    # Each category name should be written vertically below the bar. 
    # There should be a title at the top that says 'Percentage spent by category'.

This function will be tested with up to four categories.

Look at the example output below very closely and make sure the spacing of the output
matches the example exactly.

Percentage spent by category
100|
 90|
 80|
 70|
 60| o
 50| o
 40| o
 30| o
 20| o  o
 10| o  o  o
  0| o  o  o
    ----------
     F  C  A
     o  l  u
     o  o  t
     d  t  o
        h
        i
        n
        g
"""

N_CHARS = 30            # number of characters for title line
N_CHARS_DESC = 23       # number of characters for description
N_CHARS_AMT = 7         # number of characters for amount
N_DECIMAL_PLACE = 2     # number of decimal places for amount
FILL_CHAR = "*"         # fill characters for title line
BARS_CHAR = 'o'         # character in which the 'bars' in the bar chart are made out of.


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def transfer(self, amount, OtherCategory):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {OtherCategory.name}')
            OtherCategory.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def get_balance(self):
        return sum(map(lambda value: value['amount'], self.ledger))

    def get_sum_withdrawals(self):
        withdrawals = filter(lambda value: value['amount'] < 0, self.ledger)
        sum_withdrawals = abs(sum(map(lambda minus: minus['amount'], withdrawals)))
        return sum_withdrawals

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

    def __repr__(self):
        return f"Category(category='{self.name}')"

    def __str__(self):
        display = self.name.center(N_CHARS, FILL_CHAR) + "\n"
        # self.ledger[0]['description'] = 'initial ' + self.ledger[0]['description']
        for value in self.ledger:
            display += (value['description'][:N_CHARS_DESC].ljust(N_CHARS_DESC)
                        + str(round(value['amount'], N_DECIMAL_PLACE))[:N_CHARS_AMT].rjust(N_CHARS_AMT) + "\n")
        display += "Total: " + str(self.get_balance())
        return display


def create_spend_chart(categories):
    percentage_points = []
    for each_category in categories:
        withdrawals = each_category.get_sum_withdrawals()
        balance = each_category.get_balance()
        perc = round((withdrawals / (withdrawals + balance)) * 10)
        percentage_points.append((perc, each_category.name))
    return create_bar_chart(percentage_points)


def create_bar_chart(percent_points):
    print(percent_points)
    width = 5 + len(percent_points) * 3 - 2

    for i in range(width):
        for j in range(10, -1, -1):
            print(i, ':', j)

food = Category('Food')
food.deposit(2000, 'deposit')
food.withdraw(600, 'groceries')
food.withdraw(250, 'restaurant and more food for dessert')

clothing = Category('Clothing')
food.transfer(500, clothing)
clothing.withdraw(200, 'singlet')
clothing.withdraw(150, 'handkerchief and face towel')

auto = Category('Auto')
auto.deposit(10000, 'deposit')
auto.withdraw(2000, 'Withdraw Auto 1')


chilling = Category('Chilling')
chilling.deposit(500, 'deposit')
auto.transfer(1000, chilling)
chilling.withdraw(300, 'movie ticket and popcorn')
chilling.withdraw(500, 'outings: beach, fun fair')
chilling.withdraw(500, 'drinks')
chilling.transfer(200, auto)

# print(food, '\n')
# print(clothing, '\n')
# print(auto, '\n')
# print(chilling, '\n')

create_spend_chart([food, clothing, auto, chilling])