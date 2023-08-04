import random

secret_number = random.randint(1, 100)
response = None

while response != secret_number:
  response = int(input("Guess a number between 1 and 100: "))

  if response > secret_number:
    print("Your guess is too big! Guess again.")
  elif response < secret_number:
    print("Your guess is too small! Guess again.")
  else:
    print("You have guessed wisely")
