import random;


random_num = random.randint(1,100)
tries = 0 
guess = int(input("Pick a number, any number: "))
while(random_num != guess):
  if(guess > random_num):
   print("Too High")
  elif(guess < random_num):
    print("Too Low")
  tries += 1
  guess = int(input("Nope, Try Again: "))

print(f'You Guessed Correct! It Took You {tries} tries!')

