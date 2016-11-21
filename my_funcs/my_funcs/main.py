import my_funcs
import shapes

from hashlib import md5

original = "word"

print(original)
print(md5(original.encode('utf-8')).hexdigest())

print(__name__)
