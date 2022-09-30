import random
cnumbar=random.randrange(1,100)
numbar=int(input("Enter the Guessing number:----"))
if(cnumbar>numbar):

    print("Computer numbar is",cnumbar)
    print("Your numbar is too low")
elif(numbar>cnumbar):

     print("Computer numbar is",cnumbar)
     print ("your numbar is too high")
else:  
  print("Computer numbar is",cnumbar)
  print("Your numbar is same  with Computer number")
