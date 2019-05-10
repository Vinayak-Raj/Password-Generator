def validate(password):
    if len(password) < 8:
        return "Short Password. Must be atleast 8 letters."
    else:
        return "Decent Password but can be made more strong."
	
import random
import string
data = 10
def generate(size, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))

