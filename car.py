class Car():
    def __init__(self,name,fuelRate=0,velocity=0):
        self.name=name
        self._fuelRate=fuelRate
        self._velocity=velocity
        self.cVelocity=0
    
    def run (self,velocity,distance):
        self.velocity=velocity
        while distance!=0 and self.fuelRate>0.5 and self.velocity!=0:
            if distance<10:
                distance=0
            elif distance>=10:
                distance-=10
                self.fuelRate-=self.fuelRate*0.1
                  
        self.stop(distance,velocity)        
        
    def stop(self,distance,velocity):
        self.cVelocity=velocity
        self.velocity=0
        if distance==0:
            print( "You have arrived")
        elif self.fuelRate==0:
            self.cVelocity=0
            print( f"There is no fuel, the remaining distance is {distance}")
        else:
            print( f"Invalid velocity value")

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        if 0 <= value <= 200:
            self._velocity = value
            return 1
        else:
            self._velocity = 0
            return 0
          
    @property
    def fuelRate(self):
        return self._fuelRate

    @fuelRate.setter
    def fuelRate(self, value):
        if 0 <= value <= 100:
            self._fuelRate = value                 
        else:
            self._fuelRate = 0




        


        