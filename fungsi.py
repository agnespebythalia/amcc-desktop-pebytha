# def foo(x):
#     if len(x)<8:
#         print("password anda kurang dari 8")
#         print("jumlah karakternya",len(x))
#     else:
#         print('password anda berhasil')
#         print("jumlah karakternya",len(x))

# print(foo("agnespebythalia"))

# #membuat rumus lingkaran 
# def keliling_lingkaran(r,p=3.14 ):
#     return (2*p*r)

# ini untuk menebak angka
# angka=24
# run=True
# while run:
#     x=int(input('masukkan angka:'))  
#     if x == angka:
#         print("angka yang benar")
#         run=False
#     elif x < angka:
#         print("angka lebih besar sedikit")
#     elif x > angka :
#         print("angka lebih kecil lagi")
#     else:
#         print("angka yg anda masukkan kejauhan ")


#ini untuk memanggil tuple dan dict
# def total (*size, **nilai):
#     for i in size:
#         print('ukuran sepatunya :',i)
        
#     for key, value in nilai.items():
#         print(key.capitalize(),value)
# #     total(42, 43, 39, 36, david=70, sabil=80, yanuar=78, peby=81)

# run=True
# while run:
#         s = input('ketikkan nama :')        
#         if s.lower()=='keluar':
#             print('selesai')
#             run=False
#         else:
#             print('panjang karakter :',len(s))
        
# while True:
#         s= input('ketikkan nama :')
#         if s.lower() == 'keluar':
#             print('inputan selesai')
#             break
#         elif len(s) < 3:
#             print('panjang karakter',len(s))
#             continue
#         print('karakter sudah cukup panjang')

# my_wishlist=['baju','hape baru','ssd','sepatu','handbag','facial wash']
# print ('jumlah wishlistku :',len(my_wishlist))
# for i in my_wishlist:
#     print(i.upper(), end=',')

# # my_wishlist=['baju','hape baru','ssd','sepatu','handbag','facial wash']
# # print(my_wishlist)

my_wishlist=['baju','hape baru','ssd','sepatu','handbag','facial wash']
print ('jumlah wishlistku :',len(my_wishlist))
print('sebelum di urutkan')
for i in my_wishlist:
    print(i.upper(), end=',')
print('\n')

my_wishlist.sort()
print('setelah di urutkan A-Z')
for i in my_wishlist:
    print(i.upper(), end=',')
print('\n')
my_wishlist.append('kalung')
print('\nmenambahkan satu barang')
for i in my_wishlist:
    print(i.upper(),end=' ')
print('\n')
my_wishlist.remove('hape baru')
print('\n menghapus satu barang karna sudah terbeli')
for i in my_wishlist:
    print(i.upper(),end=' ')

