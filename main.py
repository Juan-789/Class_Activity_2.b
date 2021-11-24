"""
Write a program that takes from the user a number A and B (A ≤ B). Print all numbers from A to B inclusively horizontally in ascending order.
"""
print ("Within what range do you want me to print numbers?")
numFirst = int(input("First number "))
numSecond = int(input("Second number "))
for i in range (numFirst, numSecond+1, 1):
  print (i,end=" ")
#Getts two numbers annd iterates all numbers withing that range