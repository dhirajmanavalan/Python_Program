salary = int(input("enter salary:"))
late = int(input("enter late commers:"))
absent = int(input("enter absent days:"))

deduction = 0
if late > 10:
    deduction += 10
elif late > 5:
    deduction += 5

if absent > 2:
    deduction += 5

final_salary = salary - (salary * deduction / 100)
print(int(final_salary))