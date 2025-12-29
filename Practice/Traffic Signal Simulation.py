time = int(input("enter the time: "))

t = time%90

if t<=30:
    print('RED')
    
elif t>=31 and t<=45:
    print('YELLOW')

elif t>=46 and t<=90:
    print('GREEN')