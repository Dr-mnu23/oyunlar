print("Bilgisayar sınavıma hoş geldiniz!")

playing = input("Oynamak ister misin? ")

if playing.lower() != "evet":
    quit()

print("Tamam! Hadi oynayalım :)")
score = 0

answer = input("CPU ne anlama geliyor? ")
if answer.lower() == "central processing unit":
    print('Doğru!')
    score += 1
else:
    print("Yanlış!")

answer = input("GPU'nun açılımı nedir? ")
if answer.lower() == "graphics processing unit":
    print('Doğru!')
    score += 1
else:
    print("Yanlış!")

answer = input("RAM'in anlamı nedir? ")
if answer.lower() == "random access memory":
    print('Doğru!')
    score += 1
else:
    print("Yanlış!")

answer = input("PSU'nun açılımı nedir? ")
if answer.lower() == "power supply unit":
    print('Doğru!')
    score += 1
else:
    print("Yanlış!")

print(str(score) + " Puan aldın!")
print("Yüzden " + str((score / 4) * 100) + "%.")
