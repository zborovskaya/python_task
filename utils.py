import random
import string
def generate_random_string_lowercase(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string

def generate_random_string_uppercase(length):
    rand_string = ''.join(random.choice(string.ascii_uppercase) for i in range(length))
    return rand_string
