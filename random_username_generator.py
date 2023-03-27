import random
import string

class RandomUsernameGenerator:
    def __init__(self, length):
        self.length = length

    def generate_username(self):
        characters = string.ascii_letters + string.digits + '_.-'
        username = ''.join(random.choice(characters) for i in range(self.length))
        return username
