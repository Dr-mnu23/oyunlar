ad = input("Adınız nedir?: ")
print( ad, "Maceramıza hoş geldin!")

Cevap = input(
    "Toprak bir yoldasın, yolun sonu geldi ve sağa sola gidebilirsin. Hangi yoldan gitmek istersin? ").lower()

if Cevap == "sol":
    Cevap = input(
        "Bir nehre geldiniz, etrafından dolaşabilir veya yüzerek geçebilirsiniz? Yürümek için yürü yazın ve yüzerek karşı karşıya geçmek için yüz yazın: ")

    if Cevap == "yüz":
        print("Yüzerek karşıya geçtin ve bir timsah tarafından yendin.")
    elif Cevap == "yürü":
        print("Kilometrelerce yürüdünüz, suyunuz bitti ve oyunu kaybettiniz.")
    else:
        print('Geçerli bir seçenek değil. Kaybettin.')

elif Cevap == "sağ":
    Cevap = input(
        "Bir köprüye geldiniz, sallantılı görünüyor, onu geçmek mi istiyorsunuz yoksa geri mi gitmek istiyorsunuz (geç/geri)? ")

    if Cevap == "geri":
        print("Geri döndün ve kaybettin")
    elif Cevap == "geç":
        Cevap = input(
            "Köprüyü geçiyorsun ve bir yabancıyla karşılaşıyorsun. Onunla konuşuyor musunuz (evet/hayır)?")

        if Cevap == "evet":
            print("Yabancıyla konuştun ve sana altın verdi. Sen kazandın!")
        elif Cevap == "hayır":
            print("Yabancıyı görmezden geldim ve onlar gücendi ve kaybettim.")
        else:
            print('Geçerli bir seçenek değil. Kaybettin.')
    else:
        print('Geçerli bir seçenek değil. Kaybettin.')

else:
    print('Geçerli bir seçenek değil. Kaybettin.')

print("Denediğin için teşekkürler", ad)
