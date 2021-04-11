# -*- coding: utf-8 -*-
"""Phyton-2.ipynb

Noted by Yaman35

Original file is located at
    https://colab.research.google.com/drive/1tBjRfU6L-raM8tItk-2lIbw0a_6vpOPL

# **BASIC DATA TYPES**
"""

num_1 = 3
num_2 = 4.15
store = 'Text'

text1 = "I have learned strings" # surrounded with double quotes
print(text1)

e_mail = 'joseph@clarusway.com' # surrounded with single quotes
print(e_mail)

print('632') # this is also a string type

tv_open = True  # it seems TV is on now (Boolean example)

is_rainy = False  # I love sunny weather

x, y, z = 1, 2, 3 # Bu şekilde de değişkenlere atama işlemi gerçekleştirilebilir
print(x, y, z)

"""### **Type Conversion**

Type conversion refers to the conversion of one data type into another.

int() – converts some data types into integer type.

float() – converts some data types into float type.

str() – converts any data type into string type.
"""

example1 = 'sometimes what you say is less important than how you say it'
print(type(example1))  # Burada type() fonksiyonu dataların tipini çıktı olarak almak için kullanılır

example2 = '71'
print(type(example2))

example3 = 71
print(type(example3))

example4 = 71.0
print(type(example4))

example5 = 3.14j
print(type(example5))

example6 = True
print(type(example6))

f = 3.14  # the type is float
print(type(f))

f = 3.14  # the type is float

s = str(f)  # converting float to string
print(type(s))

f = 3.14  # the type is float

i = int(f)  # while converting a float value to an integer its decimal part is disregarded
print(i, '\n') # '\n' bir alt satıra geçilmesini sağlar
print(type(i))

i = 3

f = float(i)  #Burada da float yapınca sonuna .0 ekledi
print(f, '\n')
print(type(f))

x = 39
v = "11"
y = "2.5"
z = "I am at_"

print(x-int(v))
print(x-float(y))
print(z+str(x))

a = 10
print(type(str(a)))

print(str(True))  #Interview questionlarda çıkmış, görüleceği üzere True boolean ifadesi str() fonksiyonu ile stringe çevrilmiştir.
print(type(str(True)))

a = 36.5
b = '30'
c = '3.5'
d = ' F is enough for room temperature.'

print(str(a+int(b)+float(c))+d) # float ile yapılan dört işlemler sonucunda yine float çıkar. (int ile yapılsa bile)

"""### **Variables**"""

color = 'red'  # str type variable
season = 'summer'
price = 250  # int type variable
pi = 3.14  # float type variable
color = 'blue'  # You can always assign a new value to a created variable
price = 100  # value of 'price' is changed
season = 'winter'  

print(color, price, season, sep=', ') # sep ile değerler arası gösterilmesi istenen ayraçları belirtebiliyoruz

a = 5
b = 55
c = 555
c = a  # In Python, it is possible to assign the value of one variable to another variable
b = c
a = b

print(a, b, c, sep=', ') 

# Note that, If you use undefined name of a variable in the code you write, you will get an 'NameError' message.

pi = 3.14
converted_pi = str(pi)
print(converted_pi)
print(type(converted_pi))

print(int("10"))  # String ifade içerisindeki değer bir sayı ise integer() fonksiyonu ile rahatça çevrilebilir

print(int("ten"))  #Ancak tırnak içerisinde rakam varsa çevirir...

print(int("-22")) # Görüleceği üzere string ifade negatif bir değer içerse de onu integera çevirebiliyor

print(int("10.4")) # Lakin string ifade içerisindeki ifade görüldüğü gibi bir float değerse bunu çeviremez

print(int(10.4)) # Ama bu şekilde çevirebildiğini daha önce de görmüştük

days_in_feb = 28
print(days_in_feb + 'Days in February')  #Kafası karışır çünkü sen integer ile stringi topla diyorsun (armutla elma toplanmaz hesabı)

days_in_feb = 28
print(str(days_in_feb) + ' Days in February')  #İşte bu şekilde str() fonsiyon kullanımı ile string + string olur ki çalışır

first_num = '5'
second_num = '6'
print(first_num + second_num)  # String olarak yan yana çıkarır

first_num = '5'
second_num = '6'
print(int(first_num) + int(second_num)) # int() fonksiyonu ile integera çevrildikleri için normal olarak toplar

first_num = '5'
second_num = '6'
print(float(first_num) + float(second_num)) #Burada da float() fonksiyonu ile floata çevrilmişlerdir ve sonuc yine float olur.

first_num = input('Enter the first number: ')
second_num = input('Enter the second number: ')

print(int(first_num) + int(second_num)) # input() ile kullanıcıdan alınan her değer string olarak geleceği için hesaplamalarda kullanılmadan önce mutlaka integer veya float değere çevrilmelidir
print(float(first_num) + float(second_num)) # input() function always returns a string

"""## **Basic Operations**

**İşlem Öncelik Sırası**
- Parantheses: ()
- Power: **
- Unary minus: -3 etc
- Multiplication and Division: *,/
- Addition and Substraction: +,-


"""

print((3*4) + 2 * 3**2)

print(4 + 11) # sum of integers gives integer

print(39 + 1.0) # sum of an integer and float gives float, işlemde float varsa sonuç da float olur

no1, no2 = 46, 52 # Bu şekilde bir kullanım ile aynı anda birden fazla değişkene değer atama işlemi gerçekleştirebiliyoruz
no3 = no1 - no2
print(no3)

variable1 = variable2 = 'clarusway opens your path'  # Bu şekilde birden fazla değişkene aynı değeri de atayabiliyoruz

jan = mar = nis = 30
print(jan,mar,nis)

walter = None  # Bu şekilde yazarsak kod içerisinde hata vermez, bu değişkene takiben bir değer tanabilir rezerve edişmiş olur

x = 15
y = 33
z = x
x = y
print(x,y,z)

a, b, c = 5, 3.2, 'Hello'
print(a,b,c)

new_text = 'Being a good person'
new_text  #Bu şekilde de çıktı alınabilir

i = 3
i

new_text = 'Being a good person'
i = 3
new_text 
i  # Nasıl çıktı olduğuna dikkat et yukarıdakilerden farklı, bizim new_text yalan oldu,print() siz yazınca sadece en son olanı çıkartır

f = 3.14 
i = int(f)  #Böyle tanımlarsak integer olur ve küsüratlar artık çıktı olarak alınmaz
print(i) 
print(type(i)) 

i = 3 
f = float(i)  #Böyle tanımlarsak artık float olur ve küsüratlar otomatik olarak sonuna eklenir
print(f)

no1 = 46
print(no1/23)  # division gives float (Bölme işleminin sonucu her daim float tır)

print((3 * 4)/2)  # parentheses are used as in normal mathematics operations

print(7 / 2)  
print(7 // 2)  # it gives integer part of division (Çift bölü, tek bölüdekinin aksine float değil integer olarak çıkartır sonucu ve tam kısmını yazdırır)
print()
print(10 / 5)
print(10 // 5)

print(16 % 7)  # remainder of this division is 2 (% Bölüm sonucu kalanı verir)
print(9 % 2)  # remainder of this division is 1, it means 9 is an odd number (Tek sayı)

print(3**2)  # 3 üssü 2 demektir
print(2**3)  # 2 üssü 3 demektir
print(pow(4,5)) # pow() fonksiyonu da bir sayının üssünü çıkartmak için kullanılır. İlk sayı taban ikincisi üs tür.

print(64**0.5)  # square root (Karekökünü al demek anlamına gelir). Yani aslında üs 1/2 dir yani karekök içindedir
print(64**(1/3)) # Küpkökünü al demektir. Sonuçlar her ikisi için de daima float olarak çıkar

print(sqrt(36)) # sqrt() fonksiyonu sayının karekökünü almak için kullanılan fonksiyondur ve çıktısı float olur

from math import * # BU KOD ÇOK ÖNEMLİ, PYHTON KÜTÜPHANESİNDEKİ MATEMATİK FONKSİYONLARINI ÇAĞIRABİLMEK İÇİN BU KODU EKLEMEMİZ GEREKİR

print(max(4,2,8,16,10,35,3)) # Sayı dizisi içerisindeki en büyük değeri çıktı olarak verir
print(min(4,2,8,16,10,35,3)) # Sayı dizisi içerisindeki en küçük değeri çıktı olarak verir

from math import * # BU KOD ÇOK ÖNEMLİ, PYHTON KÜTÜPHANESİNDEKİ MATEMATİK FONKSİYONLARINI ÇAĞIRABİLMEK İÇİN BU KODU EKLEMEMİZ GEREKİR

print(round(3.2)) # round() fonksiyonu .' dan sonraki değere göre bir alta veya bir üste sayıyı yuvarlar
print(round(3.5))
print(round(3.7))
print()
print(floor(3.7)) # floor() fonksiyonu sayıyı tabana doğru çeker. Aslında her ikisi de round() fonksiyonuna benzer bir iş yapar fakat bizim istediğimiz yön doğrultusunda
print(ceil(3.2))  # ceil() fonksiyonu ise sayıyı tavana doğru çeker

my_num = -5
print(abs(my_num)) # abs() fonksiyonu mutlak değeri çıkartmak için kullanılır

print('Result of this (12+7) sum :', 12 + 7)

name = input("Enter your name: ")
age = input("Enter your age: ")

print("Hello " + name.title() + "! You're " + age +" years old") # Buradaki title() fonksiyonu kullanıcı nasıl yazarsa yazsın ilk karakterini büyük yazdırmak için kullanılır, Diğer harfleride eğer büyükse küçültür dikkat et.

num_1 = input("Enter the first number: ")
num_2 = input("Enter the second number: ")
result = int(num_1) + int(num_2) # input() sonucu her daim string geldiği için onu hesaplamalarda kullanabilmek amacıyla bu şekilde integer a çevirebiliriz
print(result)

num_1 = int(input("Enter the first number: ")) # Ya da direk burada int() fonksiyonunu kullanabiliriz
num_2 = int(input("Enter the second number: "))
result = num_1 + num_2
print(result)

num_1 = input("Enter the first number: ")
num_2 = input("Enter the second number: ")
result = float(num_1) + float(num_2) # Bu şekilde float() fonksiyonu ile kullanıcı ondalıklı sayı girse bile programın hata vermemesi sağlanır
print(result)

color = input("Bir renk giriniz: ")
plural_name = input("Çoğul bir isim giriniz: ")
celebrity = input("Ünlü bir kişi giriniz: ")
print()

print("Güller " + color.lower() + "dır") # lower() fonksiyonu tüm harfleri küçültür
print(plural_name.title() + " mordur") # Yukarıda bahsetmiştik
print("I love " + celebrity.upper()) # upper() fonksiyonu tüm harfleri büyük yapar

my_name = 'yAMan'
output = f"My name is {my_name.capitalize()}" # capitalize() fonsiyonu sadece ilk harfi büyük yapar diğerlerini küçük yazar

print(output)

phrase = "Hüseyin Yaman"
print(phrase.upper())  # Değişken değerinin bütün harflerini büyük yap anlamına gelir

phrase2 = "Yavuz Ali Yaman"
print(phrase2.isupper()) # phrase2 içindekiler büyük harf mi diye sorguluyor, Boolean bir değer verir

phrase2 = "Yavuz Ali Yaman"
print(phrase2.upper().isupper()) # Önce phrase2 yi büyük harf yapıyor ondan sonra sorguluyor

print(len(phrase2)) # phrase 2 değişkeninin karakter sayısını ortaya koyar, boşluklar da sayılır

print(phrase2[0])  # phrase 2 değişkeninin 0. index karakterini verir

print(phrase2.index("a")) # index() fonksiyonu içine yazılan karakterle ilk karşılaştığı index değerini verir,yani üsttekinin tam tersi

print(phrase2.index("Ali"))  # Aynı zamanda içine yazılan değerin ilk olarak kaçıncı indexte başladığını da gösterir

print(phrase2.replace("Y", "h")) # İlk parametreyi (hepsi) ikinci parametre ile yer değiştir demektir

print(phrase2.count("a")) # count() fonksiyonu ile istenen karakter, string içerisinde kaç defa geçmektedir o bulunabilir

phrase2 = "Yavuz Ali Yaman"
print(phrase2.index("c"))  # Bu şekilde olmayan bir karakteri aratmamız durumunda hata verir (substring not found)""Y

# Daire alanı bulma olayı

r = int(input('Yarıçapı giriniz:  ')) # input çıktısı her daim string olduğu için onu hesaplamalarda kullanabilmek için bu şekilde integera çevirmek gerekir
pi = 3.14
area = pi * r**2
print("Dairemizin alanı: ", area)

# Hipotenüs bulma olayı-1

a = 3  
a **= 2
b = 4
b **=2
print('c =', (a +b)**0.5) # Karekökü alma olayı var burada

# Hipotenüs bulma olayı-2 

a = 3
b = 4
hipotenüs = ((a**2 + b**2)**0.5)
print(hipotenüs)

a = 3.12
print(type(a))
print(a)
b = int(a)
print(type(b))
print(b)

b = "😃"
print(b) #Bu şekilde emojileri de value olarak "" içerisinde bir string gibi tanımlayabilmekteyiz. (Aslında herşey)

b = "11"
type(b)

b = "11"
type(b)

c = int(b)
type(c)



3 + int("3")

str("3") + str ("3")

str(3)+"3"

print("3"+"3")

number_int = 123
number_flt = 1.23

number_new = number_int + number_flt

print("Data type of number_int:", type(number_int))
print("Data type of number_flt:", type(number_flt))

print("Value of number_new:", number_new)
print("Data type of number_new:", type(number_new))

number_int = 123
number_str = "456"

print("Data type of number_int:", type(number_int))
print("Data type of number_str:", type(number_str))

print(number_int + number_str)  # Burada string ile integer ı toplamak istenildiği için hata veriyor

number_int = 123
number_str = "456"

print("Data type of number_int:", type(number_int))
print("Data type of number_str before Type Casting:", type(number_str))

number_str = int(number_str)
print("Data type of number_str after Type Casting:", type(number_str))

number_sum = number_int + number_str
print("Sum of number_int and number_str:", number_sum)
print("Data type of number_str before Type Casting:", type(number_str))

