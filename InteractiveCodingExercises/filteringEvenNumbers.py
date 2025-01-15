list_of_strings = ["1","1","2","3","5","8","13","21","34","55"]

# convert to integers

list_of_ints = [int(x) for x in list_of_strings]

# filter even numbers to new list

result = [x for x in list_of_ints if x%2 == 0]

print(result)
