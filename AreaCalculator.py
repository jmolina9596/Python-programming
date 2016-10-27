##
# This program does absolutely everything you would want it to do with caculating area with only triangles and circles
###

from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()

print("The calculator is now starting up")

print ("Current time : %s/%s/%s%s:%s" % (now.month, now.day, now.year, now.hour, now.minute))
sleep(1)
hint = "Don't forget to include the correct units ! \nExiting..."

option = input("Enter C for Crcle or T for Triangle:")
option = option.upper()

if option == 'C':
  radius = float(input("Enter radius:"))
  area = pi * radius**2
  print("The pie is baking...")
  sleep(1)
  print ("Area: %.2f. /n%s" % (area, hint))
  
elif option == 'T':
  base = float(input("Enter base:"))
  height= float(input("Enter height:"))
  area = base * height
  print("Uni Bi Tri...")
  sleep(1)
  print("Area: %.2f. /n%s" % (area, hint))

else:
  print("You have entered garbage program wil exit")
  
