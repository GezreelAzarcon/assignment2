#Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
#Display the maximum number of apples that you can buy and the remaining money that you will have.
#Display the output in the following format.
#You can buy ___ apples and your change is ___ pesos.
money = int(input('How much money do you have? '))
price = int(input('How much is the apple? '))
maxNum = money // price
change = money % price
print(f'You can buy {maxNum} apples and your change is {change} pesos.')