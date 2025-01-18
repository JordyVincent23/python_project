import socket
from time import sleep

pc_user = socket.gethostname()

def welcome():
    style = '=' * (len(pc_user) + 6)
    print(style)
    print(f'== {pc_user} ==')
    print(style)
    
def exit_program():
    print('program akan berhenti dalam')
    sleep(1)
    print('3')
    sleep(1)
    print('2')
    sleep(1)
    print('1')
    print('oke program dihentikan')
    exit()
    
if __name__ == '__main__':
    print('ini kallo runing didalam')