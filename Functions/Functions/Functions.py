
def print_tic_tac_toe(horizontal_character, vertical_character):
   print_tic_tac_toe_row_with_vertical_character(vertical_character)
   print_tic_tac_toe_horizontal_line(horizontal_character)
   print_tic_tac_toe_row_with_vertical_character(vertical_character)
   print_tic_tac_toe_horizontal_line(horizontal_character)
   print_tic_tac_toe_row_with_vertical_character(vertical_character)
   return

def print_tic_tac_toe_row_with_vertical_character(vertical_character):
    print('x',vertical_character,'x',vertical_character,'x')
    return

def print_tic_tac_toe_horizontal_line(horizontal_character):
    for space in range(5):
        print(horizontal_character, end=' ')
    print()
    return

print_tic_tac_toe("~","&")