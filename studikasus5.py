def hitung_biaya_parkir(jenis_kendaraan, lama_parkir) :
    if jenis_kendaraan == "mobil" :
        tarif = 5000
    elif jenis_kendaraan == "motor" :
        tarif = 3000
    

    total_biaya = tarif * lama_parkir
    return total_biaya

nama = input ("Masukkan nama anda terlebih dulu untuk memulai")
print ("======= SELAMAT DATANG" , nama , "DI TEMPAT PARKIR DIGITAL ======= ")

jenis_kendaraan = input ("Masukkan jenis kendaraan anda (mobil/motor):")
while jenis_kendaraan != "mobil" and jenis_kendaraan != "motor":
    print("Jenis kendaraan tidak tersedia! Silakan masukkan mobil atau motor.")
    jenis_kendaraan = input("Masukkan jenis kendaraan anda (mobil/motor): ")

jam_masuk = int (input ("Masukkan jam kendaraan masuk : "))
jam_keluar = int (input ("Masukkan jam kendaraan keluar dari parkir :"))

lama_parkir = jam_keluar - jam_masuk

total_biaya = hitung_biaya_parkir (jenis_kendaraan, lama_parkir)
print ("============== HASIL PERHITUNGAN PARKIR ==============")
print ("Jenis Kendaraan   : ", jenis_kendaraan )
print ("Jam masuk         : ", jam_masuk)
print ("Jam keluar        :",  jam_keluar)
print ("Lama Parkir       :", lama_parkir )
print ("Total biaya       : Rp", total_biaya)
print ("======================================================")