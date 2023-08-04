import random


#Write a function where the computer guesses your number
def computer_guess(x):
  low = 1
  high = x
  feedback = 'correct'

  while feedback != 'correct':
    if low != high:
      guess = random.randint(low, high)
    else:
      guess = low
    feedback = input(f"Is {guess} too high (H) or too low (L) or correct (C) ?").lower()

    if feedback == 'h':
      high = guess - 1
    elif feedback == 'l':
      low = guess + 1

    print(f"The computer guessed your number, {guess} correctly!")

computer_guess(10)