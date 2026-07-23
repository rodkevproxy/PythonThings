import time 

# Anther option to count backward is by setting first the "max value" then the min value and then as a step we set 
# -1 so it will count backwards. this is an alternative to enclosing the line of code inside a reversed method 

my_time = int(input("Enter the time in seconds"))

for x in range(my_time, 0, -1):
    seconds = x % 60 
    minutes = x / 60
    hours = x / 3600
    print (f"{hours}{minutes}{seconds}")
    time.sleep(1)

print("Time is up!")


 

