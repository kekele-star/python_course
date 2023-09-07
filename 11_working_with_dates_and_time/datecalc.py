# import time
# print(time.gmtime(0))

# time_here = time.localtime()
# print(time_here)

#  # you can choose to employ the use of time_here[] ortime_here.tm_year. They both do the same thing
# print("Year: ", time_here[0], time_here.tm_year)
# print("Month: ", time_here[1], time_here.tm_mon)
# print("Dat: ", time_here[2], time_here.tm_mday)

import time
from time import time as my_timer
import random

input("Please enter to start")

wait_time = random.randiant(1,6)
time.sleep(wait_time)
start_time = my_timer()
input("Please enter to stop")

end_time = my_timer()

print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))

print(f"Your reaction time was {end_time - start_time} seconds")


