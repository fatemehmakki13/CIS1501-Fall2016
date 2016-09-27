num_rows = int(input('What heighth triangle? '))


# Right angle triangle corner bottom left
for row in range(num_rows):
    for col in range(row):
        print('*', end=' ')
    print('')

print()

# Right angle triangle corner top left
for row in range(num_rows):
    for col in range(num_rows - row):
        print('*', end=' ')
    print('')

print()

# Right angle triangle corner top right
for row in range(num_rows):
    for col in range( row ):
        print(' ', end=' ')
    for col in range(num_rows - row):
        print('*', end=' ')
    print('')

print()

# Right angle triangle corner bottom right
for row in range(num_rows):
    for col in range( num_rows - row ):
        print(' ', end=' ')
    for col in range(row):
        print('*', end=' ')
    print('')

