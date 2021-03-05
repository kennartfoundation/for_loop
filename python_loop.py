count = 0

while count < 9:
    print('Number', count)
    count = count +1

print('good by')



import random

n = 20

to_be_guessed = int(n* random.random()) + 1
guess = 0

while guess != to_be_guessed:
    guess = int(input('New number:   '))
    if guess > 0:
        if guess > to_be_guessed:
            print('number too large')
        elif guess < to_be_guessed:
            print('Number too small')
    else:
        print('Sorry that you are giving up!')
        break
else:
    print('Congratulation. You made it')
    
num = int(input('Please enter your number:  '))

factorial = 1

if num < 0:
    print('Number must be positive')
elif num == 0:
    print("factorial = 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
print(factorial)

print('Welcom to Kenn bank of ghana')
restart = ('Y')
chances =3
balance = 67.14
while chances >=0:
    pin = int(input("Please enter your 4 digit Pin:  "))
    if pin == (1234):
        print('You entered your pin correctly\n')
        while restart not in ('n', 'No', 'no', 'N'):
            print("please press 1 for your balance\n")
            print("please press 2 to make a withdrawl\n")
            print('please press 3 to pay in \n')
            print('please press 4 to return card\n')
            option = int(input('What would you like to choose?: '))
            
            if option == 1:
                print('your balance is Gh', balance, '\n')
                restart = input('Would you like to go back?  ')
                if restart in ('n', 'No', 'no' 'N'):
                    print('thank you')
                    break
                
            elif option ==2:
                option2 = ('y')
                withdrawl = float(input('How much would you like to withdraw? \nGh10/Gh20/Gh40/Gh50/Gh33'))
                if  withdrawl in [10, 20, 40, 60, 80, 100]:
                    balance = balance -withdrawl
                    print('\nYour balance is now Gh', balance)
                    restart = input('Would you like to go back?  ')
                    if restart in ('n', 'No', 'no' 'N'):
                        print('thank you')
                        break
                elif withdrawl !=[10, 20, 40, 60, 80, 100]:
                    print('Invalid Amount, please Re-try\n')
                    restart = ('y')
                elif withdrawl == 1:
                    withdrawl = float(input('Please enter Desired amount:  '))
                
                elif option == 3:
                    Pay_in = float(input('How much would you like to pay in?  '))
                    balance = balance + Pay_in
                    print('\nYour balance is now Gh', balance)
                    restart = input('Would you lik to go back? ')
                    if restart in ('n', 'No', 'no' 'N'):
                        print('thank you')
                        break
                    
                elif option == 4:
                    print('Please wait whilst your car is returne................\n')
                    print('Than you for your sercice')
                    break
                else:
                    print('Plese enter a correct number.  \n')
                    restart = ('y')
    elif pin !=('1234'):
        print('Incorrect Password')
        chances = chances - 1
        if chances == 0:
            print('\nNo more tries')
            break
                    
#use a for loop over a collection
Months = ["Jan","Feb","Mar","April","May","June"]
for i, m in enumerate (Months):
		print(i, m)