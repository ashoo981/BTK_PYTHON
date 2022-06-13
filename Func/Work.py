def myFunction():

    return 10



#s = myFunction()
#print(s)


def topDeger(a,b):

    return a+b


def kareAl(a,ust):

    return a**ust

class Musteri:
    def __int__(self,adi,soyadi,cinsiyet,tc,dogum_yili,adres):
        self.adi =adi
        self.soyadi=soyadi
        self.cinsiyet=cinsiyet
        self.tc=tc
        self.dogum_yili=dogum_yili
        self.adres=adres    

class SiparisHesapla:
    def __int__(self,total_value):

        self.total_value=total_value   



    def totalValue(a,b,c):

        siparisler = [a,b,c]
        
        sipHep=SiparisHesapla()
        sipHep.total_value=siparisler[0]+siparisler[1]+siparisler[2]
        return 1

def sayiToplama():

    x = int( input('1. sayıyı giriniz.'))
    y = int( input('2. sayıyı giriniz.'))
    toplam = x+y

    return toplam



