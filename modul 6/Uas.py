print('SELAMAT DATANG DI NIAGA')


member = input('apakah anda memiliki kartu member? ')
belanja = int(input('Masukan total belaja anda Rp.'))

if member == "ya" and belanja >= 500000:
    diskon =  belanja / 100 * 10
    total = belanja - diskon
    print('diskon anda = 10%')
    print(f'diskon yang kamu dapatkan : Rp.{diskon:.0f}')
    print (f'total belanjaan : Rp.{total:.0f}') 
elif member == "ya" and belanja >= 100000:
    diskon =  belanja / 100 * 5
    total = belanja - diskon
    print('diskon yang kamu dapatkan = 5%')
    print(f'diskon yang kamu dapatkan : Rp.{diskon:.0f}')
    print (f'total belanjaan : Rp.{total:.0f}') 
elif member == "ya" and belanja < 100000:
    diskon =  belanja / 100 * 3
    total = belanja - diskon
    print('diskon yang kamu dapetkan = 3%')
    print(f'diskon yang kamu dapatkan : Rp.{diskon:.0f}')
    print (f'total belanjaan : Rp.{total:.0f}') 
elif member == "tidak" and belanja >= 100000:
    total = belanja / 100 * 3
    print('diskon yang kamu dapetkan = 3%')
    print (f'total belanjaan : Rp.{total:.0f}') 
elif member == "tidak" and belanja < 100000:
    total = belanja
    print('kamu tidak mendapatkan diskon')
    print (f'total belanjaan : Rp.{total:.0f}') 
print ("terima kasih telah berbelanja :)")