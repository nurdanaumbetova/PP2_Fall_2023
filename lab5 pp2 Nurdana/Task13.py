import random

print('Guess a number')
def Game():
    target=random.randrange(1,20)
    n=0
    while True:
        guess=int(input())
        if guess==target:
            print(f'Very good, Nurdanka!!! You are very smart, OMG!!! \n{n} trials')
            exit()
        if guess>target:
            print('Your guess is too big :(')
            n+=1
        elif guess<target:
            print('Your guess is too low :(')
            n+=1
        else:
            f"Congratulations! You guessed the number {guess} in {target} attempts."
        
            
cn=Game()
