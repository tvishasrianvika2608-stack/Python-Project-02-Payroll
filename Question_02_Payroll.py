
name = input("Enter employee name: ")

basic = float(input("Enter basic salary: "))
allowances = float(input("Enter allowances: "))

hours = float(input("Enter overtime hours: "))
rate = float(input("Enter overtime rate per hour: "))

incentives = float(input("Enter incentives: "))

overtime = hours * rate

gross = basic + allowances + overtime + incentives

if gross <= 20000:
    deduction = 0

elif gross <= 50000:
    deduction = (gross - 20000) * 0.05

else:
    deduction = 1500 + (gross - 50000) * 0.10

net_salary = gross - deduction

print("\n----- EMPLOYEE SALARY STATEMENT -----")
print("Employee Name:", name)
print("Basic Salary:", basic)
print("Allowances:", allowances)
print("Overtime Payment:", overtime)
print("Incentives:", incentives)
print("Gross Salary:", gross)
print("Total Deduction:", deduction)
print("Net Salary:", net_salary)
print("-------------------------------------")
