class Car:
    def __init__(self, name,F,m):
        #Forward Force
        self.name = name    
        self.F = F
        self.m = m
        self.x = 0.0
        self.v = 0.0

    def move(self, dT):
        a = self.F / self.m
        dV = a * dT
        self.v = self.v +dV
        print("v: ",self.name, self.v)
        dX = self.v * dT
        self.x = self.x + dX
        print("x: ",self.name, self.x)
        
   
   
   
   