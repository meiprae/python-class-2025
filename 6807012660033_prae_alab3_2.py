import random
secret = random.randint(1, 20)

for attempt in range(1,8):
    guess = int(input(f"Attempt {attempt}/8 guess the number: "))
    if guess == secret: 
        print("Correct! You win.")
        break
    elif guess < secret:
        print("Too high.")
    else:
        print("Too high.")
else:
    print(f"sorry, you've used all attempts. The number was: {secret}")