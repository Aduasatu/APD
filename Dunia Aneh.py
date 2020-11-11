import os
import time
data = []

def clear_screen():
    os.system('cls')

def login ():
    clear_screen()
    print ("="*55)
    print ("------------ SELAMAT DATANG DI DUNIA ANEH -------------")
    print ("="*55)
    print (" Silahkan masukkan Biodata Anda serta buatlah Sandi !! ")
    print ("="*55)
    nama = str(input("NAMA              : "))
    nick = str(input("NAMA PANGGILAN    : "))
    umur = int(input("UMUR (*angka saja): "))
    sandi= (input("SANDI             : "))
    data.append(sandi)
    data.append(nama)
    data.append(nick)
    if (umur > 17):
        ruang_atas()
    elif (umur <= 17):
        ruang_bawah()


def ruang_bawah():
    clear_screen()
    print ("="*45)
    print (" Hai", data [2])
    print (" Sebelum Lanjut Harap Masukkan Sandi Anda !! ")
    print ("="*45)
    for i in range (3):
        sandi = input("SANDI : ")
        if sandi == data [0]:
            kalkulator()

        else :
            print ("Sandi Anda salah")
            if i == 3:
                print("Terlalu Banyak Mencoba")
                print("Buatlah Kembali Bio Anda")
                time.sleep(1)
                hapus()

def kalkulator():
    clear_screen()
    print ("="*44)
    print (" Silahkan pilih apa yang kamu ingin lakukan ")
    print ("------------- Pilih angka 1-4 --------------")
    print ("="*44)
    print ("1. Penjumlahan ")
    print ("2. Pengurangan ")
    print ("3. Perkalian ")
    print ("4. Pembagian ")
    print ("="*44)
    select = input("Pilihan : " )
            
    if select == "1":
        clear_screen()
        print ("="*36)
        a = float(input("Masukkan angka pertama   : "))
        b = float(input("Masukkan angka kedua     : "))
        print ("="*36)
        c = a + b
        print (">>> Hasil : ", c,"<<<")

        time.sleep (1)
        print ("\n")
        print ("="*36)
        print("Apakah anda ingin kembali berhitung?")
        print(">>> Masukkan 1 jika Ya")
        print(">>> Tekan Sembarang jika Tidak")
        print ("="*36)
        pil = input(">>> Pilihan : ")
        if pil == "1":
            kalkulator()
        else :
            exit()
            
    elif select == "2":
        clear_screen()
        print ("="*36)
        a = float(input("Masukkan angka pertama   : "))
        b = float(input("Masukkan angka kedua     : "))
        print ("="*36)
        c = a - b
        print ("Hasil :", c)

        time.sleep (1)
        print ("\n")
        print ("="*36)
        print("Apakah anda ingin kembali berhitung?")
        print(">>> Masukkan 1 jika Ya")
        print(">>> Tekan Sembarang jika Tidak")
        print ("="*36)
        pil = input(">>> Pilihan : ")
        if pil == "1":
            kalkulator()
        else :
            exit()
            
    elif select == "3":
        clear_screen()
        print ("="*36)
        a = float(input("Masukkan angka pertama   : "))
        b = float(input("Masukkan angka kedua     : "))
        print ("="*36)
        c = a * b
        print ("Hasil :", c)

        time.sleep (1)
        print ("\n")
        print ("="*36) 
        print("Apakah anda ingin kembali berhitung?")
        print(">>> Masukkan 1 jika Ya")
        print(">>> Tekan Sembarang jika Tidak")
        print ("="*36)
        pil = input(">>> Pilihan : ")
        if pil == "1":
            kalkulator()
        else :
            exit()
            
    elif select == "4":
        clear_screen()
        print ("="*36)
        a = float(input("Masukkan angka pertama   :"))
        b = float(input("Masukkan angka kedua     :"))
        print ("="*36)
        c = a / b
        print ("Hasil :", c)

        time.sleep (1)
        print ("\n")
        print ("="*36)
        print("Apakah anda ingin kembali berhitung?")
        print(">>> Masukkan 1 jika Ya")
        print(">>> Tekan Sembarang jika Tidak")
        print ("="*36)
        pil = input(">>> Pilihan : ")
        if pil == "1":
            kalkulator()
        else :
            exit()
            
    else :
        clear_screen()
        print ("="*60)
        print (" Mohon maaf angka yang anda masukkan tidak pada rentang 1-4 ")
        print ("="*60)
        time.sleep(2)
        ruang_bawah()


def ruang_atas():
    clear_screen()
    print ("="*45)
    print (" Hai", data [2])
    print (" Sebelum Lanjut Harap Masukkan Sandi Anda !! ")
    print ("="*45)
    for i in range (3):
        sandi = input("SANDI : ")
        if sandi == data [0]:
            lanjut()

        else :
            print ("Sandi Anda salah")
            if i == 3:
                print("Terlalu Banyak Mencoba")
                print("Buatlah Kembali Bio Anda")
                time.sleep(2)
                hapus()

def lanjut():
    clear_screen()
    print ("="*62)
    print ("--------- Silahkan pilih apa yang kamu ingin lakukan ---------")
    print ("---------------------- Pilih angka 1-2 -----------------------")
    print ("="*62)
    print ("1. Menghitung Nilai Tukar Rupiah dengan 10 Mata Uang Tertinggi")
    print ("2. Menentukan Jodoh ")
    print ("="*62)
    print ("\n")
    select = input("Pilihan : ")
    
    if select == "1":
        kurs()
        

    elif select == "2":
        clear_screen()
        print ("="*55)
        a = str(input("Masukkan Nama Anda                 : "))
        b = str(input("Masukkan Nama Orang yang Anda suka : "))
        print ("="*55)
        d = len (a)
        e = len (b)
        c = 100 - (d + e) * 100 / 100
        print ("\n")
        print ("Persentase Jodoh : ", c,"%")

        time.sleep (1)
        print ("\n")
        print ("="*44)
        print("--- Apakah anda ingin kembali Mencoba? ---")
        print(">>> Masukkan 1 jika Ya")
        print(">>> Tekan Sembarang jika Tidak")
        print ("="*44)
        pil = input(">>> Pilihan : ")
        if pil == "1":
            lanjut()
        else :
            exit()
            
    else :
        clear_screen()
        print ("="*60)
        print (" Mohon maaf angka yang anda masukkan tidak pada rentang 1-2 ")
        print ("="*60)
        time.sleep(2)
        ruang_atas()

def hapus():
    data [0:3] = []
    login()

def kurs():
    clear_screen()
    print ("="*45)
    print("--------- Silahkan Pilih Angka 1-20 ----------")
    print ("="*45)
    print("1. Rupiah ke Dollar")
    print("2. Dollar ke Rupiah")
    print("3. Rupiah ke Dinnar Kuwait")
    print("4. Dinnar Kuwait ke Rupiah")
    print("5. Rupiah ke Dinnar Bahrain")
    print("6. Dinnar Bahrain ke Rupiah")
    print("7. Rupiah ke Riyal Oman")
    print("8. Riyal Oman ke Rupiah")
    print("9. Rupiah ke Dinar Yordania")
    print("10. Dinar Yordania ke Rupiah")
    print("11. Rupiah ke Poundsterling")
    print("12. Poundsterling ke Rupiah")
    print("13. Rupiah ke Dollar Kepulauan Cayman")
    print("14. Dollar Kepulauan Cayman ke Rupiah")
    print("15. Rupiah ke Euro")
    print("16. Euro ke Rupiah")
    print("17. Rupiah ke Franc Swiss")
    print("18. Franc Swiss Rupiah")
    print("19. Rupiah ke Dollar Kanada")
    print("20. Dollar Kanada ke Rupiah")
    print ("="*45)
    print ("\n")
    pil = input("Pilihan: ")
    
    if pil == "1":
        clear_screen()
        print ("="*40)
        IDR = float(input("Masukkan Nilai Rupiah : Rp. "))
        ex = IDR / 14116.50
        time.sleep(1)

        print("Nilai Dollar :", ex, "USD")

        time.sleep (1)
        print ("\n")
        print ("="*36)
        print(" Apakah anda ingin kembali Mencoba? ")
        print(">>> Masukkan 1 jika Ya")
        print(">>> Tekan Sembarang jika Tidak")
        print ("="*36)
        print ("\n")
        pil = input("Pilihan : ")
        if pil == "1":
            lanjut()
        else :
            exit()
        
    elif pil == "2":
        clear_screen()
        print ("="*40)
        USD = float(input("Masukkan Nilai Dollar : "))
        ex = USD * 14116.50
        time.sleep(1)

        print("Nilai Rupiah : Rp.", ex)

        time.sleep (1)
        print ("\n")
        print ("="*36)
        print(" Apakah anda ingin kembali Mencoba? ")
        print(">>> Masukkan 1 jika Ya")
        print(">>> Tekan Sembarang jika Tidak")
        print ("="*36)
        print ("\n")
        pil = input("Pilihan : ")
        if pil == "1":
            lanjut()
        else :
            exit()

    elif pil == "3":
        clear_screen()
        print ("="*40)
        IDR = float(input("Masukkan Nilai Rupiah : Rp. "))
        ex = IDR / 46140.07
        time.sleep(1)

        print("Nilai Dinar Kuwait :", ex, "KWD")

        time.sleep (1)
        print ("\n")
        print ("="*36)
        print(" Apakah anda ingin kembali Mencoba? ")
        print(">>> Masukkan 1 jika Ya")
        print(">>> Tekan Sembarang jika Tidak")
        print ("="*36)
        print ("\n")
        pil = input("Pilihan : ")
        if pil == "1":
            lanjut()
        else :
            exit()
        
    elif pil == "4":
        clear_screen()
        print ("="*40)
        KWD = float(input("Masukkan Nilai Dinar Kuwait : "))
        ex = KWD * 46140.07
        time.sleep(1)

        print("Nilai Rupiah : Rp.", ex)

        time.sleep (1)
        print ("\n")
        print ("="*36)
        print(" Apakah anda ingin kembali Mencoba? ")
        print(">>> Masukkan 1 jika Ya")
        print(">>> Tekan Sembarang jika Tidak")
        print ("="*36)
        print ("\n")
        pil = input("Pilihan : ")
        if pil == "1":
            lanjut()
        else :
            exit()

    elif pil == "5":
        clear_screen()
        print ("="*40)
        IDR = float(input("Masukkan Nilai Rupiah : Rp. "))
        ex = IDR / 37440.62
        time.sleep(1)

        print("Nilai Dinar Bahrain :", ex, "BHD")

        time.sleep (1)
        print ("\n")
        print ("="*36)
        print(" Apakah anda ingin kembali Mencoba? ")
        print(">>> Masukkan 1 jika Ya")
        print(">>> Tekan Sembarang jika Tidak")
        print ("="*36)
        print ("\n")
        pil = input("Pilihan : ")
        if pil == "1":
            lanjut()
        else :
            exit()

    elif pil == "6":
        clear_screen()
        print ("="*40)
        BHD = float(input("Masukkan Nilai Dinar Bahrain : "))
        ex = BHD * 37440.62
        time.sleep(1)

        print("Nilai Rupiah : Rp.", ex)

        time.sleep (1)
        print ("\n")
        print ("="*36)
        print(" Apakah anda ingin kembali Mencoba? ")
        print(">>> Masukkan 1 jika Ya")
        print(">>> Tekan Sembarang jika Tidak")
        print ("="*36)
        print ("\n")
        pil = input("Pilihan : ")
        if pil == "1":
            lanjut()
        else :
            exit()
        
    elif pil == "7":
        clear_screen()
        print ("="*40)
        IDR = float(input("Masukkan Nilai Rupiah : Rp. "))
        ex = IDR / 36669.90
        time.sleep(1)

        print("Nilai Riyal Oman", ex, "OMR")

        time.sleep (1)
        print ("\n")
        print ("="*36)
        print(" Apakah anda ingin kembali Mencoba? ")
        print(">>> Masukkan 1 jika Ya")
        print(">>> Tekan Sembarang jika Tidak")
        print ("="*36)
        print ("\n")
        pil = input("Pilihan : ")
        if pil == "1":
            lanjut()
        else :
            exit()
        
    elif pil == "8":
        clear_screen()
        print ("="*40)
        OMR = float(input("Masukkan Nilai Riyal Oman : "))
        ex = OMR * 36669.90
        time.sleep(1)

        print("Nilai Rupiah : Rp.", ex)

        time.sleep (1)
        print ("\n")
        print ("="*36)
        print(" Apakah anda ingin kembali Mencoba? ")
        print(">>> Masukkan 1 jika Ya")
        print(">>> Tekan Sembarang jika Tidak")
        print ("="*36)
        print ("\n")
        pil = input("Pilihan : ")
        if pil == "1":
            lanjut()
        else :
            exit()
        
    elif pil == "9":
        clear_screen()
        print ("="*40)
        IDR = float(input("Masukkan Nilai Rupiah : Rp. "))
        ex = IDR / 19910.41
        time.sleep(1)

        print("Nilai Dinar Yordania :", ex, "JOD")

        time.sleep (1)
        print ("\n")
        print ("="*36)
        print(" Apakah anda ingin kembali Mencoba? ")
        print(">>> Masukkan 1 jika Ya")
        print(">>> Tekan Sembarang jika Tidak")
        print ("="*36)
        print ("\n")
        pil = input("Pilihan : ")
        if pil == "1":
            lanjut()
        else :
            exit()
        
    elif pil == "10":
        clear_screen()
        print ("="*40)
        JOD = float(input("Masukkan Nilai Dinar Yordania : "))
        ex = JOD * 19910.41
        time.sleep(1)

        print("Nilai Rupiah : Rp.", ex)

        time.sleep (1)
        print ("\n")
        print ("="*36)
        print(" Apakah anda ingin kembali Mencoba? ")
        print(">>> Masukkan 1 jika Ya")
        print(">>> Tekan Sembarang jika Tidak")
        print ("="*36)
        print ("\n")
        pil = input("Pilihan : ")
        if pil == "1":
            lanjut()
        else :
            exit()
        
    elif pil == "11":
        clear_screen()
        print ("="*40)
        IDR = float(input("Masukkan Nilai Rupiah : Rp. "))
        ex = IDR / 18721.61
        time.sleep(1)

        print("Nilai Pounsterling :", ex, "GBP")

        time.sleep (1)
        print ("\n")
        print ("="*36)
        print(" Apakah anda ingin kembali Mencoba? ")
        print(">>> Masukkan 1 jika Ya")
        print(">>> Tekan Sembarang jika Tidak")
        print ("="*36)
        print ("\n")
        pil = input("Pilihan : ")
        if pil == "1":
            lanjut()
        else :
            exit()
        
    elif pil == "12":
        clear_screen()
        print ("="*40)
        GBP = float(input("Masukkan Nilai Poundsterling : "))
        ex = GBP * 18721.61
        time.sleep(1)

        print("Nilai Rupiah : Rp.", ex)

        time.sleep (1)
        print ("\n")
        print ("="*36)
        print(" Apakah anda ingin kembali Mencoba? ")
        print(">>> Masukkan 1 jika Ya")
        print(">>> Tekan Sembarang jika Tidak")
        print ("="*36)
        print ("\n")
        pil = input("Pilihan : ")
        if pil == "1":
            lanjut()
        else :
            exit()

    elif pil == "13":
        clear_screen()
        print ("="*40)
        IDR = float(input("Masukkan Nilai Rupiah : Rp. "))
        ex = IDR / 16956.82
        time.sleep(1)

        print("Nilai Dollar Kepulauan Cayman :", ex, "KYD")

        time.sleep (1)
        print ("\n")
        print ("="*36)
        print(" Apakah anda ingin kembali Mencoba? ")
        print(">>> Masukkan 1 jika Ya")
        print(">>> Tekan Sembarang jika Tidak")
        print ("="*36)
        print ("\n")
        pil = input("Pilihan : ")
        if pil == "1":
            lanjut()
        else :
            exit()
        
    elif pil == "14":
        clear_screen()
        print ("="*40)
        KYD = float(input("Masukkan Nilai Dollar Kepulauan Cayman : "))
        ex = KYD * 16956.82
        time.sleep(1)

        print("Nilai Rupiah : Rp.", ex)

        time.sleep (1)
        print ("\n")
        print ("="*36)
        print(" Apakah anda ingin kembali Mencoba? ")
        print(">>> Masukkan 1 jika Ya")
        print(">>> Tekan Sembarang jika Tidak")
        print ("="*36)
        print ("\n")
        pil = input("Pilihan : ")
        if pil == "1":
            lanjut()
        else :
            exit()
        
    elif pil == "15":
        clear_screen()
        print ("="*40)
        IDR = float(input("Masukkan Nilai Rupiah : Rp. "))
        ex = IDR / 16661.47
        time.sleep(1)

        print("Nilai Euro :", ex, "EUR")

        time.sleep (1)
        print ("\n")
        print ("="*36)
        print(" Apakah anda ingin kembali Mencoba? ")
        print(">>> Masukkan 1 jika Ya")
        print(">>> Tekan Sembarang jika Tidak")
        print ("="*36)
        print ("\n")
        pil = input("Pilihan : ")
        if pil == "1":
            lanjut()
        else :
            exit()
        
    elif pil == "16":
        clear_screen()
        print ("="*40)
        EUR = float(input("Masukkan Nilai Euro : "))
        ex = EUR * 16661.47
        time.sleep(1)

        print("Nilai Rupiah : Rp.", ex)

        time.sleep (1)
        print ("\n")
        print ("="*36)
        print(" Apakah anda ingin kembali Mencoba? ")
        print(">>> Masukkan 1 jika Ya")
        print(">>> Tekan Sembarang jika Tidak")
        print ("="*36)
        print ("\n")
        pil = input("Pilihan : ")
        if pil == "1":
            lanjut()
        else :
            exit()
        
    elif pil == "17":
        clear_screen()
        print ("="*40)
        IDR = float(input("Masukkan Nilai Rupiah : Rp. "))
        ex = IDR / 15415.26
        time.sleep(1)

        print("Nilai Euro :", ex, "CHF")

        time.sleep (1)
        print ("\n")
        print ("="*36)
        print(" Apakah anda ingin kembali Mencoba? ")
        print(">>> Masukkan 1 jika Ya")
        print(">>> Tekan Sembarang jika Tidak")
        print ("="*36)
        print ("\n")
        pil = input("Pilihan : ")
        if pil == "1":
            lanjut()
        else :
            exit()
        
    elif pil == "18":
        clear_screen()
        print ("="*40)
        CHF = float(input("Masukkan Nilai Euro : "))
        ex = CHF * 15415.26
        time.sleep(1)

        print("Nilai Rupiah : Rp.", ex)

        time.sleep (1)
        print ("\n")
        print ("="*36)
        print(" Apakah anda ingin kembali Mencoba? ")
        print(">>> Masukkan 1 jika Ya")
        print(">>> Tekan Sembarang jika Tidak")
        print ("="*36)
        print ("\n")
        pil = input("Pilihan : ")
        if pil == "1":
            lanjut()
        else :
            exit()
        
    elif pil == "19":
        clear_screen()
        print ("="*40)
        IDR = float(input("Masukkan Nilai Rupiah : Rp. "))
        ex = IDR / 10780.29
        time.sleep(1)

        print("Nilai Dolar Kanada :", ex, "CAD")

        time.sleep (1)
        print ("\n")
        print ("="*36)
        print(" Apakah anda ingin kembali Mencoba? ")
        print(">>> Masukkan 1 jika Ya")
        print(">>> Tekan Sembarang jika Tidak")
        print ("="*36)
        print ("\n")
        pil = input("Pilihan : ")
        if pil == "1":
            lanjut()
        else :
            exit()
        
    elif pil == "20":
        clear_screen()
        print ("="*40)
        CAD = float(input("Masukkan Nilai Dolar Kanada : "))
        ex = CAD * 10780.29
        time.sleep(1)

        print("Nilai Rupiah : Rp.", ex)

        time.sleep (1)
        print ("\n")
        print ("="*36)
        print(" Apakah anda ingin kembali Mencoba? ")
        print(">>> Masukkan 1 jika Ya")
        print(">>> Tekan Sembarang jika Tidak")
        print ("="*36)
        print ("\n")
        pil = input("Pilihan : ")
        if pil == "1":
            lanjut()
        else :
            exit()
        
    else :
        clear_screen()
        print ("="*61)
        print (" Mohon maaf angka yang anda masukkan tidak pada rentang 1-20 ")
        print ("="*61)
        print ("Mohon Tunggu Sesaat")
        time.sleep(3)
        kurs()


login ()  