#FIRST PART OF THE QUESTION
    #defining a function
def calculate_discount(price,discount_percent):
    if discount_percent >= 20:
        discount = discount_percent/100 * price
        final_price = price - discount 
        return final_price
    else:
        return price
print(calculate_discount(18000,50))

#SECOND PART OF THE QUESTION
    #prompting buyers to input the cost of the items
price = int(input("How much is the item:"))
discount_percent = int(input("What is the discount?"))
print(calculate_discount(price,discount_percent))