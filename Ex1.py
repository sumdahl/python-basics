from operator import ne


employee_name = input("Enter your name : ")
number_of_hours = int(input("Input number of hours you worked : "))
hourly_rate = int(input("Input the hourly rate you agreed to work : "))
net_salary = number_of_hours * hourly_rate
print("Net Salary of " +employee_name+ " : ", net_salary)
