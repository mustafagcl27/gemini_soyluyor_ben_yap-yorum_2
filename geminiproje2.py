#atm ve akıllı cüzdan smilasyonu

tl_bakiye=10000
usd_bakiye=0
usd=32
para_çekme_limiti=5000
pin=1234
pin_deneme=3
aktif_mi=True
while (pin_deneme>0):
    sifre=int(input("lütfen giriş pinininizi tuşlayiniz :"))
    if sifre==pin:
        print("*****sisteme hoşgeldiniz*****")
        aktif_mi=True
        break
    else:
        pin_deneme-=1
        aktif_mi=False
        print(f"yanliş pin... kalan hakkiniz ({pin_deneme})")
        if pin_deneme==0:
            print("kartiniz bloke olmuştur lütfen bankanizla iletişime geçiniz...")
            break
while (aktif_mi):
    print("*****MENÜ***** \n 1- Bakiye Sorgulama \n 2- Para Yatirma \n 3- Para Çekme \n 4- Döviz Alimi \n 5- Döviz Satimi \n 6- çikiş ")
    secim=int(input("lütfen bir seçim tuşlayiniz : "))
    if secim==1:
     print(f"TL Hesabiniz : {tl_bakiye}\n USD Hesabiniz : {usd_bakiye}")
    elif secim==2:
     yatir=float(input("lütfen yatirmak istediğiniz tutari giriniz : "))
     if yatir<=0:
        print("para eksi olamaz...")
        continue
     else:
        tl_bakiye+=yatir
        print(f"seçilen tutar hesaba geçmiştir güncel bakiyeniz \ntl : {tl_bakiye}\nusd : {usd_bakiye}")
    elif secim==3:
     çek=float(input("lütfen çekmek istediğiniz tutari giriniz"))
     if çek<=0:
             print("para eksi olamaz...")
             continue
     else:
        if çek>tl_bakiye:
           print(f"bakiye yetersiz güncel bakiyeniz : {tl_bakiye}")
           continue
        else:
           if para_çekme_limiti-çek<0:
              print(f"günlük çekim miktariniziz istediğiniz tutarı çekmeyi karşılamıyor \n günlük güncel kalan çekim bakiyesi : {para_çekme_limiti}")
              continue
           else:
              tl_bakiye-=çek
              para_çekme_limiti-=çek
              print(f"çekim işlemi başarili güncel bakiye : {tl_bakiye}")
    elif secim==4:
       print(f"güncel dolar {usd}")
       dolaral=float(input("kaç dolar almak istiyorsunuz : "))
       if dolaral<=0:
            print("para eksi olamaz...")
            continue
       else:
          if tl_bakiye<(dolaral*usd):
             print(f"hesabinizda yeterli para yok... \n max alabileceğiniz dolar{tl_bakiye/usd:.2f}")
             continue
          else:
             usd_bakiye+=dolaral
             tl_bakiye-=dolaral*usd
             print(f"{dolaral} dolar alinmiştir \ngüncel dolar bakiyeniz : {usd_bakiye} \n güncel tl bakiyeniz : {tl_bakiye}")
    elif secim==5:
        print(f"güncel dolar bakiyeniz : {usd_bakiye}")
        dolarsat=float(input("kaç dolar satmak istiyorsunuz : "))
        if dolarsat<=0:
            print("para eksi olamaz...")
            continue
        else:
           if dolarsat>usd_bakiye:
              print(f"{dolarsat} kadar dolariniz yoktur...")
              continue
           else:
              
              tl_bakiye+=dolarsat*usd
              usd_bakiye-=dolarsat
              print(f"satiş işleminiz başarili hesabiniza geçen tl : {dolarsat*usd}\ngüncel tl bakiyeniz : {tl_bakiye}")
    elif secim==6:
        print(f"bizi tercih ettiğiniz için teşekkürler \n çıkış yapılıyor...")
        aktif_mi=False
    else: 
        print("belirtilen seçenekleri tuşlayınız...")
