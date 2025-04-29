from person import Person

class Employee(Person):
    def __init__(self,name,money,mood,healthRate,id,car,email,salary,distanceToWork):
        super(Employee,self).__init__(name,money,mood,healthRate)
        self.id=id
        self.car=car
        self.salary=salary
        self.email=email
        self.distanceToWork=distanceToWork

    def __str__(self):
        return self.name     
    
    def work(self,hours):
        if hours==8:
            self.mood="Happy"
            print(f"This Employee is {self.mood}")
        elif hours>8:
            self.mood="Tired"
            print(f"This Employee is {self.mood}")
        else:
            self.mood="Lazy"
            print(f"This Employee is {self.mood}")          
    
    def drive(self,distance,velocity):
        self.distanceToWork=distance
        self.car.run(velocity,distance)
    
    def refuel(self,gasAmount=100):
        new_fuel = self.car.fuelRate + gasAmount
        self.car.fuelRate = new_fuel

    def send_email(self):
        pass
        


