a : int(input('masukan nilai A : '))
b : int(input('masukan nilai B : '))

print('pilih antara penjumlahan pengurangan dan perkalian dengan 1/2/3')
metode = int(input('pilih antara 1/2/3 : '))

if metode == '1' :
    penjumlahan : (a + b)
    print(penjumlahan)

elif metode == '2' :
    pengurangan : (a - b)
    print(pengurangan)

elif metode == '3' :
    perkalian : (a * b)
    print(perkalian)