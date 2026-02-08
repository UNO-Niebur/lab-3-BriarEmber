#ApproxPi.py
#Name:Devyn Conaway
#Date:2/7/2026
#Assignment:Lab 3
import math
import time


#PLEASE NOTE - This is an optional, extra credit portion of the lab.

def main():
  realPi = math.pi
  decimal_input = int(input("Please pick decimal precision up to 10."))
  #ask user for decimal percision (up to 10)

  start = time.time()
  #calculate pi using the approximation technique
  #Loop until the level of percision is reached
  approxPi = 4/1
  sign = -1
  denom = 3
  while round(approxPi, decimal_input) != round(realPi, decimal_input):
    print(approxPi)
    approxPi = approxPi + (sign * 4 / denom)
    
    sign = sign * -1
    denom = denom + 2

  end = time.time()

  elapsedTime = end - start
  print(elapsedTime)

if __name__ == '__main__':
  main()
