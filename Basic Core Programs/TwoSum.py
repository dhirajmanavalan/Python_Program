inputs = [3,2,4]
target = int(input("Enter the target value:\n"))

for i in range(len(inputs)):
    for j in range((i+1), len(inputs)):
        if inputs[i] + inputs[j] == target:
            # print([i, j])
            print(f"The two index values are: {[i,j]}")