# import os #Głównie interakcja z systemem operacyjnym
# import glob #Tworzy listy plikow na podstawie wyszukiwan symboli wieloznacznych w katalogu
# import argparse #Mechanizm przetwarzania wiersza polecen
# import sys #!!!DO UZUPELNIENIA
# import re #Procesuje stringi
# import shutil #Zarzadzanie plikami i katalogami
# import math #Daje dostep do bardziej zaawansowanych dzialan matematycznych
# import random #Mozliwosc stworzenie psedolosowasci
# import statistics #Mozliwosc latwiejszej obslugi wiekszej ilosci danych w pojeciu bardziej matematcznym
# from urllib.request import urlopen #Dostep do internetu i procesowanie protokolu internetowego
# import smtplib #Daje mozliwosc wysylania maili !! Wymaga serweru mailowego odpalonego na localnym hoscie
# from datetime import date #pozwala na dostep do czasu
# import zlib #archiwizacja i kompresja danych
# from timeit import Timer # (Pomiar wydajnosci)pozwala przyspieszyc program pakujac i rozpakowujac zamiast tradycyjnej
                            # zamiany argumentow
# import doctest #Pozwala pisac kod wysokiej jakosci- sprawdza poprawnosc np. funkcji
# import unittest #Podobnie jak dosctest ale pozwala na zachowanie bardziej komplkeksowego zestawu testow w osobnym pliku
# import reprlib # udostepnia funkcje repr() dla duzych i zagniezdzonych kontenerow
# import pprint  # bardziej wyrafinowany sposob wyswietlania (gdy wynik jest dluzszy niz jedna linia to dodaje podzial
#                 # lini i wciecia by wyraznie ujawnic strukture danych
# import textwrap # zawija text do okreslonej dlugosci znakow
# import locale   # Modul ustawien regionalnych uzyskuje dostep do bazy danych formatow danych specyficznych dla kultury
                  # zapewnia bezposredni sposob formatowania liczb za pomoca separatorow grup
# from string import Template # Klasa szablonow z uproszczona skladnia odpowiednia do edycji przez uzytkownikow koncowych
#                 # dzieki temu uzytkownicy moga dostosowac swoje aplikacje bez koniecznosci modyfikowania aplikacji
# import time, os.path ### DO UZUPELNIENIA
# import struct     #udostepnia funkcje pack() oraz unpack() do pracy z binarnymi formatami rekordow o zmiennej dlugosci
# import threading, zipfile # threading to technika odsprzegania zadan ktore nie sa kolejno zalezne, mozna uzyc do poprawy
#                           # responsywnosci aplikacji ktore akceptuja dane wejsciowe uzytkownika podczas gdy inne zadania
#                           # dzialaja w tle
# import logging # proste wiadomosci logowe wysylane do pliku lub do sys.stderr
# import weakref, gc # pozawala na lepsze zarzadzanie pamiecia (korzystne w przypadku aplikacji webowych)
# from array import array # lepsze zarzadzanie listami
# from collections import deque # szybkie dodawanie i odczytywanie z lewej strony listy !!!raczej spowalnia w srodku listy
# import bisect # sortowanie listy na postawie wielkosci intigera
# from heapq import heapify, heappop, heappush # wykorzystywanie najmniejszych wartosci z listy
# from decimal import *

print(" Zaczynamy ")

""" os """
# os.getcwd() #Pokazuje aktualny folder projektu
#
# # help(os) #Opisy modułu (w tym przypadku modulu os)
# dir(os) #Pokazuje wszystkie mozliwe funkcje modulu
#
""" shutil """
# #shutil.copyfile('main.py','main_copy.py') <-- kopiuje plik z(x<do>y)
# #shutil.move('/folder1/folder2','innyfolder') <-- Prawdopodobnie przenosi folder z (x<doy) !!!!!!! Niepewne
#
""" glob """
# glob.glob('*.py') #Tworzy liste plikow z koncowka okreslona w nawiasie ktore sa w danym folderze/projekcie
#
""" sys """
# sys.stderr.write('Warning\n') # okazuje error message (W konsoli podswietlany na czerwono)
# #sys.exit() #<-- sposob na zakonczenie skryptu
#
""" re """
# re.findall(r'\b[a-z]*','which foot or hand fell fastest') #tworzy liste stringow ('zakres','string')
# re.sub(r'(\b[a-z]+) \1',r'\1','cat in the the hat hat') #Usuwa zdublowanego kolejnego stringa np. Ala ma ma kota
# 'Ala ma kota'.replace('ma','nie ma') # Polecany sposob zmieniania stringow w przypadku pojedynczych stringow - ulatwia
                                         #debugowanie
#
""" math """
# print(math.cos(math.pi/4))
# print(math.log(1024,2))

""" random """
# random.choice(['apple','pear','banana']) #Losowy wybor
# random.sample(range(100),10)   #Losowy wybor z podanego przedzialu oraz ilosc losowych liczb
# random.random() #Losowy float
# random.randrange(6) #Losowy intiger z zasiegu podanego w argumencie
#
""" statistic """
# data=[2.75,1.75,1.26,0.25,0.5,1.25,3.5]
# statistics.mean(data) #Zlicza srednia
# statistics.median(data)# Medaina z zakresu
# print(statistics.variance(data))
#
""" from urllib.request import urlopen """
# with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
#   for line in response:
#       line = line.decode('utf-8')  # Dekoduje dane binarne na text
#       if 'EST' in line or 'EDT' in line:  # Szuka czasu wschodniego
#           print(line)
#
""" smptlib """
# server = smtplib.SMTP('localhost')
# server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
# """To: jcaesar@example.org
# From: soothsayer@example.org
#
# Beware the Ides of March.
# """)
# server.quit()
#
""" from datetime import date """
# now = date.today() #Pobiera aktualna czas z systemu
# print (now)
# print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
# birthday = date(1997, 12, 17) #Data urodzin rok/miesiac/dzien
# age = now - birthday
# print(age.days)
# print()
#
""" zlib """
# s = b'witch which has which witches wrist watch'
# print(len(s))
# t = zlib.compress(s) #Kompresuje dlugosc znakow co finalnie z ilosci 41 daje 37 znakow
# print(len(t))
# print(zlib.decompress(t))
# print(zlib.crc32(s))
# print()
#
""" from timeit import Timer """
# print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
# print(Timer('a,b = b,a', 'a=1; b=2').timeit())
#
""" import doctest """
# def average(values):
#     """Computes the arithmetic mean of a list of numbers.
#     print(average([20, 30, 70]))
#     40.0
#     """
#     return sum(values) / len(values)
# print(doctest.testmod()) #automatycznie sprawdza poprawnosc osadzonych testow
#
""" import unittest """
# class TestStatisticalFunctions(unittest.TestCase):
#
#     def test_average(self):
#         self.assertEqual(average([20, 30, 70]), 40.0)
#         self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
#         with self.assertRaises(ZeroDivisionError):
#             average([])
#         with self.assertRaises(TypeError):
#             average(20, 30, 70)
#
# print(unittest.main())  #Calling from the command line invokes all tests

""" reprlib """
# print(reprlib.repr(set('supercalifragilistbicexpialidocious')))
# tworzy liste znakow wystepujacych w danym argumencie

""" pprint """
# t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
#      'yellow'], 'blue']]]
# pprint.pprint(t,width=30) # Width to szerokosc w znakach wyswietlanych

""" textwrap """
# doc = """The wrap() method is just like fill() except that it returns
#      a list of strings instead of one big string with newlines to separate
#      the wrapped lines."""
# print(textwrap.fill(doc,width=40)) # wyzej wyjasnione co robi

""" local """
# print(locale.setlocale(locale.LC_ALL,'English_United States.1252'))
# conv=locale.localeconv() # get mapping of convention
# x=1234567.8
# print(locale.format("%d",x,grouping=True))
# print(locale.format_string("%s%.*f",(conv['currency_symbol'],
#                     conv['frac_digits'],x),grouping=True))
""" from string import Template """
# t=Template('${village}folk send $$10 to $cause.')
# print(t.substitute(village='Nottingham',cause='the ditch fund'))

# T=Template('Return the $item to $owner.')
# d=dict(item='unladen swallow')
# #print(T.substitute(d)) # powoduje blad 'Key error' ,poniewaz nie ma informacji o '$owner'
# print(T.safe_substitute(d)) # zeby uniknac tego bledu mozna uzyc safe_substitute

""" time, os.path """
# photofiles=['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
# class BatchRename(Template):
#     delimiter='%'
# fmt=input('Enter rename style (%d-date %n-seqnum %f-format):')
# t=BatchRename(fmt)
# date=time.strftime('%d%b%y')
# for i,filename in enumerate(photofiles):
#     base,ext=os.path.splitext(filename)
#     newname=t.substitute(d=date,nn=i,f=ext)
#     print('{0}--> {1}'.format(filename,newname))

""" struct """
# ponizszy kod pokazuje jak przegladac informacje naglowkowe w pliku ZIP bez uzycia modulu zipfile

# with open('myfile.zip','rb') as f:
#     data=f.read()
# start=0
# for i in range(3):  #Pokaz 3 pierwsze pliki naglowka
#     start+=14
#     fields=struct.unpack('<IIIHH',data[start:start+16]) # 'H' i 'I' oznaczaja odpowiednio dwa i cztery bajty liczb bez znaku
                                                          # '<' oznacza ze maja one standardowy rozmiar i kolejnosc bajtow
                                                          # little-endian
#     crc32, comp_size, uncomp_size, filenamesize, extra_size=fields
#
#     start+=16
#     filename=data[start:start+filenamesize]
#     start+=filenamesize
#     extra=data[start:start+extra_size]
#     print(filename,hex(crc32),comp_sieze,uncomp_size)
#
#     start+=extra_size+comp_size # przejdz do nastepnego naglowka

""" threading, zipfile """
# Głównym wyzwaniem aplikacji wielowątkowych jest koordynacja wątków, które współużytkują dane lub inne zasoby.
# W tym celu moduł wątków udostępnia szereg operacji podstawowych synchronizacji, w tym blokady, zdarzenia, zmienne
# warunkowe i semafory.
#
# Chociaż narzędzia te są potężne, drobne błędy projektowe mogą powodować problemy, które są trudne do odtworzenia.
# Preferowanym podejściem do koordynacji zadań jest zatem skoncentrowanie całego dostępu do zasobu w jednym wątku, a
# następnie użycie modułu kolejki do zasilenia tego wątku żądaniami z innych wątków. Aplikacje korzystające z obiektów
# kolejki do komunikacji i koordynacji między wątkami są łatwiejsze do zaprojektowania, bardziej czytelne i bardziej niezawodne.

# class AsyncZip(threading.Thread):
#     def __init__(self,infile,outfile):
#         threading.Thread.__init__(self)
#         self.infile=infile
#         self.outfile=outfile
#
#     def run(self):
#         f=zipfile.ZipFile(self.outfile,'w',zipfile.ZIP_DEFLATED)
#         f.write(self.infile)
#         f.close()
#         print('Finished background zip of: ',self.infile)
# background=AsyncZip('mydata.txt','myarchive.zip')
# background.start()
# print('The main program continues to run in foregroud.')
#
# background.join() # Czeka na zakonczenie zadania w tle
# print('Main program waited until background was done.')

""" logging """
# logging.debug('Debugging information')
# logging.info('Information message')
# logging.warning('Warning:config file %s not found','server.conf')
# logging.error('Error Occurred')
# logging.critical('Critical error -- shuting down')

""" wekakref, gc"""
# class A:
#     def __init__(self,value):
#         self.value=value
#     def __repr__(self):
#         return str(self.value)
#
# a=A(10)         #Tworzy referencje
# d=weakref.WeakValueDictionary()
# d['primary']=a  #Nie tworzy referencji
# d['primary']    #pobiera obiekt jesli caly czas istnieje
#
# del a           #Ususwa referencje
# gc.collect()    #Urruchamia 'garbage collection'
#
# d['primary']    #

""" from array import array"""
#  udostepnia funkcje array() ktora dziala jak lista przechowuje jednorpdne dane i bardziej kompaktowo

# a=array('H',[4000,10,700,22222]) # 'H' oznacza dwubajtowe liczby binarne bez znaku zamiast standardowych 16 bajtow dla
#                                  # standardowych list obiektow pythona
# print(sum(a))
# print(a[1:3])

""" from collections import deque """
# obiekt deque jest jak lista z szybszym dopisywaniem i "wyskakiwaniem" z lewej strony ale wolniej sprawdza w srodku
# te obiekty sa dobrze dostosowane do implementacji kolejek i szerokiego wyszukiwania pierwszych drzew

# d=deque(["task1","task2","task3"])
# d.append("task4")
# print("Handling",d.popleft())
#
# unsearched=deque([starting_node])
# def breadth_first_search(unsearched):
#     node=unsearched.popleft()
#     for m in gen_moves(node):
#         if is_goal(m):
#             return m
#         unsearched.append(m)

""" bisect """
# scores=[(100,'perl'),(200,'tcl'),(400,'lua'),(500,'python')]
# bisect.insort(scores,(300,'ruby')) # za sprawa intigera dobiera pozycje na liscie i pozostawia ja posortowana
# print(scores)

""" from heapq import heapify, heappop, heappush """
# Modul heapq zapewnia funkcje do implementacji stosow na podstawie regularnych list.Wpis o najnizszej wartosci jest
# zawsze utrzymywany w pozycji zero. Ma to najlepsze zastosowanie w przypadku aplikacji ktore wielkokrotnie uzyskuja
# dostep do najmniejszego elementu ale nie chca uruchamiac pelnego sortowania listy

# data=[1,3,5,7,9,2,4,6,8,0]
# heapify(data) #zmienia kolejnosc listy (pierwsze 3 pozycje sa pokoleji)
# print(data)
# heappush(data,-5)   #dodaje nowy wpis
# print(data)
# print([heappop(data)for i in range(3)]) # pobiera 3 najmniejsze wpisy

""" from Decimal import * """
# print(Decimal('1.00'))
# print(Decimal('1.00') % Decimal('.10'))
# print(1.00%0.10)
# print(sum([Decimal('0.1')]*10)==Decimal('1.0'))
# print(sum([0.1]*10)==1.0)
#
# print(Decimal(1)/Decimal(7))



