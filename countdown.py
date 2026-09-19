import time 
my_time = int(input("enter the time in seconds :"))

for x in range(my_time, 0 ,-1):
    minutes = (x%3600) // 60
    hour = x // 3600
    seconds = x % 60 
    print(f"{hour}:{minutes}:{seconds}" , end="\r") 
    time.sleep(1)

print("time's up")