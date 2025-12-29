# units = int(input("Enter unit: "))

# if units<=100:
#     for _ in range(1,101):
#         units = units+3

# if units >=101 and units<=200:
#     for _ in range(1,101): 
#         units = units+5
        
# if units >=201 and units<=300:
#     for _ in range(1,101):
#         units = units+8
        
# # if units>300:
# #     for _ in units:
# #         units=units((units+10)/100)
# print(units)

units = int(input("enter unit: "))

bill = 0

if units<=100:
    bill = units*3

elif units<=200:
    bill = (100*3) + (units-100)*5
    
else:
    bill = (100*3) + (100*5) + (units-200)*8

if units>300:
    bill = bill+(bill*10/100)

print(int(bill))