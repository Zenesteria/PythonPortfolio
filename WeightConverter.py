def weightconverter():
    Quit = False
    while not Quit:
        weight = int(input("Weight: "))
        WeightType = input("(K)g or (L)bs: ").lower()
        if WeightType == 'k':
            convertedWeight = weight*2.205
            print('Your weight is %s pounds'%convertedWeight)
            userQuit = input("Do you wish to convert again? Y or N ")
            if userQuit.lower() == 'y':
                Quit = True
            elif userQuit.lower() == 'n':
                Quit = False
            else:
                print('invalid input')
                break
        elif WeightType == 'l':
            convertedWeight = weight*0.45
            print('Your weight is %s kilos'%convertedWeight)
            userQuit = input("Do you wish to convert again? Y or N ")
            if userQuit.lower() == 'y':
                Quit = True
            elif userQuit.lower() == 'n':
                Quit = False
            else:
                print('invalid input')
                break


weightconverter()
