numNumbers = int(input())
phoneBook={}

for nums in range(numNumbers):
    number = input()
    phoneBook[number.split()[0]] = number.split()[1]

while True:
    try:
        name = input()
        if name in phoneBook.keys():
            print('{}={}'.format(name,phoneBook[name]))
        else:
            print('Not found')
    except:
        break