import time
from time import time as my_timer
import random

# some key functions in action
# print(time.gmtime(0))
#
# # named tuple of time struct
# print(time.localtime())
#
# # number of seconds since 1/1/1970
# print(time.time())
#
# time_here = time.localtime()
# print(time_here)
#
# # demonstrating that the struct is a tuple that can be addressed by position or name
# print("Year:", time_here[0], time_here.tm_year)
# print("Month:", time_here[1], time_here.tm_mon)
# print("Day:", time_here[2], time_here.tm_mday)

# reaction time game
input("Press enter to start")

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input("Press enter to stop")

end_time = my_timer()

print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))

print("Your reaction time was {} seconds".format(end_time - start_time))
