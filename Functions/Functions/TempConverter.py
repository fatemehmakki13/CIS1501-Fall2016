def c_to_f(temp_in_c):
    return temp_in_c * 9 / 5 + 32

def f_to_c(temp_in_f):
    return (temp_in_f - 32) * 5 / 9

temp_c = float(input('Enter temperature in Celsius: '))
temp_f = None

temp_f = c_to_f(temp_c)

print('Fahrenheit:' , temp_f)
print('Celcius:', f_to_c(temp_f) )

