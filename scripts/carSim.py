from re import M
import time as tm

running = True

t = 0.0
dT = 0.1

#details car: m = mass, F = force, v = speed, x = distance travelled
m = 600.0
F = 800.0
v = 0.0
x = 0.0



while (running):
    # t = t + dT
   t += dT
   print("Time: ", t)
   a = F / m
   dV = a * dT
   v = v +dV
   print("v: ", v)
   dX = v * dT
   x = x + dX
   print("x: ", x)
   tm.sleep(0.1)
   if x >= 100.0:
     running = False

print ("Duration: ", t, " seconds")



