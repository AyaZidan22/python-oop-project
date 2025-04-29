🧠 OOP Project – Office Simulation in Python
This project showcases core Object-Oriented Programming (OOP) concepts using Python through a simulation of an office environment. It demonstrates how classes interact to model real-life objects such as employees and their vehicles, and how lateness, refueling, and salary management are handled.

📁 Project Structure
![OOP Lab_page-0011](https://github.com/user-attachments/assets/0904bce9-eb0f-40b5-b7bc-43f3a7e2ea90)
![OOP Lab_page-0010](https://github.com/user-attachments/assets/dc0e1eba-ea49-4eba-ae4a-4fbf9393eef8)
![OOP Lab_page-0009](https://github.com/user-attachments/assets/86bf2aef-9d18-4e3b-99a0-db3fcb6de266)
![OOP Lab_page-0008](https://github.com/user-attachments/assets/61937eb3-f0fd-45d1-bdbc-1c5fb3fc5d74)
![OOP Lab_page-0007](https://github.com/user-attachments/assets/443fef10-0e45-42c9-8a7e-2dc8b17e6f93)
![OOP Lab_page-0006](https://github.com/user-attachments/assets/b3d6ebec-f1aa-458d-b0e0-01a93cd315d6)
![OOP Lab_page-0005](https://github.com/user-attachments/assets/f8af2de1-87ac-4574-b591-f2f27eaa8432)

🚀 Key Features:
🚗 Driving simulation with fuel and velocity tracking
⛽ Refueling capability
⏱️ Lateness detection based on commute time and speed
👥 Employee management: Hiring and firing functionality
💵 Salary adjustments: Reward or deduct salary based on punctuality

🧪 Example Usage

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

📤 Sample Output

You have arrived
You're not Late
samy is rewarded, his new salary after reward is 10010
zedan is hired
Number of employees after hiring: 3
Current employee list:
samy with ID: 2
aya with ID: 5
zedan with ID: 10
Employee with ID 5 has been fired.
Number of employees after firing: 2
samy is an employee who works at ITI-Smart-Village. He commutes daily (except weekends) using his Fiat 128 car.
