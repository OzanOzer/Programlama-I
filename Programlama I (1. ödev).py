#1.Soru
def gelirHesapla():
    x=int(input('Finasman gelirini giriniz:'))
    y=int(input('Pazar gelirini giriniz:'))
    z=int(input('Kira gelirini giriniz:'))
    gelir=x+y+z
    print('Geliriniz:',gelir)
    return gelirHesapla
def giderHesapla():
    a=int(input('Ücret miktarını giriniz:'))
    b=int(input('Finansman giderlerini giriniz:'))
    c=int(input('Pazar giderlerini giriniz:'))
    d=int(input('Kira giderlerini giriniz:'))
    e=int(input('Muhasebe giderlerini giriniz:'))
    gider=a+b+c+d+e
    print('Gideriniz:',gider)
    return giderHesapla
def karHesapla():
    gelir=int(input('Geliri giriniz:'))
    gider=int(input('Gider giriniz:'))
    kar=gelir-gider
    if kar<1000:
        print('DÜŞÜK KAR!!!')
    elif kar==1000:
        print('İDEAL KAR.')
    else:
        print('MAKSİMUM KAR.')
    return karHesapla
##2.soru
def ekipmanEtkinlikOraniHesapla():
    planlanmisÜretimSüresi=int(input('Planlanmış üretim süresini giriniz:'))
    plansizDurus=int(input('Plansız duruşu giriniz:'))
    kullanilabilirlik=(planlanmisÜretimSüresi-plansizDurus)/planlanmisÜretimSüresi
    print('Kullanılabilirlik oranız:',kullanilabilirlik)
    standartCevrimZamani=int(input('Standart çevrim zamanını giriniz:'))
    uretimMiktari=int(input('Üretim miktarını giriniz:'))
    performans=(standartCevrimZamani*uretimMiktari)/(planlanmisÜretimSüresi-plansizDurus)
    print('Performasn oranınız:',performans)
    saglamUrunMiktari=int(input('Sağlam ürün miktarını giriniz:'))
    toplamUretimMiktari=int(input('Toplam üretim miktarını giriniz:'))
    kalite=saglamUrunMiktari/toplamUretimMiktari
    print('Kalite oranınız:',kalite)
    oee=kullanilabilirlik*performans*kalite*100
    print('Ekipman etkinlik oranınız:',oee)
    return ekipmanEtkinlikOraniHesapla
###3.soru
def adamBasiCiroHesapla():
    satisMiktari=int(input('Satış miktarını giriniz:'))
    birimSatisFiyati=int(input('Birim satış fiyatını giriniz:'))
    ciro=satisMiktari*birimSatisFiyati
    print('Cironuz:',ciro)
    toplamCalisanSayısı=int(25)
    print('Toplam Çalışan Sayınız:',toplamCalisanSayısı)
    adamBasiCiro=ciro/toplamCalisanSayısı
    print('Adam başı cironuz:',adamBasiCiro)
    return adamBasiCiroHesapla


    
