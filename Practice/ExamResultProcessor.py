s1 = int(input("sub 1: "))
s2 = int(input("sub 2: "))
s3 = int(input("sub 3: "))
s4 = int(input("sub 4: "))
s5 = int(input("sub 5: "))

failmark = 35
if s1 < failmark or s2 < failmark or s3 < failmark or s4 < failmark or s5 < failmark:
    print("FAIL")
else:
    average = (s1 + s2 + s3 + s4 + s5) / 5
    if average >= 75:
        print("DISTINCTION")
    else:
        print("PASS")