def checkName(name):
    print('='*10)
    print(f'My name is {name}')
    print('='*10)

def checkBilangan(nilai):
    if nilai % 2 == 0:
        print(f'Genap dengan nilai {nilai}')
    else:
        print(f'Ganjil dengan nilai {nilai}')


def login(username, password):
    if username == 'wahyu' and password == 'admin1234':
        print('Berhasil Login')
    else:
        print('Salah')