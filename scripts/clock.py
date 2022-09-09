import time as tm

running = True

t = 0.0
dT = 0.1

while (running):
#   t = t + dT
   t += dT
   tm.sleep(0.1)
   print("Time: ", t)







