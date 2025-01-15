with open("file1.txt") as file1:
    file1_contents = file1.readlines()
    file1_contents = [int(x.strip()) for x in file1_contents]

    
with open("file2.txt") as file2:
    file2_contents = file2.readlines()
    file2_contents = [int(x.strip()) for x in file2_contents]

result = [x for x in file1_contents if x in file2_contents]

print(result)