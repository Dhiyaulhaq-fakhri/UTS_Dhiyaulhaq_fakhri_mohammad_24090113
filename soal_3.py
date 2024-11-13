jumlah_barang = str(input('masukan jumlah barang : '))
store_barang = 0

for i in range(1, jumlah_barang, + 1) :
    harga_barang = int(input('masukan harga barang :'))
    store_barang += harga_barang
   
total = store_barang + harga_barang 

print(f'total belanjaan : Rp.{total}')