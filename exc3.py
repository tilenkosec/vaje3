import helper3

# 1. Create an input where user inputs number of groceries that he/she wants to buy.
# Save input into variable named your_input.
# If user inputs a number greater than 40, set your_input to 0.

your_input = int(input("How many groceries do you want to buy?: "))
if your_input > 40:
    your_input = 0
    print your_input

# Do not change line below.
price_list, groceries_list, money_available = helper3.buy(your_input)
#

# 2. Create a function that accepts price_list as a parameter and returns average.
def avgg(price_list): 
    average = (sum(price_list) / len(price_list))
    return average
average = avgg(price_list)
print "This is the average price:", average

print price_list, groceries_list
# 3. price_list and groceries_list are arrays that are the same length. groceries_list contains names of groceries. First price in
# price_list is a price for the first grocery in groceries_list and so on.
# Create a function that prints all groceries and its price like:
# food, 15
# clothes, 9
# ...

def combine(groceries_list, price_list):
    for i in range(len(groceries_list)):
        print(str(groceries_list[i]) + ", " + (str(price_list[i]))
#combine(groceries_list, price_list)

# 4. Use a function from task #2 and for every grocery prints if its price is above or below average.

for i in price_list:
    if (avgg(price_list)>i):
    print ("This one is above the average price: ", i)
    elif (avgg(price_list)<i):
    print ("This one is above the below price: ", i)