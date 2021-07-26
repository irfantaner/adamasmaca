isim=input("İsminizi girin : ")
print("Hoşgeldin " + isim + " adam asmaca oyununa başlayabilirsin.")
gizli_kelime = "quarion"
tahmin_edin = ""
tahmin_hakkiniz = 10
while tahmin_hakkiniz>0:
    karakter_kaldi = 0
    for karakter in gizli_kelime:
        if karakter in tahmin_edin:
            print(karakter)
        else:
                print("-")
                karakter_kaldi+=1
    if karakter_kaldi ==0:
            print("TEBRİKLER !")
            break

    tahmin=input("Bir harf tahmin edin: ")
    tahmin_edin +=tahmin

    if tahmin in gizli_kelime:
        print("Tuttu :)")
    if tahmin not in gizli_kelime:
            tahmin_hakkiniz-=1
            print("Tutmadı :( ")
            print(f"{tahmin_hakkiniz} tane tahmin hakkınız kaldı.")
            if tahmin_hakkiniz ==0:
                print("Başaramadın abi :( ")
