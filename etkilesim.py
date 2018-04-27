def etkilesimOrani(x,y,z,a,b):
    begeniSayisi=int(x)
    yorumSayisi=int(y)
    paylasimSayisi=int(z)
    icerikSayisi=int(a)
    takipciSayisi=int(b)
    global engagementRate
    engagementRate=(((begeniSayisi+yorumSayisi+paylasimSayisi)/icerikSayisi)/takipciSayisi)*100
    print('Etkileşim oranınız:',engagementRate)
    if engagementRate>0.20:
        print('Başarılı')
    else:
        print('Başarısız')
    
