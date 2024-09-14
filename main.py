import random
print("One-Million-To-One")
print()
print("""Guess a number between 1 and 1,000,000 and I will tell you if you are too low, too high, or get it correct.""")
print()
print("Let's play!")
print()
correct_number = random.randint(1,1000000)
print()
count = 1
while True:
  guess = int(input("What is your guess? "))
  if guess == correct_number:
    print("Correct!")
    print("You are a winner! 🎉")
    print()
    if count == 1:
      print("It took you", count, "guess to get it correct")
      break
    else:
      print("It took you", count, "guesses to get it correct")
      break
  elif guess >= correct_number:
    print("Too high")
    print()
    count += 1
  elif guess <= 0:
    print("Now we'll never know what the answer is …")
    exit()
  else:
    print("Too low")
    print()
    count += 1
