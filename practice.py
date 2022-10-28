son=list(range(200,1000,2))
print(son)
print(sum(son))
print(son[-1]-son[0])
print(len(son))

#taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
#nonushta degan yangi ro'yxatga taomlardan nusxa oling
#Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
#Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
taomlar='osh','chuchvara','lag\'mon', 'tuxum','kasha'
nonushta= taomlar[:]
nonushta=list(nonushta)
del nonushta[0]
nonushta=tuple(nonushta)
print(nonushta)


#print("Bugun necha kishi bilan suhbat qildingiz?>>>")
#odamlar=[]
#for n in range(3):
#    odamlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi:"))
#print(odamlar)

#avtolar = ['audi','bmw','volvo','kia','hyundai']
#for avto in avtolar: # avtolar ichidadi har bir avto uchun ...
#    if avto == 'bmw':  # ... agar avto bmw ga teng bo'lsa ...
#        print(avto.upper()) # avto nomini hamma harflarini katta bilan yoz.
#    else: # aks holda ... 
#       print(avto.title())
#ism = input('Ismingiz nima?\n>>>') # Foydalanuvchi ismini so'raymiz
#if ism.lower() != 'ali': # Agar ism Aliga teng bo'lmasa ...
#    print(f"Uzr, {ism.title()} biz Alini kutayapmiz.") # quyidagi xabar chiqadi
#else:
#    print("Salom, Ali")

#ism=input("Ismingiz nima?\n>>>")
#if ism.lower()!="doniyor":
#    print(f'Uzr {ism.title()} biz Doniyorni kutayapmiz')
#else: 
#  print("Salom, Doniyor!")
#javob = float(input("12x6 nechiga teng?>>>"))
#if javob!=72:
#    print("Javob xato!")
#javob=float(input("15X5 ning javobini toping\n>>>"))
#if javob!= 75:
#    print("Javob noto'g'ri")
#else: print("Siz to'g'ri topdingiz")
#yosh = int(input("Yoshingiz nechida?>>>"))
#if yosh>=18: # yosh 18 dan katta yoki teng bo'lsa
#    print('Xush kelibsiz!')
#else: # ask holda
#    print('Kirish mumkin emas!')
#yosh=int(input("Yoshingiz nechchida\n>>>"))
#if yosh>=18:
 #   print("Siz kirsangiz bo'ladi")
#else: print("Sizga ta'qiqlangan kirish")
#login = input("Yangi login tanlang:")
#if len(login)<=5: # login uzunligini tekshiramiz
#    print("Login 5 harfdan ko'proq bo'lishi shart!")
#login= input("Yangi login kiriting:")
#if len(login)<=6:
#    print("6ta harfdan iborat login tanlang")
#else: print("Tabriklaymiz, siz ro'yxatdan o'tdingiz")
#yil = int(input("Tug'ilgan yilingizni kiriting:"))
#if 202220-yil<18: # foydalanuvchining yoshini hisoblaymiz
 #   print(f"Yoshingiz {2022-yil}da ekan.")
 #   print("Kirish mumkin emas!")
#else:
 #   print("Xush kelibsiz!")

#avtolar = ['audi','bmw','volvo','kia','hyundai']
#for avto in avtolar: # avtolar ichidadi har bir avto uchun ...
  #  if avto == 'bmw':  # ... agar avto bmw ga teng bo'lsa ...
   #     print(avto.upper()) # avto nomini hamma harflarini katta bilan yoz.
    #else: # aks holda ... 
       # print(avto.title())
#4 yoshdan kichik bolalarga kirish bepul
#4 yoshdan 12 yoshgacha kirish 5000 so'm
#12 yoshdan kattalarga 10000 so'm
#Foydalanuvchidan yoshini so'rab, hayvonot bog'iga kirish chiptasi narhini chiqaruvchi dastur yozamiz.
#yosh= int(input("Yoshingizni kiriting>>>"))
#if yosh <= 4:
#    print('Sizga kirish bepul')
#elif yosh <=12:
#    print("Sizga kirish 5000 so'm")
#else:
#    print("Sizga kirish 10000 so'm")

#yosh= int(input("Yoshingizni kiriting>>>"))
#if yosh <= 4:
#    narx= 0
#elif yosh <=12:
#    narx= 5000
#else: narx= 10000
#print(f"Sizga kirish {narx} so'm")

#kun= input('bugungi kunni kiriting>>>')
#if kun.lower() == 'shanba' or kun.lower()=='yakshanba':
#    print("Bugun dam olish kuni")
#else: print('Bugun ish kuni')

#kun= input('bugungi kunni kiriting>>')
#harorat = float(input("Havo harorati qanday?"))
#if kun.lower()=='yakshanba' and harorat>=30:
#    print('qani cho\'milgani ketdik')
#else: print('Bugun uyda qolamiz')
#narh = 15000 # mijoz 15000 so'mga taom oldi.
#choy = False # mijoz choy ham oldi
#salat = True # mijoz salat olmadi

#if choy and salat: # agar mijoz choy ham salat ham olgan bo'lsa
#    narh = narh + 10000 # narhga 10000 so'm qo'shamiz
#elif choy or salat: # agar choy yoki salat olgan bo'lsa
#    narh = narh + 5000 # narhga 5000 so'm qo'shamiz

#print(f"Jami {narh} so'm") # yakuniy narhni chiqaramiz

#narh = 15000 # mijoz 15 so'mga ovqat oldi
#choy = True
#salat = False
#non = True
#kompot = True
#assorti = False
#Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
#if choy:   # agar choy olsa
 #   print("Mijoz choy oldi.")
#3    narh = narh + 3000
#if salat:  # agar salat olsa
 #   print("Mijoz salat oldi.")
#    narh = narh + 5000
#if non:    # agar non olsa
 #   print("Mijoz non oldi.")
#    narh = narh + 2000
#if kompot: # agar kompot olsa
 #   print("Mijoz kompot oldi.")
#    narh = narh + 5000
#if assorti: # agar assorti olsa
 #   print("Mijoz assorti oldi.")
#2 3   narh = narh + 15000
    
#print(f"Jami {narh} so'm")



#menyu=['shashlik','manti','osh','lag\'mon']
#taom= input('Nima ovqat yeysiz?')
#if taom.lower() in menyu:
#    print("Zakazingiz qabul qilindi")
#else: print("Bizda bu ovqat qolmadi")

#Foydalanuvchidan juft son kiritishni so'rang.
# Agar foydalanuvchi juft son kiritsa "Rahmat!",
# agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
#son = float(input("Juft son kiriting: "))
#if son%2:
#    print('Bu son juft emas.')
#else:
#    print("Rahmat!")

#Foydalanuvchi yoshini so'rang, 
#va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:

#Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
#Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
#Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm

#yosh= float(input('Yoshingizni ayting>>>'))
#if yosh<=4 or yosh >= 60:
#    print("Sizga kirish bepul")
#elif yosh<=18:
#    print("Sizga kirish 10000 ming so'm")
#elif yosh >= 18:
#    print("Sizga kirish 20ming so'm")
#Foydalanuvchidan ikita son kiritishni so'rang, 
#sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida 
#xabarni chiqaring
#son= float(input('1-sonni kiriting>>'))
#son2= float(input('2-sonni kiriting>>'))
#if son >son2:
 #   print(f"{son}>{son2} ekan")
#elif son< son2:
 #   print(f"{son}<{son2} ekan")
#else: print("Sonlar teng")

#mahsulotlar degan ro'yxat yarating va 
#kamida 10 ta turli mahsulotni kiriting. 
#Yangi, savat degan bo'sh ro'yxat yarating va 
#foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. 
#Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va 
#qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" 
# aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.

#foydalanuvchilar degan ro'yxat tuzing, 
#va kamida 5 ta login qo'shing. 
#Foydalanuvchidan yangi login tanlashni so'rang va 
#foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning 
#tarkibi bilan solishtiring. 
#Agar ro'yxatda bunday login mavjud bo'lsa, 
#"Login band, yangi login tanlang!" 
#aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.

car_0 = {'model':'ferrari','rang':'qizil'}
print(car_0['model'])
talaba={"ism":"Doniyor", "kurs":4, "yosh":23}
print(talaba["kurs"])
talaba["fakultet"]="Turizm"
print(talaba)
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }
#otam (onam, akam, ukam, va hokazo) degan lug'at yarating va 
#lug'atga shu inson haqida kamida 3 ta m'alumot kiriting 
#(ismi, tu'gilgan yili, shahri, manzili va hokazo). 
# Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring :
#Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan
otam= {"ism":"Obid","yil":1973,"shahar":"Shahrisabz"}
print(f"otam {otam['ism']},{otam['yil']}-yilda {otam['shahar']}da tug'ilgan")

python_izohli_lugati = {
    'integer':"Butun son",
    'float':"O'nlik son",
    'string':"Matn",
    'list':"Ro'yxat",
    'tuple':"O'zgarmas ro'yxat"}




#kalit = input("Kalit so'z kiriting:").lower()
#tarjima = python_izohli_lugati.get(kalit)
#if tarjima==None:
#    print("Bunday so'z mavjud emas")
#else:
#    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")

#suz=input("Biror so'z kiting>>>")
#lugat={"apple":"olma"}
#if suz == None:
#    print("Bunday so'z yo'q")
#else:
#    print(lugat["apple"])

talaba= {"ism":"Doniyor","yosh":23,"o'qish":"akademiya"}
for kalit,qiymat in talaba.items():
    print(f"kalit:{kalit}")
    print(f"qiymat:{qiymat}")
mahsulotlar = { # Do'kondagi mahsulotlar
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
    }

#print(mahsulotlar.keys())
#print('Do\'kondagi mahsulotlar:')
#for mahsulot in mahsulotlar.keys():
#    print(mahsulot.title())

bozorlik=['olma','uzum','olcha','banan']
#for mahsulot in mahsulotlar:
#    if mahsulot in bozorlik:
#        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]}")

for buyum in bozorlik:
    if buyum not in mahsulotlar:
        print(f"Sizning do'koningizda {buyum} yo'q ekan")
davlatlar = {
    "o'zbekiston":'toshkent',
    'aqsh':'washington d.c.',
    'rossiya':'moskva',
    'tojikiston':'dushanbe',
    "qirg'iziston":'bishkek',
    'qozog\'iston':'nursulton',
    'malayziya':'kuala-lumpur',
    'singapur':'sungapur',
    'italiya':'rim'}

#print('Dunyo davlatlari:')
#for davlat in sorted(davlatlar):
#    print(davlat.upper())
for poytaxt in sorted(davlatlar.values()):
    print(poytaxt)

#Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini 
#kiriting). Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. 
#Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, 
#agar taom menuda bo'lsa narhini ko'rsating, 
#aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.
#menu = {
#        'osh':20000,
#        "lag'mon":22000,
#        'non':4000,
#        'choy':5000,
#        'shashlik':12000,
#        'somsa':6000,
#        'tabaka':15000
#        }
#print('3 ta taom buyurtma bering.')
#buyurtmalar = []
#for n in range(3):
#    buyurtmalar.append(input(f"{n+1}-taom:").lower())
#for buyurtma in buyurtmalar:
#    if buyurtma in menu:
#        print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
#    else:
#        print(f"Kechirasiz, bizda {buyurtma} yo'q.")
        