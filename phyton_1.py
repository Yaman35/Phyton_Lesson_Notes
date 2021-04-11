# -*- coding: utf-8 -*-
"""Phyton-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PstMFfdO0B4n5j3mMW2HhunAam0KhNFs

# **QUOTES AND COMMENTS**
"""

print('Hello World!')  # This is a inline comment with two spaces after code, Bu şekilde tek tırnak da kullanılabilir.
# Single line comment with one space after (#)
# Satırları seçip Ctrl + K + Z yaparsan da seçilen satırların hepsini birden comment satırına dönüştürebilirsin

print("HÜSEYİN YAMAN")  # Bu şekilde çift tırnak da kullanılabilir

print(" . ")  # Boşluklu kullanım

print("""you can write your code using the editor below.
Once you write the code, click the run button to see the result.""")  # Uzun  cümlelerde bu şekilde 3 tırnak işareti kullanılabilir hata vermemesi için
                                                                      # Birden fazla satır yazılacaksa da bu şekilde kullanmak uygun olacaktır.

print('He said that "I am ill" and felt down')  # Bu şekilde tek tırnaklar içerisinde cümlede çift tırnaklar kullanılabilir veya tam tersi
print("It's not a problem")

print('Hello', "World", '''Test''')  # Bu şekilde de bir kullanım yapılabilir

print('''it's not a problem using "triple" quotes''')

print('We should have enough time for our family") # Bu şekildeki başlarken ve bitirirken farklı tırnak kullanımları hata verir
print('I'm happy to learn')  # Bu da yanlış bir kullanımdır, tek tırnaklardan ötürü hata verir (syntax error)

print(572)  # Bu integer olarak kabul edilir
print(3.14)  # Bu float olarak kabul edilir
print('3.14')  # Bunun da çıktısı üstteki gibidir lakin tırnak içerisinde olduğu için string olarak kabul edilir ve hesaplamalarda bu şekilde kullanılamaz
               # Dolayısıyla tırnak içerisindeki herşey string tir

print("print('3.14')")

print('first line')
print()  # second line is empty, Boşluk bırakmak istersek sadece bu şekilde yazmak yeterli olacaktır
print('third line')

print("-*76ahmet ..üç")  # Tırnak içerisine yazılan herşet string tir

print('''Birden fazla satır  
var diyelim
o zaman ne olacak''')  # Üçlü tırnaklar birden fazla satırı bu şekilde alt alta yazılması durumunda hata vermez fakat diğerleriyle veriyor
print()
print("""Birden fazla satır  
var diyelim
o zaman ne olacak""")  # Bu şekilde de kullanılabilir üçlü turnak

print(''''We should have enough time for our family"''')

print(''''''''''')  #Burada ilk 3 tırnakta sonra 3 tırnak daha var ama sonraki 3 tırnaktan sonra sadece 2 tırnak var oyüzden hata verir

print('''''''''''')  # Ama burada bütün 3 tırnaklar birbirini karşılıyor dolayısıyla sıkıntı yok

print('''1''''''1''')

print()  # Boş satır örnekleri
print("")
print('')

print('''')  #Bi tekli tırnaktan sonra bi tekli tırnak geliyor tamam ama sonra bidaha ve bi daha geliyor o yüzden kafası karışır ve hata verir

print(''' '''' ''')  # Bu şekilde hata vermiyor,boş çıktı veriyor

print('''''''''')  # Ama bu şekilde hata veriyor

print(" '''' ")  # Bu şekilde de ortadaki tek tırnakların çıktısını alabiliyoruz

print(''''''k'''''')

print('''1'''')  # Bu kullanım da hata verir çünkü ilk üçlüden sonra ikinci üçlü var artı bi tane daha tekli var

print(''''1''')  # Bu kullanım hata vermez çünkü ilk üçlü var sonra da ikinci üçlü var aradaki tekli ve 1 i string olarak alır ve çıkartır

print(3.14*2)  # Buradaki float ı 2 ile çarparak sonucu çıktı olarak gösterir
print('3.24'*2)  # Buradaki stringi yan yana iki kez yazar

print('''1'''"""2""")

print('''1'''1'''1''')  # Aradaki 1 açıkta kalıyor muhtemelen o yüzden hata veriyor

print('''1''''''1''')  # Bak bu çalıştı

print("I"'T')

print("print("3.14")")  # Buradaki ilk çift tırnaktan sonra hemen içteki çift tırnak çıktı diye karşısına kafası karıştı

print("print('3.14')") # Ama bak bu şekilde yazılırsa sıkıntı yok

print("'''sds'")

print('''''k''''')  # İlk 3 tekli tırnaktan sonra ''k stringi var ve de sonra 3 lü tek tırnak geliyor,en sondaki '' ise boş veriyor sanırım

print("""Merhaba"""")  #Sondaki çift tırnak yalnız kaldı muhtmelen o yüzden hata veriyor

print(''.'')  # Burada tek tırnakla başlamış sora hemen tek tırnak gelmiş yani kapattı aslında sonra nokta gelmiş açıkta kalmış sonra yine birbirini kapatan iki tane tek tırnak

print('.''')

print(".") # Yukarıdaki örnek ile kıyaslandığında bak bunda sıkıntı yok

"""**DOCSTRINGS**"""

print(print.__doc__) # Bu şekildeki kullanum fonksiyonların nasıl değerler aldığını ve ne şekilde kullanıldığını gösterir
print()              # print() Fonksiyonun açıklamasını bu şekilde görebiliriz
print(abs.__doc__)
print()
print(list.__doc__)
print()
print(sum.__doc__)
print()
print(map.__doc__)
print()
print(input.__doc__)

def function(): # Don't be confused, we use 'def()' to create a function. 
                # You will see it in the next lessons.
    """
Hi, I am the docstring of this code. 
If you need any information about this function or module, read me. 
It can help you understand how the module or function works.
    """
print(function.__doc__) # Docstring runs as an explanatory text of codes and it should be written between triple quotes.

def sayhi():
  print("Hello World!")

sayhi() # Görüleceği üzere fonksiyonu tanımladıktan sonra en son çağırma işlemini yapmamız gereklidir

def toaster():  #Bu şekilde bir fonksiyonun tanımını yapar ve o fonksiyon istenildiği zaman çağırılabilir

  print("""
Hi, This toaster works with 110v electricity.
You can use it whenever you want.
Created bu Clarusway
  """)

toaster()

def sayhi(name): # Bu şekilde değişkenli bir fonksiyon da tanımlayabiliriz
  print("Hello " + name + " !")

sayhi("Hüseyin")
sayhi("Hasan")

def say_hi(name): # Bu şekilde kullanıcıdan bilgi alarak da onun girdisini kullanan bir fonksiyon tanımlayabiliriz
  print("Hello " + name.title() + " !")

name = input("Lütfen isminizi giriniz: ")
say_hi(name)

def info(name, age): 
  print("Hello " + name.title() + " !, You're " + age + " years old!")

name = input("Lütfen isminizi giriniz: ")
age = input("Lütfen yaşınızı giriniz: ") # Burada input içerisinden string geldiği için yukarıda + ile stringlerle birleştirirken sıkıntı olmuyor
info(name, age)

def info(name, age): 
  print("Hello " + name.title() + " !, You're " + str(age) + " years old!") # Bu şekilde bir kullanım da olabilirdi

name = input("Lütfen isminizi giriniz: ")
age = int(input("Lütfen yaşınızı giriniz: ")) # Bu şekilde bir kullanım da olabilirdi
info(name, age)

def cube(num):
  num*num*num  # Eğer bu şekilde yazarsak işlem sonucunda herhangi birşey çıkartmıyor ve None veriyor
print(cube(3)) 

# return kullanımı

def cube(num):
  return num*num*num  # Fakat işlem başına return yazarsak doğru çıktıyı alabilliyoruz
print(cube(3))

def cube(num):
  return num*num*num  

result = cube(4) # Bu şekilde fonksiyon sonucunu bir değişkene atayarak da çıktısını alabiliriz
print(result)

def cube(num):
  return num*num*num 
  print("code") # Bu çıktı çıkmayacaktır çünkü return den sonra gelenleri phyton disregard eder ve işlemi bitirir

result = cube(4) # Bu şekilde fonksiyon sonucunu bir değişkene atayarak da çıktısını alabiliriz
print(result) # Sadece bu print() fonksiyonu bir çıktı verecektir

def cube(num):
  return num*num*num  

num = int(input("Küpü alınacak olan sayıyı giriniz: ")) # Bu şekilde kullanıcıdan bir sayı girmesini isteyip onun küp alma işlemini de yapabiliriz
print(cube(num))