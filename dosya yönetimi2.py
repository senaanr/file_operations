# kullanıcıdan aldığı ürün bilgisini urunler.txt dosyasına kaydeden fonk
def urun_ekle(ad, fiyat):
    with open("urunler.txt","a", encoding="UTF-8") as file:
        file.write(f"ad: {ad} fiyat: {fiyat}\n ")
        
#urun_ekle("samsung s10", 50)
urun_ekle("samsung s10", 6987)
urun_ekle("samsung s11", 5800)

def bul_ve_degistir(dosya_ad, eski_kelime, yeni_kelime):
    with open(dosya_ad, "r+") as file:
        text = file.read()
        yeni_text = text.replace(eski_kelime, yeni_kelime)
        file.seek(0)
        file.write(yeni_text)
        file.truncate() #imlecin olduğu yerden sona kadar bilgileri silsin
        
bul_ve_degistir("urunler.txt", "samsung s10", "samsung s9")