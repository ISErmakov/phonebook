
def read_phonebook():
    file = open('phonebook.txt', 'a+')
    lines = file.readlines()
    #print(*lines)
    #for i in lines:
    #    print(i)
    return lines