num_rows = int(input('What heighth rectangle? '))
num_cols = int(input('What width rectangle? '))

for row in range(num_rows):
    for col in range(num_cols):
        print('*', end=' ')
    print('')