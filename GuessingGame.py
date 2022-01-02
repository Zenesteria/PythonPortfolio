import random

Quit = False

while not Quit:
    print('''Welcome to [Zen's Guessing Game]. In this game you would be asked to guess a random number
over a certain range depending on the difficulty selected. Please select a difficult below''')

    print('')

    print('''[1]Easy( 1 - 10, 5 tries)
[2]Medium( 1 - 20, 3 tries)
[3]Hardcore( 1 - 50, 2 tries)
''')

    difficulty = input('')

    number_of_tries = 0


    if difficulty == '1':
        number_of_tries = 5
        randNumber = random.randint(1, 10)

        guessed = False
        
        while not guessed and number_of_tries > 0:
            User_Guess = int(input('Please guess a number between 1 and 10: '))

            if User_Guess == randNumber:
                print('''   
                                                        ,jf
   _am,    ,_am,  ,_g_oam,    _am,   _g_ag,   _am,   koewkovg   _mm_
 ,gF  @._-gF   @-"  jf   @  ,gF  @  ^ NX  #_,gF  @     jf      qK  "
 8Y      8Y    d   j#   jF .8Y  ,d   dY     8Y   d    jf       *b,
jK   ,  jK   ,N   jN   jF  :K  ,Z  ,jF     jK  ,Z"  ,jfk,       dN.
 NbpP    NbpP    dP   dFk_o8NbpP"V^dF       NbpY"V^"dF "dYo-"*h,W"
                         ,gF',@'
                        :8K  j8
                         "*w*"
                ''')
                guessed = True
                retry = input('Would you like to play again y/n? ')
                if retry.lower() == 'n':
                    Quit = True
                else:
                    number_of_tries = 5
                    randNumber = random.randint(1, 10)

                    guessed = False
                    print(' ')

            elif User_Guess > randNumber:
                number_of_tries = number_of_tries - 1
                print('Wrong, Guess a lower number')
            elif User_Guess < randNumber:
                number_of_tries = number_of_tries - 1
                print('Wrong, Guess a higher number')

        if number_of_tries == 0:
            print('''
                    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
                    ███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
                    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
                    ██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
                    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
                    ███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
                    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
                    ███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
                    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
                    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
                    ██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
                    ███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
                    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
                    ┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
                    ┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
                    ┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
                    ┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
                    ┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
                    ┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
                    ┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
                    ┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
                    ┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
                    ┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
                    ┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
                    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
            ''')
            retry = input('Would you like to play again y/n? ')
            if retry.lower() == 'n':
                Quit = True
            else:
                number_of_tries = 5
                randNumber = random.randint(1, 10)
                print(' ')

