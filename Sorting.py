'''sort ascn'''
# lst = [10,30,50,20,80]
# print(lst)
# lst.sort()
# print(lst)

'''sort desc'''
# lst = [10,30,50,20,80]
# print(lst)
# lst.sort(reverse=True)
# print(lst)

'''sort ascn alphabetical'''
# lst = ['python','java','abc','dhiraj']
# print(lst)
# lst.sort()
# print(lst)

'''sort ascn for heterogenous
//-->error
'''
# lst = ['python',30,40,'abc','dhiraj','java','ruby']
# print(lst)
# lst.sort()
# print(lst)

'''Selection Sort'''

lst = [10,2,30,5,1,50,22]
print(lst)

for i in range(0,len(lst)-1):
    for j in range(i+1,len(lst)):
        if(lst[j]<lst[i]):
            lst[i],lst[j]=lst[j],lst[i]

print(lst)
    