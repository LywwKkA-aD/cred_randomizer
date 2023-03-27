import os
import time
import random
from lib.random_username_generator import RandomUsernameGenerator
from lib.random_password_generator import RandomPasswordGenerator

class CredentialsGenerator:
    def __init__(self):
        self.username_generator = RandomUsernameGenerator(length=10)
        self.password_generator = RandomPasswordGenerator()

    def print_with_effect(self, text):
        for char in text:
            effect = random.choice([f"\033[1;31;40m{char}\033[0m", f"\033[1;32;40m{char}\033[0m", f"\033[1;33;40m{char}\033[0m", f"\033[1;34;40m{char}\033[0m"])
            print(effect, end='', flush=True)
            time.sleep(0.1)
        print()

    def generate_credentials(self):
        username = self.username_generator.generate_username()
        password = self.password_generator.generate_password()

        # Clear the terminal before printing
        os.system('cls' if os.name=='nt' else 'clear')

        print("""
   ____    ____    U _____ u ____          ____  U _____ u _   _     
U /"___|U |  _"\ u \| ___"|/|  _"\      U /"___|u\| ___"|/| \ |"|    
\| | u   \| |_) |/  |  _|" /| | | |     \| |  _ / |  _|" <|  \| |>   
 | |/__   |  _ <    | |___ U| |_| |\     | |_| |  | |___ U| |\  |u   
  \____|  |_| \_\   |_____| |____/ u      \____|  |_____| |_| \_|    
 _// \\   //   \\_    <<   >>  |||_         _)(|_   <<   >> ||   \\,-. 
(__)(__) (__)  (__)(__) (__)(__)_)       (__)__) (__) (__)(_")  (_/  
        """)
        print("Username: ", end='')
        self.print_with_effect(username)
        time.sleep(1)
        print("Password: ", end='')
        self.print_with_effect(password)

if __name__ == "__main__":
    generator = CredentialsGenerator()
    generator.generate_credentials()
