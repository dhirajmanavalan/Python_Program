password = input("enter password: ")

digit = False
uppercase = False

for ch in password:
    if ch>='0' and ch<='9':
        digit = True
    elif ch>='A' and ch<='Z':
        uppercase = True
        
if digit and uppercase and len(password)>=8:
    print('Strong')
else:
    print('Weak')