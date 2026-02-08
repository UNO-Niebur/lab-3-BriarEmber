#TempConvert.py
#Name:Devyn Conaway
#Date:2/7/2026
#Assignment:Lab 3


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  tempF = float(input("Please input a temperature in Fahrenheit."))

  tempC = ((tempF - 32) / 1.8)
  tempC = round(tempC, 1)

  print(tempF, "is ", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()
