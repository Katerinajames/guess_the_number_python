#https://codingnomads.com/blog/python-project-for-beginners-guess-the-number-game
#https://inventwithpython.com/chapter4.html
import random
i=random.randint(1,1000)

print(i)
print("--------------------------------------------")
print("I have a number between 1 and 1000")
print ("Can you guess my number?")
guess=None 
while guess !=i:
 guess=int(input ("Please type your first guess!!"))
 if i>guess:
	  print("Too low")
 if i<guess:
	  print("Too high")	 
 if i==guess:
	 print("Excellent! You guessed the number!")
	
 else:
	 print(" nope, sorry. try again!")
 
