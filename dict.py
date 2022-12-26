def reverse():
    print('enter key value pairs with a space between them')
    n = 1 #number of key value pairs
    d = dict(input("Enter key and value: ").split() for _ in range(n))
    print('the input dictionary is:',d)
    print()
    reversedDict = dict()
    for key in d:
        val = d[key]
        reversedDict[val] = key
    print("The reversed dictionary is:")
    print(reversedDict)

reverse()




