cr = '#'

def draw_square(size):
    for h in range(size):
        for w in range(size):
            print(cr, end='')
        print() 

def draw_rect(height, width):
    for h in range(height):
        for w in range(width):
            print(cr, end='')
        print()

print(__name__)