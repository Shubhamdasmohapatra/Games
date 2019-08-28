import random

num = random.randint(1,101)

print(num)

guess_no = 1

guess = int(input('Enter a number between 1 and 100 '))

while guess != num:
    
    if guess < num:
        print('Choose a higher number ')
        guess = int(input('Enter a number between 1 and 100 '))
        guess_no = guess_no + 1
    
    elif guess > num:
        print('Choose a lower number ')
        guess = int(input('Enter a number between 1 and 100 '))
        guess_no = guess_no + 1
    
print(f'You guessed it right in {guess_no} guesses')

        
         
