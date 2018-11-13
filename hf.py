# write history and read if you need
def wrt(res):
    k = open('history.txt', 'a')
    k.write(str(res) + '\n')  # need write new answer in new line - work -     k.write(str(res) + '\n')
    k.close()

def rd():
    hist = input("show calculation history - y or n: ")
    if hist == "y":
        k = open('history.txt')
        print("data in file is: ", k.read())
        k.close()
