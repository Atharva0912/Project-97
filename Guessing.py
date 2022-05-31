guess = int(input("Pls enter a number between 1 to 9: "))
n = 8
chances = 0
while chances <5:
    if guess>n:
        chances = chances+1
        print(guess,"is a very large number, try a number less than",guess)
        guess = int(input("Pls enter a number between 1 to 9: "))
    elif guess<n:
        chances = chances+1
        print(guess,"is a very small number, try a number greater than", guess)
        guess = int(input("Pls enter a number between 1 to 9: "))
    elif guess == n:
        print("You Win!!!")
        break
if not chances <= 5:
    print("You loose! The actual number is: ", n)

