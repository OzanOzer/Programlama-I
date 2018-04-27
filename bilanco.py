def aktifHesapla(x,y,z,c,k,a,b,d):
    kasaHesabi=int(x)
    alinanCekHesabi=int(y)
    bankalarHesabi=int(z)
    alicakSenetHesabi=int(c)
    ticMallarHesabi=int(k)
    global dönenVarlik
    dönenVarlik=kasaHesabi+alinanCekHesabi+bankalarHesabi+alicakSenetHesabi+ticMallarHesabi
    print('Dönen varlıklar değeriniz:',dönenVarlik)
    binalarHesabi=int(a)
    tasitlarHesabi=int(b)
    demirbasHesabi=int(d)
    global duranVarlik
    duranVarlik=binalarHesabi+tasitlarHesabi+demirbasHesabi
    print('Duran varlık değeriniz:',duranVarlik)
    global topAktif
    topAktif=dönenVarlik+duranVarlik
    print('Toplam aktifiniz:',topAktif)
def pasifHesapla(q,w,e,r,t):
    bankaKrediHesabi=int(q)
    saticilarHesabi=int(w)
    global kisaVadeliYaKa
    kisaVadeliYaKa=bankaKrediHesabi+saticilarHesabi
    print('Kısa vadeli yabancı kaynak Değeriniz:',kisaVadeliYaKa)
    bankaKredilerHesabi=int(e)
    borcSenHesabi=int(r)
    global uzunVadeliYaKa
    uzunVadeliYaKa=bankaKredilerHesabi+borcSenHesabi
    print('Uzun vadeli yabancı kaynak değeriniz:',uzunVadeliYaKa)
    sermayeHesabi=int(t)
    global ozKaynak
    ozKaynak=sermayeHesabi
    print('Öz kaynaklar değeriniz:',ozKaynak)
    global topPasif
    topPasif=kisaVadeliYaKa+uzunVadeliYaKa+ozKaynak
    print('Toplam pasifiniz:',topPasif)
def bilancoHesapla():
    print('Toplam aktifiniz:',topAktif)
    if topAktif==topPasif:
        print('Kapanış bilançosu doğru hesaplanmıştır.')
    else:
        print('Bilanço yanlış hesaplanmıştır.')
    
    
