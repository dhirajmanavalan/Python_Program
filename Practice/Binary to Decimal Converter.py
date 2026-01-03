binary = input("Enter binary number: ")
decimal = 0
power = 0
for digit in binary[::-1]:    
    decimal += int(digit) * (2 ** power) 
    power += 1
print(decimal)

'''
y we are taking digit input becuz we want to perform right to left

Digit (R→le) |Power of 2 |Value
1| 2 power 0 | =1

'''