import modulexercise

while True:
    print('1. Penjumlahan')
    print('2. Perkalian')
    print('3. Pengurangan')
    pilih = int(input('Masukkan operasi aritmatik yang ingin anda lakukan (1/2/3): '))
    a = int(input('Masukkan Nilai: '))
    b = int(input('Masukkan Nilai: '))

    if pilih == 1:
        modulexercise.penjumlahan(a,b)
    elif pilih == 2:
        modulexercise.perkalian(a,b)
    elif pilih == 3:
        modulexercise.pengurangan(a,b)
    else:
        print('Input Yang Anda Pilih Tidak Ditemukan! ')
    
    keluar = input('Apakah anda ingin keluar? ya/tidak: ')
    if keluar == 'ya':
        break

print('Terimakasih Sudah Memakai Program Mini Kalkulator!')
        
  
