from random import randint
for i in range(0,3,1):
  x=int(input("Enter number between 0 and 10 : "))
  if (x==randint(1,9)):
     print("You win")
     exit()
  else :
    print("Try again")
print("You lose, game over")