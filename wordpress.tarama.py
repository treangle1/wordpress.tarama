#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet WORDPRESS TARAMA")

print("-"*55)
print("Bu tool Treangle tarafından yapılmıştır. instagram = zumrudu.anka.team")
print("-"*55)

print("""

Wordpress Tarama Programına Hoş Geldiniz.

1) Hızlı Tarama
2) Eklenti Tarama
3) Tema Tarama
4) Yönetici Kullanıcı Adı Tarama

""")

islemno = input("İşlem Numarası Giriniz : ")
if(islemno=="1"):
    site = input("Site Adresi Giriniz : ")
    os.system("wpscan --url " + site)
elif(islemno=="2"):
    site = input("Site Adresi Girin : ")
    os.system("wpscan --url " + site + " --enumerate p")

elif(islemno=="3"):
    site = input("Site Adresi Girin : ")
    os.system("wpscan --url " + site + " --enumerate t")

elif(islemno=="4"):
    site = input("Site Adresi Girin : ")
    os.system("wpscan --url " + site + " --enumerate u")

else:
    print("Hatalı Seçim Yaptınız. Program Kapatıldı...")




