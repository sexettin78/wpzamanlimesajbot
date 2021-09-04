import pywhatkit as kit
#pip install pywhatkit
hedef = input("Hedef numara giriniz +90 şeklinde > ")
saat = int(input("Atılacak saati giriniz > "))
dakika = int(input("Atılacak dakikayı giriniz > "))
mesaj = input("Atılacak mesajı giriniz > ")
kit.sendwhatmsg(hedef,mesaj, saat, dakika)
