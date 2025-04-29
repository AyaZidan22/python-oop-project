from office import Office
from person import Person
from employee import Employee
from car import Car

samy = Employee(
    name="samy",
    money=100,
    mood="Neutral",
    healthRate="75%",
    id=2,
    car=Car("Fiat 128"),
    email="samy@example.com",
    salary=10000,
    distanceToWork=20,
)
aya = Employee(
    name="aya",
    money=100,
    mood="Neutral",
    healthRate="75%",
    id=5,
    car=Car("BMW"),
    email="aya@example.com",
    salary=15000,
    distanceToWork=20,
)
zedan = Employee(
    name="zedan",
    money=100,
    mood="Neutral",
    healthRate="75%",
    id=10,
    car=Car("Tesla"),
    email="zedan@example.com",
    salary=15000,
    distanceToWork=20,
)
samy.refuel()
samy.drive(distance=20.0,velocity=60.0)

iti=Office("ITI-Smart-Village",[samy,aya])
print(iti.check_lateness(empId=2,moveHour=6))
iti.hire(zedan)
print(f"Number of employees after: {Office.employeesNum}")
print("The employees list is now:")
for emp in iti.employees:
    print(f"{emp.name} with id: {emp.id}")
print(iti.fire(empId=5))
print(f"Number of employees after: {Office.employeesNum}")

print(f"{samy.name} is an Employee, He works in ITI and he has a car. He goes everday except weekends to {iti.name} office by his {samy.car.name} car")