from datetime import datetime, timedelta

class Office:
    employeesNum=0
    def __init__(self,name,employees):
        self.name=name
        self.employees=employees
        Office.employeesNum += len(employees)  
        
    def get_all_employees(self):
        return self.employees
    
    def get_employee(self,empId):
        for employee in self.employees:
            if employee.id==empId:
                return f"Employee with Id: {empId} is {employee}"
        return f"Employee with Id:{empId} is not found"
        
    def hire(self,employee):
        self.employees.append(employee)
        Office.employeesNum += 1
        print(f"{employee.name} is hired")


    def fire(self,empId):
        for i in range(len(self.employees)):
            if self.employees[i].id==empId:
                self.employees.pop(i)
                Office.employeesNum -= 1
                return f"Employee with ID {empId} has been fired."
        return f"No employee found with ID {empId}."
             
    def check_lateness(self,empId,moveHour):
        for employee in self.employees:
            if employee.id==empId:
                lateness_result = Office.calculate_lateness("09:00", moveHour, employee.distanceToWork, employee.car.cVelocity)
                if lateness_result is None:
                    return "Invalid velocity; lateness could not be checked."
                elif lateness_result:
                    print("You're Late")
                    return self.deduct(empId, 10)
                else:
                    print("You're not Late")
                    return self.reward(empId, 10)


    def deduct(self,empId,deduction):
        for employee in self.employees:
            if employee.id==empId:
                employee.salary-=deduction
                return f"{employee.name} is deducted, his new salary after deduction is {employee.salary}"
        
    def reward(self,empId, reward):
        for employee in self.employees:
            if employee.id==empId:
                employee.salary+=reward
                return f"{employee.name} is rewarded, his new salary after reward is {employee.salary}"

    @staticmethod
    def calculate_lateness (targetHourStr , moveHourStr, distance, velocity):
        moveHour = datetime.strptime(moveHourStr, "%H:%M")
        targetHour = datetime.strptime(targetHourStr, "%H:%M")

        if velocity <= 0 or velocity > 200:
            return None 
        
        timeAvaliable =targetHour - moveHour
        travelDuration = timedelta(hours=distance / velocity)

        if travelDuration<=timeAvaliable:
            return 0 #not late
        else:
            return 1  #late 

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num     
        

        
        

        
