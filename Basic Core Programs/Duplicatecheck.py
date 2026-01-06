lst = [1,2,3,4,5,1,2]
unique = []
duplicate = []

for elements in lst:
    if elements not in unique:
        unique.append(elements)
    elif elements not in duplicate:
        duplicate.append(elements)
        
print(f"These are duplicate values: {duplicate}")
print(f"These are Unique values: {unique}")