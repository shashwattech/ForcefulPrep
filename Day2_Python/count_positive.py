count = 0
n = int(input("How many numbers you want to enter: "))

for i in range (n):

    num = int(input("Enter the number: "))

    if (num> 0):
        count = count + 1


print ("Positive integer count is", count)