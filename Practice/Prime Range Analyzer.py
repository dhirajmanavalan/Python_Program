"""first 10 - 30 how many prime count it // 11 13 17 19 23 29"""

# a = int(input("enter number: "))

# for i in range(2,a):
#     if(a%i==0):
#         print("Not prime")
#         break
# else:
#     print("prime")


# A = int(input("Enter input1 : "))
# B = int(input("Enter input2 : "))

# count =0

# ''' i ** 0.5 eg: i=25--> i**0.5 = 5'''
# for i in range(A,B+1):
#     if i > 1:
#         prime = True
#         for j in range (2,int(i**0.5)+1):
#             if i%j==0:
#                 prime = False
#                 break
#         if prime:
#             count = count+1


# A = int(input("Enter input1 : "))
# B = int(input("Enter input2 : "))

# # for(int i=0 ;i*i<=b;i++) --> java

# count = 0
# for i in range(10,30):
#     if i*i<=B:
#         count = count+1
#     else:
#         pass

# print(count)


A = int(input("Enter input1 : "))
B = int(input("Enter input2 : "))
count = 0
for i in range(A, B + 1):
    if i > 1:
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
print(count)
