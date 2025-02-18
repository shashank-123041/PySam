name,eid,basic_salary,allowances,bonus_percentage=input("Enter the name of the employee: "),int(input("Enter the employee ID: ")),float(input("Enter the Salary of the Employee: ")),float(input("Enter the Special allowances of the Emplyee: ")),float(input("Enter the Bonus Percentage of the Emplyee: "))

gross_monthly_salary=basic_salary+allowances
annual_gross_salary=(gross_monthly_salary*12)
annual_gross_salary+=annual_gross_salary*bonus_percentage*0.01

print("Employee Name        : ",name)
print("Employee ID          : ",eid)
print("Basic salary         : ",basic_salary)
print("Special allowance    : ",allowances)
print("Bonus Percentage     : ",bonus_percentage,"%")
print("Gross Monthly Salary : ",gross_monthly_salary)
print("Annual Gross Salary  : ",annual_gross_salary)