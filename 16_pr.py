import time

#timestamp = int(time.strftime('%H'))
timestamp = int(input('enter time: '))

if 5 <= timestamp < 12:
    print("Good Morning!")

elif 12 <= timestamp < 18:
    print("Good Afternoon")

elif 18 <= timestamp < 21:
    print("Good Evening!")

else:
    print("Good Night")