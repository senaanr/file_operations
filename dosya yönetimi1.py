# dosya içeriğini bir başka dosyaya kopyalama
"""def dosya_kopyala(dosya_ismi, yeni_dosya_ismi):
    with open(dosya_ismi) as file:
        icerik = file.read()
    with open(yeni_dosya_ismi, "w") as new_file:
        new_file.write(icerik)
        
dosya_kopyala("msg.txt", "msg_yeni.txt")"""


#eski dosyadaki içerikleri yeni dosyaya tersten yazdırma
def ters_cevir(dosya_ismi, yeni_dosya_ismi):
    with open(dosya_ismi, encoding="UTF-8") as file:
        icerik = file.read()
            
    with open(yeni_dosya_ismi, "w", encoding="UTF-8") as new_file:
        new_file.write(icerik[::-1])
        
#ters_cevir("msg.txt", "msg_ters.txt")


def bilgilendir(dosya_ismi):
    with open(dosya_ismi) as file:
        satirlar = file.readlines() #her satır dizi içinde gelsin
        
    sonuc = {
        "satir_sayisi": len(satirlar),
        "kelime_sayisi": sum(len(satir.split(' ')) for satir in satirlar),
        "karakter_sayisi":sum(len(satir) for satir in satirlar)
    }
    
    return sonuc
print(bilgilendir("msg.txt"))