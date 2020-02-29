n = int(input())

def sorter(string):
    odd = ""
    even = ""
    for idx, l in enumerate(list(string)) :
        if idx % 2 == 0 :
            even += l 
        else :
            odd += l 

    print (even+" "+ odd)

for x in range(0, n):
    s = input()
    sorter(s)