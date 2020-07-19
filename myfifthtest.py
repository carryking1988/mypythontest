import random
import string

def randomcode(n):
    charlist = string.ascii_uppercase + string.digits
    return ''.join(random.choice(charlist) for i in range(n))

if __name__ == "__main__":
    print(randomcode(10))