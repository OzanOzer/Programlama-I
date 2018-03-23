#1.soru
satisMiktari=500
print('Satış miktarınız:',satisMiktari)
birimSatisFiyati=20
print('Birim satış fiyatınız:',birimSatisFiyati)
ciro=5000
print('Cironuz:',ciro)
i=0
while(ciro<=500000):
    ciro=ciro+(satisMiktari*birimSatisFiyati)
    satisMiktari=satisMiktari+200
    birimSatisFiyati=birimSatisFiyati+10
    i=i+1
print("500.000 den fazla kar",i,"ayda tamamlanmıştır.")
#2.soru
stokMiktari=10000
print('Stok miktarınız:',stokMiktari)
i=0
alinanUrun=100
print('Alınan ürün sayısı:',alinanUrun)
satilanUrun=500
print('Satılan ürün sayısı:',satilanUrun)
fark=alinanUrun-satilanUrun
while(stokMiktari>0):
    stokMiktari=stokMiktari+fark
    i=i+1
print(i,"ayda stok sıfırlanacaktır.")
#3.soru
toplam=0
while True:
    print("Bir sayı giriniz,Çıkış için 0(sıfır)")
    girilen=int(input("sayı:"))
    if(girilen!=0):
        a=girilen%3
        toplam=toplam+a
        print("Toplam",toplam)
    else:
        print("Çıkış Yapıldı")
        break
#4.soru
calisan=50
print('Çalışan sayısı:',calisan)
yevmiye=90
print('Yevmiye:',yevmiye)
aylikMesai=0
haftalikMaas=630
print('Haftalık maaş:',haftalikMaas)
aylikMaas=0
while aylikMesai<=22:
    haftalikMesai=int(input("Haftalık Mesai:"))
    aylikMesai=haftalikMesai*4
    haftalikMaas=haftalikMaas+(haftalikMesai*yevmiye*0.10)
    aylikMaas=aylikMaas+haftalikMaas*4
    print("Aylık Maaş",aylikMaas)
else:
    print("Aylık mesai 22 saatten fazla olamaz")
#5.soru
gunlukUretilen=200
print('Günlük üretilen ürün:',gunlukUretilen)
gunlukDefoluUrun=0
toplamDefoluUrun=0
i=0
while (gunlukDefoluUrun<=gunlukUretilen*0.20):
    gunlukDefoluUrun=int(input("Günlük defolu ürün miktarı:"))
    toplamDefoluUrun=toplamDefoluUrun+gunlukDefoluUrun
    i=i+1
    if(gunlukDefoluUrun>gunlukUretilen*0.20):
        print("Defolu ürün sayısı limiti aştı")
        break
    
    print(i,"Günlük","defolu ürün sayısı:",toplamDefoluUrun) 

    

    
