n = int(input("Enter the number:\n"))
rev = 0

while n > 0:
    rev = rev * 10 + n %10
    n = n // 10     
print(f"The reversed number is : {rev}")

