target = int(input("Enter a number: "))

if target > 1000:
    print("Target value too large, exiting")
    exit()

sum = 0

for n in range(0,target+1):
    if n % 2 == 0:
        sum += n

# alternative
# for number in range(2, target + 1, 2):
#     sum += number

print(sum)
