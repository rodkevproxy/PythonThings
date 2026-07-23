# compound interest calculator 
# Using a while True will allow us to enter 0 values 

principle = 0 
rate = 0 
time = 0 

while True: 
    principle = float(input("Enter the amount "))#
    if principle < 0: 
        print("Principle can not be less than 0")#
    else:
        break

while True:
    rate = int(input("Enter the rate "))
    if rate < 0: 
        print("The rate can not be less than 0")
    else:
        break

while True: 
    time = int(input("Enter the time "))
    if time < 0: 
        print("Time can not be less than 0")
    else: 
        break 

total = principle * pow((1 + rate / 100), time)


print(principle)
print(rate)
print(time)

print(f"Balance after {time} year/s: {total:.2f}")

