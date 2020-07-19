import random
import string

def randomcode(size=6,chars = string.ascii_uppercase+string.digits):
     return "".join(random.choices(chars,k=size))