city = input("Enter the city your city name: ")
temp = float(input("Enter the temperature in Celsius: "))


if temp >= 50:
        print(" Weather: It is dangerously hot!!")
elif temp >= 40:
        print(" Weather: Its a good day to catch a tan!!")
elif temp >= 30:
        print(" Weather: It's cold get a cup of hot chocolate!!")

import datetime
import calendar

now = datetime.datetime.now()
print("City:", city)
print("Time now:",now)


print(calendar.calendar(now.year))