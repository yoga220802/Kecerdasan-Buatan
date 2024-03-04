def maximum_profit(barang, ketersedian):

    # penampung data sementara
    max_profit = 0
    data_profit = []

    for x in range(ketersedian // barang[0]['terigu']): # looping barang ke 1
        for y in range(ketersedian // barang[1]['terigu']): # looping barang ke 2

            # cek jika semua jumlah terigu yang digunakan lebih dari `ketersedian`
            # maka countinue
            if ((barang[0]['terigu'] * x) + (barang[1]['terigu'] * y)) > ketersedian: 
                continue

            # simpan total profit yanga di dapat pada perulangan saat ini
            profit = (barang[0]['harga'] * x) + (barang[1]['harga'] * y)

            # cek jika profit lebih besar dari max_profit yang didapatkan sebelumnya,
            # simpan profit dan data yang didatapt
            if profit > max_profit:
                data_profit = [x, y]
                max_profit = profit

    return data_profit, profit

ketersedian = 10
barang = [{'nama': 'Cireng', 'harga': 150_000, 'terigu': 4 }, 
          {'nama': 'Cimol','harga': 135_000, 'terigu': 2}]
jumlah_terigu, profit = maximum_profit(barang, ketersedian)

print(f"Profit tertinggi yang di dapat Rp.{profit}")
print("barang yang di dapat diproduksi: ")
print(f"\t{barang[0]['nama']}: {jumlah_terigu[0]}")
print(f"\t{barang[1]['nama']}: {jumlah_terigu[1]}")
