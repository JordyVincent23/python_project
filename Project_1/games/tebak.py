import random

def start():
    while True:  
        jawaban = random.randint(1, 4)
        
        bentuk = '[]'
        contoh = [bentuk] * 4
        final = contoh.copy()
        final[jawaban - 1] = '$'

        tanya = input(f'PILIH SATU KOTAK {' '.join(contoh)} 1/2/3/4: ')
        while tanya not in['1', '2', '3', '4']:
            if tanya == '':
                tanya = input('INVALID, ISI LAGI: ')
            else:
                tanya = input('INVALID. ONLY 1,2,3,4: ')
        tanya = int(tanya)
                
        if tanya == jawaban:
            print(f'''SELAMAT KAMU MEMBAWA PULANG HADIAH
                    {' '.join(final)}''')
        else:
            print(f'''SAYANG SEKALI KAMU KURANG BERUNTUNG
                    {' '.join(final)}''')
            
        tanya1 = input('mau main lagi? y/n: ')
        if tanya1 == 'n':
                from main import option
                option()
        
if __name__ == '__main__':
    start()