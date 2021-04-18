
class budget:
    """
    This is a budget app that allows for depositing funds to each of the categories, 
    withdrawing funds from each category,
    each category balance and transfer of balance between categories
    """
    
    #budget instance
    def __init__(self, category):   
        self.category = category
        self.ledger =list ()
       

    def deposit(self, amount, explanation = ''):
        """
        This is a deposit method that shows amount deposited and explaining
        what the deposit is meant for to which if none is given, it will default to an empty 
        string. It will also append object to the legder list.
        """
        self.ledger.append({'amount':amount, 'explanation': explanation})


    def withdrawal(self, amount, explanation = ''):
        """
        This is a withdrawal method that shows amount withdrawn which will append in the ledger as well,
        but in negative amount. It will also show if withdrawal took place or not in the True or False bool
        """
        if (self.get_funds(amount)):
            self.ledger.append({'amount':-amount, 'explanation': explanation})
            return True
        else:
            return False


    def transfer(self, amount, budget):
        """
        This function will show transfer of money between budget instances
        and will also return True or false is transfer took place.
        """
        if (self.get_funds(amount)):
            self.withdrawal(amount, "Transfer to" + budget.category)
            budget.deposit(amount, "Transfer from" + self.category)
            return True
        else:
            return False


    def check_funds():
        if(self.balance() >= amount):
            return True
        else:
            return False


    def balance(self):
        """
        This function will show total money left after
        deposit or withdrawal might have taken place
        """
        total_money = 0
        for item in self.ledger:
            total_money += item['amount']
        return total_money
    


food = Budget('Food', 1000)
savings = Budget('Savings', 1500)
entertainment = Budget('Entertainment', 800)
clothing = Budget('Clothing', 500)

# print(food.category + ' ' + str(food.amount))
# food.withdrawal()
