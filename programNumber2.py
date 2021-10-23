#Create a program that will ask how many apples and oranges you want to buy.
#Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
#Display the output in the following format.
#The total amount is ______.
print('Apple is 20 pesos')
apple = int(input('How many apple do you want to buy? '))
print('Orange is 25 pesos')
orange = int(input('How many oranges do you want to buy? '))
totalApple = apple * 20
totalOrange = orange * 25
total = totalApple + totalOrange
print(f'The total amount is {total}')

