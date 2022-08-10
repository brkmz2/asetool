#!/usr/bin/env python
# encofing:utf-8
import os
os.system("apt-get install figlet")
os.system("clear")
os.system("python -m pip install colorama")
os.system("apt-get install cowsay")
import colorama
from colorama import Fore, Back, Style
colorama.init()
os.system("clear")
print(Fore.GREEN)
os.system("figlet Mahlukatlar")
print(Fore.RED)
os.system("cowsay HOŞGELDİNİZ MAHLUKATLAR")
print(Fore.BLUE)
print("""
1 >>> Mac Adresi Değişme
2 >>> DNS Numaralandırma
3 >>> Toplu Bilgi Toplama
4 >>> Çalışan Cihazların Görünmesi
5 >>> Portlardan Bilgi Toplama
""")

islemno = input("İşlem ID >>> ")
os.system("clear")
if(islemno=="1"):
          os.system("apt-get install macchanger")
          os.system("clear")
          os.system("figlet MAC ADRESI DEGISME")
          print(Fore.YELLOW)
          print("Eğer Ağ Kartınızı Bilmiyorsanız ifconfig komutunu çalıştırarak öğrenebilrsiniz.")
          print(Fore.BLUE)
          kart = input("Ağ Kartınız Nedir? (örğ. eth0) >>> ")
          
          os.system("macchanger -r " + kart)
          print(Fore.RED)
          geri = input("Eski Mac Adresine Dönmek İçin (G) Basınız >>> ")
          if(geri=="G"):
                   os.system("macchanger -p " + kart)
          else:
                print("Hatalı Komut Girdiniz ")
         
elif(islemno=="2"):
          os.system("figlet DNS ISLEMLERI")
          print("""
         
          a >>> dnsmap
         
          b >>> dnsenum
          """)
          dnsaraci = input("DNS Aracı Seçiniz >>> ")
          if(dnsaraci=="a"):
                os.system("clear")
                os.system("apt-get install dnsmap")
                os.system("clear")
                os.system("figlet DNSMAP")
                dnshedef = input("Hedefi Giriniz >>> ")
                os.system("clear")
                os.system("dnsmap " + dnshedef)
          elif(dnsaraci=="b"):
                os.system("clear")
                os.system("apt-get install dnsenum")
                os.system("clear")
                print(Fore.RED)
                os.system("figlet DNSENUM")
                dnshedef1 = input("Hedefi Giriniz >>> ")
                os.system("clear")
                os.system("dnsenum " + dnshedef1 )
          else:
                print("Dostum Öyle Bir Komut Yok")    
                
elif(islemno=="3"):
          os.system("apt-get install dmitry")
          os.system("clear")
          print(Fore.YELLOW)
          os.system("figlet DMİTRY")
          dhedef = input("Hedefi Giriniz >>> ")
          print(Fore.RED)
          print("""
          BEKLEYİNİZ...
          
          """)
          print(Fore.BLUE)
          os.system("dmitry " + dhedef + " -winsepfb -o /root/Desktop/sonuc")
          os.system("clear")
          print(Fore.RED)
          print("Bilgiler /root/Desktop/sonuc.txt belgesine kayıt edilmiştir :)) ")
     
elif(islemno=="4"):
             print("""
          
             1 >>> İç Ağ İçin
          
             2 >>> Dış Ağ İçin          
          
             """)
             netd = input("Ağ Seçiminiz >>> ")
             if(netd=="1"):
                    os.system("apt-get install netdiscover")
                    os.system("clear")
                    print(Fore.RED)
                    os.system("netdiscover")
                    
             elif(netd=="2"):
                        print(Fore.RED)
                        os.system("figlet NMAP") 
                        islem4 = input("Kontorol Edilecek IP veya Ip Aralığı (örğ: 123.567.78.9-125) >>> ")
                        os.system("nmap " + islem4 + " -sP")     
                        print(Fore.YELLOW)
                        print("Çalışan Cihazlar IP Adresi Gösterilen Cihazlardır")
                    
             else:
                          print("Hatalı Kod Girdiniz")
                          
elif(islemno=="5"):
            print("""
            1 >>> Porttan Bilgi Alma
            
            2 >>> İşletim Sistemi Öğrenme
            
            3 >>> Güvenlik Duvarı Kontrolü
            
            4 >>> Güvenlik Duvarı Çeşidi Öğrenme
                        
            """)
            print(Fore.GREEN)
            son = input(" Seçiminiz >>> ")
            if(son=="1"):
                    os.system("clear")
                    print(Fore.YELLOW)
                    hedef12 = input("Hedefi Giriniz >>> ")
                    os.system("figlet NMAP")
                    os.system("nmap " + hedef12 + " -sV -sV")
                    
            elif(son=="2"):
                    os.system("clear")
                    print(Fore.GREEN)
                    hedef13 = input("Hedefi Giriniz >>> ")
                    print(Fore.RED)
                    os.system("figlet NMAP")
                    os.system("nmap " + hedef13 + " -O")
                    
            elif(son=="3"):      
                    print(Fore.RED)
                    hedef14 = input("Hedefi Giriniz >>> ")
                    hedef15 = input("Hedef Portu Giriniz >>> ")
                    os.system("figlet NMAP")
                    os.system("nmap " + hedef14 + " --script http-waf-detect -p " + hedef15 )      
                    
            elif(son=="4"):      
                    print(Fore.RED)
                    hedef16 = input("Hedefi Giriniz >>> ")
                    hedef17 = input("Hedef Portu Giriniz >>> ")
                    os.system("figlet NMAP")
                    os.system("nmap " + hedef16 + " --script http-waf-fingerprint -p " + hedef17 ) 
            else:
                         print("Hatalı Kod Girdiniz")                     
