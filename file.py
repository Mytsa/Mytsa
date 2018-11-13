
f = open('hi1.txt', 'w')
f.write(input("input data: "))
f.close()
f = open('hi1.txt')
print("data in file is: ")
print(f.read())
f.close()
# for line in f:
# 	print (line)