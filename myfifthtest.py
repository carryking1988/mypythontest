import random
import string
def randomcode(n):
    code_list = string.ascii_uppercase + string.digits
    code = ""
    for i in range(n):
        code += random.choice(code_list)
    return code 


print(randomcode(10))