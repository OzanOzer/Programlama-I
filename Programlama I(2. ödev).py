#1.Soru
def katmaDegerCiroHesapla(a,b,c,d,e):
    katmaDegerCiro=a-(b+c+d+e)
    if (katmaDegerCiro>1000):
        print('Katma değer cironuz:',katmaDegerCiro,'İşletme katma değer cirosu yüksek.')
    elif (katmaDegerCiro>=500):
        print('Katma değer cironuz:',katmaDegerCiro,'İşletme katma değer cirosu normal.')
    else:
        print('Katma değer cironuz:',katmaDegerCiro,'işletme katma değer cirosu düşük.')
a=int(input('Toplam Satış Miktarını giriniz:'))
b=int(input('Hammadde Maliyetini giriniz:'))
c=int(input('Bakım Onarım Giderlerini giriniz:'))
d=int(input('Sevkiyat giderlerini giriniz:'))
e=int(input('Satın alınan hizmet gierlerini giriniz:'))
katmaDegerCiroHesapla(a,b,c,d,e)
##2.soru
#calSur:Çalışma Süresi
#topMusSa:Toplam müşteri sayısı
#musCalSur:Müşteri çalışma süresi
def musteriCalismaSuresi2016(calSur2016,topMusSa2016):
    global musCalSur2016
    musCalSur2016=calSur2016/topMusSa2016
    return musCalSur2016
def musteriCalismaSuresi2017(calSur2017,topMusSa2017):
    global musCalSur2017
    musCalSur2017=calSur2017/topMusSa2017
    return musCalSur2017
def yillarArasiFark(musCalismaSuresi2016,musCalismaSuresi2017):
    yillarArasiFark=musCalSur2017-musCalSur2016
    print('Yıllar arasındaki müşteri çalışma süresi farkı:',yillarArasiFark)
print('2016 yılı:')
calSur2016=int(170)
topMusSa2016=int(50)
print('Çalışma süresi:',calSur2016)
print('Toplam müşteri sayısı:',topMusSa2016)
musCalismaSuresi2016=musteriCalismaSuresi2016(calSur2016,topMusSa2016)
print('2016 Yılı müşteri çalışma süresi:',musCalSur2016)
print('2017 yılı:')
calSur2017=int(220)
topMusSa2017=int(70)
print('Çalışma süresi:',calSur2017)
print('Toplam müşteri sayısı:',topMusSa2017)
musCalismaSuresi2017=musteriCalismaSuresi2017(calSur2017,topMusSa2017)
print('2017 yılı müşteri çalışma süresi:',musCalSur2017)
a=musteriCalismaSuresi2016(calSur2016,topMusSa2016)
b=musteriCalismaSuresi2017(calSur2017,topMusSa2017)
yillarArasiFark(a,b)
###3.Soru
def ilk6AylikGelir(yazGel,finGel,urunSaGel):
    global ilk6AyTopGel
    ilk6AyTopGel=yazGel+finGel+urunSaGel
    print('İlk 6 aylık toplam geliriniz:',ilk6AyTopGel)
    return ilk6AyTopGel
def ilk6AylikGider(calMa,kiraGid,donMal):
    global ilk6AyTopGid
    ilk6AyTopGid=calMa+kiraGid+donMal
    print('İlk 6 aylık toplam gideriniz:',ilk6AyTopGid)
    return ilk6AyTopGid
def ilk6AyİsletmeKari(ilk6AyTopGel,ilk6AyTopGid):
    global ilk6AyİsKar
    ilk6AyİsKar=ilk6AyTopGel-ilk6AyTopGid
    return ilk6AyİsKar
def son6AylikGelir(yazGel,spoGel,eTicGel,urunSaGel):
    global son6AyTopGel
    son6AyTopGel=yazGel+spoGel+eTicGel+urunSaGel
    print('Son 6 aylık toplam geliriniz:',son6AyTopGel)
    return son6AyTopGel
def son6AylikGider(calMa,kiraGid,bakMal):
    global son6AyTopGid
    son6AyTopGid=calMa+kiraGid+bakMal
    print('Son 6 aylık toplam gideriniz:',son6AyTopGid)
    return son6AyTopGid
def son6AyİsletmeKari(son6AyTopGel,son6AyTopGid):
    global son6AyİsKar
    son6AyİsKar=son6AyTopGel-son6AyTopGid
    return son6AyİsKar
def karlarArasiFark(ilk6AyİsKar,son6AyİsKar):
    fark=ilk6AyİsKar-son6AyİsKar
    print('İşletme karları arasındaki fark:',fark)
    if (fark>5000):
        print('İşletme çok karlı.')
    elif (fark>=1000):
        print('İşletme karı normal.')
    else:
        print('İşletme yeterince karda değil.')
print('İlk 6 aylık gelirlerinizi yazınız')
yazGel=int(input('Yazılım gelirlerinizi yazınız:'))
finGel=int(input('Finansman gelirlerinizi yazınız:'))
urunSaGel=int(input('Ürün satış gelirinizi yazınız:'))
print('İlk 6 aylık giderlerinizi yazınız')
calMa=int(input('Çalışan maaşlarını giriniz:'))
kiraGid=int(input('Kira giderlerinizi giriniz:'))
donMal=int(input('Donanım maliyetinizi giriniz:'))
ilk6AyGelir=ilk6AylikGelir(yazGel,finGel,urunSaGel)
ilk6AyGider=ilk6AylikGider(calMa,kiraGid,donMal)
ilk6AyİsletmeKari(ilk6AyGelir,ilk6AyGider)
print('İlk 6 aylık İşletme karınız:',ilk6AyİsKar)
print('Son 6 aylık gelirlerinizi yazınız')
yazGel=int(input('Yazılım gelirlerinizi yazınız:'))
spoGel=int(input('Sponsorluk gelirinizi giriniz:'))
eTicGel=int(input('E ticaret gelirinizi giriniz:'))
urunSaGel=int(input('Ürün satış gelirinizi yazınız:'))
print('Son 6 aylık giderlerinizi yazınız')
calMa=int(input('Çalışan maaşlarını giriniz:'))
kiraGid=int(input('Kira giderlerinizi giriniz:'))
bakMal=int(input('Bakım maliyetinizi giriniz:'))
son6AyGelir=son6AylikGelir(yazGel,spoGel,eTicGel,urunSaGel)
son6AyGider=son6AylikGider(calMa,kiraGid,bakMal)
son6AyİsletmeKari(son6AyGelir,son6AyGider)
print('Son 6 aylık işletme karınız:',son6AyİsKar)
a=ilk6AyİsletmeKari(ilk6AyTopGel,ilk6AyTopGid)
b=son6AyİsletmeKari(son6AyTopGel,son6AyTopGid)
karlarArasiFark(a,b)
####4.soru
def donBasiStok(dolapSayisi,yatakSayisi,KoltukSayisi):
    global donemBasiStok
    donemBasiStok=koltukSayisi+yatakSayisi+dolapSayisi
    return donemBasiStok
def donSonuStok(satKoltukSayisi,satDolapSayisi,satYatakSayisi,alKoltukSayisi,alYatakSayisi,alDolapSayisi):
    global donemSonuStok
    donemSonuStok=(dolapSayisi-satDolapSayisi)+(yatakSayisi-satYatakSayisi)+(koltukSayisi-satKoltukSayisi)+alKoltukSayisi+alYatakSayisi+alDolapSayisi
    return donemSonuStok
def ortStok(donBasStok,donSonStok):
    ortalamaStok=(donemBasiStok+donemSonuStok)/2
    print('Ortalama stok:',ortalamaStok)

dolapSayisi=int(20)
yatakSayisi=int(30)
koltukSayisi=int(25)
print('Dolap sayınız:',dolapSayisi)
print('Yatak sayısı:',yatakSayisi)
print('Koltuk sayınız:',koltukSayisi)
donBasStok=donBasiStok(dolapSayisi,yatakSayisi,koltukSayisi)
print('Dönem başı stok:',donemBasiStok)
satKoltukSayisi=int(25)
satYatakSayisi=int(20)
satDolapSayisi=int(10)
print('Satılan koltuk sayısı:',satKoltukSayisi)
print('Satılan yatak sayısı:',satYatakSayisi)
print('Satılan dolap sayısı:',satDolapSayisi)
alKoltukSayisi=int(10)
alYatakSayisi=int(15)
alDolapSayisi=int(5)
print('Alınan koltuk sayısı:',alKoltukSayisi)
print('Alınan yatak sayısı:',alYatakSayisi)
print('Alınan dolap sayısı:',alDolapSayisi)
donSonStok=donSonuStok(satKoltukSayisi,satDolapSayisi,satYatakSayisi,alKoltukSayisi,alYatakSayisi,alDolapSayisi)
print('Dönem sonu stok:',donemSonuStok)
a=donBasiStok(dolapSayisi,yatakSayisi,koltukSayisi)
b=donSonuStok(satKoltukSayisi,satDolapSayisi,satYatakSayisi,alKoltukSayisi,alYatakSayisi,alDolapSayisi)
ortStok(a,b)


