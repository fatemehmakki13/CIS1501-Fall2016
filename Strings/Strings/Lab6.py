# Type all other functions here



def print_menu(usrStr):
   validOptions = ( 'c', 'w', 'f', 'r', 's', 'q' )
   menuOp = ' '

   while menuOp not in validOptions:
       print('MENU')
       print('c - Number of non-whitespace characters')
       print('w - Number of words')
       print('f - Fix capitalization')
       print('r - Replace punctuation')
       print('s - Shorten spaces')
       print('q - Quit')
       print()
       print('Choose an option: ')
       menuOp = input()

       if menuOp == 'c':
           print('Number of non-whitespace characters: %d' % get_num_of_non_WS_characters(usrStr) )
       elif menuOp == 'w':
           print( 'FIX ME')
       elif menuOp == 'f':
            print( 'FIX ME')
       elif menuOp == 'r':
           print( 'FIX ME')
       elif menuOp == 's':
            print( 'FIX ME')

   return menuOp, usrStr

def get_num_of_non_WS_characters(userInput):
    numberOfNonWhiteSpaceCharacters = 0
    for character in userInput:
        if not character.isspace():
            numberOfNonWhiteSpaceCharacters += 1
    return numberOfNonWhiteSpaceCharacters

if __name__ == '__main__':
    # Complete main section of code
    menuOption = ''
    userInput = input('Enter a sample text: ')
    while ( menuOption != 'q' ):
        menuOption, userInput = print_menu(userInput)