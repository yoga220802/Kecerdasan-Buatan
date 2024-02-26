def profit_max(barang, ketersedian):

    max_harga = 0
    data_propit = []
    
    for x in range(ketersedian // barang[0]['terigu']): # looping barang ke 1
        for y in range(ketersedian // barang[1]['terigu']): # looping batang ke 2
            
            # cek jika semua jumlah terigu yang digunakan lebih dari 10
            # maka countinue
            if ((barang[0]['terigu'] * x) + (barang[1]['terigu'] * y)) > 10: 
                continue
            
            # simpan total profit dari perulangan
            profit = (barang[0]['harga'] * x) + (barang[1]['harga'] * y)

            # cek jika profit lebih besar dari profit yang didapatkan sebelumnya
            # dan simpan data tersebut
            if profit > max_harga:
                data_propit = [x, y]
                max_harga = profit

    return data_propit, profit
    

cireng = {
    'harga': 150_000,
    'terigu': 4,
}

cimol = {
    "nama": 'cimol',
    'harga': 135_000,
    'terigu': 2,
}

barang = [cireng, cimol]
ketersedian = 10
print(profit_max(barang, ketersedian))
