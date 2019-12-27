#module

import sys 
print ('commandline arguments : ')
for i in sys.argv:
    """ kita dapat memberikan argument saat menjalankan program python"""
    print(i)

print(sys.argv)
print(sys.path)
#modules 

from math import sqrt
def nilai(x):
    return sqrt(x)

akar=float(input("masukkan nilai yang ingin dikonversikan desimal : "))
print("hasilnya akar: ",nilai(akar))

#input output
#oop
#problem solving
 



