import random
from libs import welcome, exit_program
from games import tebak
from market import warung

def option():
    user_option = int(input('option:\n1.game tebak tebakan\n2.Warung\n3.hentikan program\nSilahkan pilh: '))
    if user_option == 1:
        tebak.start()
    elif user_option == 2:
        warung.start()
    elif user_option == 3:
        exit_program()
    else:
        print('itu doang pilihannya')
        
if __name__ == '__main__':
    welcome()
    option()
    exit_program()