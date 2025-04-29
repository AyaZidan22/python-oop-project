class Person:
    def __init__(self,name,money,mood,healthRate):
        self.name=name
        self.money=money
        self.mood=mood
        self.healthRate=healthRate

    def sleep(self,hours):
        if hours==7:
            self.mood="Happy"
            print(f"This Employee is {self.mood}")
        elif hours<7:
            self.mood="Tired"
            print(f"This Employee is {self.mood}")
        else:
            self.mood="Lazy"
            print(f"This Employee is {self.mood}")    

    def eat(self,meals):
        if meals==3:
            self.healthRate='100%'
            print(f"This Employee's health rate is {self.healthRate}")
        elif meals==2:
            self.healthRate='75%'
            print(f"This Employee's health rate is {self.healthRate}")
        elif meals==1:
            self.healthRate='50%'
            print(f"This Employee's health rate is {self.healthRate}")
        
    def buy(self,items):
        self.money=self.money-(10*items)
        print(f"This Employee's total money is now {self.money}")


             