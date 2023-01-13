options = ['load data', 'export data', 'analyze & predict']

choice = 'x'

def DisplayOptions(options):

    print("1 - load data")
    print("2 - export data")
    print("3 - analyze & predict")
    print("Select option above or press enter to exit")
    choice = input()

    return choice

while choice:
    choice = DisplayOptions(options)

    if choice:
        try:
            choice = int(choice)
            if (choice < 4) and (choice > 0):
                print(options[choice-1])
            else:
                print("Pick number between 1 and 3")
        except:
            print("Please insert number")

    else:
        print("END")


