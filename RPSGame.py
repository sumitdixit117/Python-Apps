import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

images = [rock, paper, scissor]
print("What do you choose, Type 0 for Rock, 1 for Paper or 2 for Scissor.")
x = int(input("You choose: "))
print(images[x])

rndm = random.randint(0, 2)
print(f"Computer chose: {rndm}")

print(images[rndm])

if x == rndm:
    result = 0
elif x == 0 and rndm == 2:
    result = 1
elif x == 2 and rndm == 0:
    result = -1
elif x > rndm:
    result = 1
else:
    result = -1

if result == 0:
    print("Match Tie")
elif result == -1:
    print("You Lose")
else:
    print("You Win")
