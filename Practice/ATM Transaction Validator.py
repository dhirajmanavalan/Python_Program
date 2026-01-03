balance = int(input('Enter balance: '))

number_of_transactions = int(input('Enter number of transactions: '))

for _ in range(number_of_transactions):
    amount = int(input("Enter amount: "))
    
    if amount<=balance and amount%100==0:
        balance = balance-amount
        print('Success')
    
    else:
        print('Failed')
        
print(balance)