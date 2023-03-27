import secrets
import string

class RandomPasswordGenerator:
    def __init__(self):
        self.alphabet = string.ascii_letters + string.digits + string.punctuation

    def generate_password(self):
        password = ''.join(secrets.choice(self.alphabet) for i in range(32))  # 32 characters for 128-bit strength
        return password