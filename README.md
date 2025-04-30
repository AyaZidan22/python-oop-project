🧠 OOP Project – Office Simulation in Python
This project showcases core Object-Oriented Programming (OOP) concepts using Python through a simulation of an office environment. It demonstrates how classes interact to model real-life objects such as employees and their vehicles, and how lateness, refueling, and salary management are handled.

# Project Structure
![OOP Lab_page-0011](https://github.com/user-attachments/assets/33f4f1de-3baf-4dc9-b173-a35035dc5464)
![OOP Lab_page-0010](https://github.com/user-attachments/assets/5b7dbb99-e498-4f1d-88d5-a6e83ee72a6a)
![OOP Lab_page-0009](https://github.com/user-attachments/assets/eda5afbb-c97d-423e-98cf-6981b3afe3d7)
![OOP Lab_page-0008](https://github.com/user-attachments/assets/89ef8ea8-4362-4031-bee6-ed6f02610e13)
![OOP Lab_page-0007](https://github.com/user-attachments/assets/d5304aab-def3-4a25-bd20-12be8e70aa3d)
![OOP Lab_page-0006](https://github.com/user-attachments/assets/63559f4c-4b69-4250-bf4b-c426693bf967)
![OOP Lab_page-0005](https://github.com/user-attachments/assets/27e6a43a-1cdc-44b6-b37e-9ee15095e629)



# Key Features:
🚗 Driving simulation with fuel and velocity tracking
⛽ Refueling capability
⏱️ Lateness detection based on commute time and speed
👥 Employee management: Hiring and firing functionality
💵 Salary adjustments: Reward or deduct salary based on punctuality

# Example Usage

from office import Office
from employee import Employee
from car import Car

# Create employees
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

# Simulate actions
samy.refuel()
samy.drive(distance=20.0, velocity=60.0)

iti = Office("ITI-Smart-Village", [samy, aya])
print(iti.check_lateness(empId=2, moveHour=6))

iti.hire(zedan)
print(f"Number of employees after hiring: {Office.employeesNum}")
print("Current employee list:")
for emp in iti.employees:
    print(f"{emp.name} with ID: {emp.id}")

print(iti.fire(empId=5))
print(f"Number of employees after firing: {Office.employeesNum}")

print(f"{samy.name} is an employee who works at {iti.name}. He commutes daily (except weekends) using his {samy.car.name} car.")
