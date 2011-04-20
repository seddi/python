#!/usr/bin/python
#-*- coding:utf-8 -*-

#      Banka.gir adindaki dosyadan 3 satirlik veri okunur. Fakat verilerin istenilen duzende verilmis olmasi
# gerekir cunku veri kontrolu yapilmamistir. 
# Ornek: 
#      banka.gir adinda dosyamizin icerigi ;
#		5            --> okunurken asal sayi miktari olarak dusunulmustur
#		3 5 7 11 17  --> verilen asal sayilar olarak okuma yapilmistir
#		40           --> sifresi istenilen musteri numarasi olarak dusunulmustur
# 
# NOT : Bu duzende verilen bir dosyadan okuma yapilacagi dusunuldugu icin kontrol yoktur.

try:
	f_oku = open("banka.gir","r")
except IOError:
	print "-->banka.gir<-- adinda dosya bulunamadi. Bu adda bir dosya oldugundan eminmisiniz?"

try:
	a = int(f_oku.readline())          # Dosya ilk satiri asal sayilarin sayisi
except ValueError:
	print "-->banka.gir<-- dosyasinin 1. satirinda okunan deger integer olmali"
	exit(0)
	
asal_sayilar = f_oku.readline()        # Dosyanin 2. satiri asal sayilar
asal_sayilar = asal_sayilar.split(" ") # Dosyadan okunan 2. satiri bosluga gore karakter dizilerini sayir ve liste yap
asal = []
for i in range(a):       # Eger dosyada a tane asal sayi demesine ragmen a dan fazla asal sayi varsa ilk a tanesini al
	try:
		asal.append(int(asal_sayilar[i]))  # 2. satirdan okunan karakter dizilerini tamsayi tipine donustur ve asal sayi listesini olustur
	except ValueError:
		print "-->banka.gir<-- dosyasinin 2. satirinda okunan degerler integer olmali"
		exit(0)
	except IndexError:
		print "-->banka.gir<-- dosyasinin 2. satirinda eksik sayida deger girilmis."
		exit(0)

try:
	k = int(f_oku.readline())    # Dosaynin 3. satirindan musteri numarasini oku ve int olarak k degiskenine ata
except ValueError:
	print "-->banka.gir<-- dosyasinin 3. satirinda okunan deger integer olmali"
	exit(0)
	
f_oku.close()            # okumak icin acilan banka.gir dosyasini kapat
asal.sort()              # Asal sayilarin sirali olmamasi durumuna karsilik siralama yapilir
liste = asal[:]          # Asal sayilar listesine bagli olusturulacak sifre listemiz 

# sifre listemize (liste) guncel haline yineleme ile yeni bulunan sifreler eklenir.
# Bu fonsiyon cagrisi for dongusu ile musteri no kadar tekrarli olarak guncel sifre listesi uzerinde islem yapar ve
# istenilen musteri numarasindaki kisinin sifresini garanti eder 

def sifre_liste(i, j, durum):
	sifre = liste[i]*asal[j]           # Asal sayilar listesi ile sifre listemizin elemanlari carpilir
	if sifre in liste:                 # sifre, sifre listemizde (liste) yoksa ekle
		pass
	else:
		if (sifre < max(liste) and k <= len(liste)): # eger sifre max elemandan kucukse max ile degistir
			indis = liste.index(max(liste))
			liste.pop(indis)
			liste.insert(indis, sifre)
			print "----sifre--- >> %d "%sifre
		else:
			if (len(liste) < k):    	# sifre max elemandan buyuk ve listemizin boyu istenen musteri numarasindan kucukse ekle
				liste.append(sifre)
	
	if(durum == 1 and i < len(liste)-1): # sifre liste boyutu musteri no'ya ulastiginda ve indis sifre liste sonunda degilse
		sifre_liste(i+1, j, durum)
	
	elif (len(liste) < k and durum == 0):   # sifre listesinin eleman sayisi musteri no olana kadar asal sayi listesinin ilk elemani 
		sifre_liste(i+1, j, durum)        # ile sifre listemizin elemanlari isleme devam ettir ve sifreleri ekle
	
	else :
		if (j == (len(asal)-1)):          # Asal sayi listemizi dolasmissak cik
			liste.sort()				  # sifre listesini sirala
			return
		else :							  # Asal sayi listesinin bir sonraki elemani ile isleme devam et
			i = 0     # Asal sayi listesinin her elemani icin sifre listeyi bastan taramaya basla
			durum = 1 # Asal sayi listesinin ilk elemani ile sifre listenin ilk islemi bitince durum'u hep 1 olarak ayarla cunku sifre liste boyutu artik hep musteri no kadar
			sifre_liste(i, j+1, durum)

state = 0				 # Durum kontrolu yapmak icin degisken
for n in range(k):       # sifre listesinde k. elemanin k. indise denk gelen en kucuk eleman oldugunu garanti altina al
	sifre_liste(0, 0, state)
	state = 1            # ilk liste belirlendikten sonra sifre_liste fonksiyonu icinde durum kontrolu icin state'i 1 yap
	#~ print liste

f_yaz = open("banka.cik","w") 
f_yaz.write(str(liste[k-1]))  # k. musteri sifresini banka.cik dosyasina yazdir
f_yaz.close()                 # banka.cik dosyasina yazildi kapat

print liste

