import time
def countdown(end, start=1):
    for i in range(start, end+1):
        print(i)
        time.sleep(1)
countdown(10)
print('Done!!')