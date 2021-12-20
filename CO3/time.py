import time
print("Current time in sec:",time.time())
print("Current time:",time.ctime())
print("Time after 30 sec:",time.ctime(time.time()+30))
t=time.localtime()
print("Time:",t)
print("Current Year:",t.tm_year)
print("Current month:",t.tm_mon)
print("Current day:",t.tm_mday)
print("Current Hour:",t.tm_hour)
print("Current Number of day:",t.tm_yday)
print("Current week:",t.tm_wday)

