def one():
    print 'Eivind'
    print 'Norling'


def two():
    name = raw_input("Please enter your full name here: ")
    split = str.split(name, ' ')
    print split

    for i in split:
        print i


def main():

    pro = input('Select program one or two by typing either: 1 or 2: ')

    if pro == 1:
        one()
    elif pro == 2:
        two()
    else:
        print 'Error: Type either 1 or 2 into the console to select program to run!'
        main()


if __name__ == '__main__':
    main()
