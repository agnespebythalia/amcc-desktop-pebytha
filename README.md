# Cara Instal Visual Studio Code di Windows, Linux dan MacOS

Visual Studio Code merupakan IDE Pemrograman yang bisa digunakan untuk banyak sekali bahasa pemrograman.

Visual Studio Code diluncurkan pertama kali pada tanggal 29 April 2015 oleh Microsoft dengan tujuan untuk membantu para programmer dalam mengembangkan program-program mereka.

Visual Studio Code terdapat beberapa fitur yang membantu para programmer, fitur tersebut seperti:

- Extensions yang dapat diinstal berbagai dukungan bahasa pemrograman
- Ikon & Tema
- Fitur debugger dan problems untuk mengetahui warning dan error pada source yang kita tulis
- Integrasi dengan git dan
- Terminal
- Pada Windows, terminal Visual Studio Code dapat menggunakan PowerShell maupun CMD. Sedangkan pada linux terminal yang digunakan adalah Bash.

# Install VS Code Windows
Untuk menginstall Visual Studio Code di Windows, Anda dapat mendownload master filenya melalui link di bawah.

Pertama download terlebih dahulu master instalasi Visual Studio Code pada link di atas. Apabila telah di download, buka file instalasinya dan tekan next.

Pada form persetujuan Lisensi, tekan I accept the agreement kemudian tekan next.

Selanjutnya tekan next hingga instalasi selesai.

# install VS Code Linux
Terdapat tiga versi untuk menginstal Visual Studio Code di linux. Mana yang Anda pilih?

Tergantung distro linux apa yang Anda gunakan.

## 1. Ubuntu, Debian
Untuk melakukan instalasi pada Ubuntu, langkah pertama yaitu dengan menambahkan repositori dan key.

curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg
sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
Setelah itu, Update repositori dan instal VS Code.

sudo apt-get update
sudo apt-get install code # or code-insiders

## 2. RHEL, Fedora, dan CentOS
Untuk melakukan instalasi, langkah pertama yaitu dengan menambahkan repositori dan key.

sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'
Setelah itu, Update repositori dan instal VS Code.

dnf check-update
sudo dnf install code

## 3. openSUSE dan SLE
Untuk melakukan instalasi, langkah pertama yaitu dengan menambahkan repositori dan key.

sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ntype=rpm-md\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/zypp/repos.d/vscode.repo'
Setelah itu, Update repositori dan instal VS Code.

sudo zypper refresh
sudo zypper install code
Install VS Code MacOS
Untuk menginstall Visual Studio Code di Windows, Anda dapat mendownload master filenya melalui link di bawah.

icon-software
Visual Studio Code
icon-download
Cara Instal Di Mac OS
Ini adalah cara yang paling mudah. Pertama download terlebih dahulu Visual Studio Code pada link di atas.

Setelah di download, langsung buka aplikasi tersebut. Visual Studio Code bisa langsung digunakan.

Penutup
Itulah beberapa cara instalasi visual studio code di Windows, Linux, dan Mac OS. Setelah penginstalan selesai, VS Code sudah dapat digunakan untuk menuliskan dan menjalankan kode Anda.
_______________________________________________________________________________________________________________________________

# Cara Install Python di Windows
## Python
Pemrograman Python

Instalasi python di Windows sangat gampang. Langkah-langkanya sama seperti menginstal software Windows pada umumnya, next-next-finish.

Tapi ada konfigurasi yang harus dipilih ditengah-tengah proses instalasi, agar perintah Python dapat dikenali di CMD.

Python yang akan di instal dalam panduan ini adalah python versi 3. Download di situs resmi python (python.org).

## Download Python
1. Buka File python-3.msi
Setelah download selesai, kita akan mendapatkan file python-3.4.2.msi. File python-3.4.2.msi adalah file instalator python. File ini akan melakukan instalasi ke sistem windows.

Klik ganda untuk mengeksekusinya.

2. Pilih Pengguna
Pada tahapan ini kita akan diminta untuk memilih siapa saja yang boleh memakai python.

Pilih saja ‘Install for all users’ agar bisa dipakai untuk semua user di komputernya.


3. Lokasi Instalasi
Tentukan lokasi python akan diinstal. Biarkan saja di C:\python34\, kemudian klik next.


4. Kostumisasi
Pada tahapan ini, kita akan menentukan fitur-fitur yang akan diinstal.

Jangan lupa untuk mengaktifkan ‘Add python.exe to path’ agar perintah python dikenali pada CMD (Command Prompt).

Kustomisasi Python

5. Selesai…
Klik finish untuk menyelesaikan.

Instalasi Python Selesai

Berhasil…
sumber Artikel >>https://www.petanikode.com/python-windows/
### NOTE : Bagi yang menggunakan LINUX python itu sudah Otomatis. tinggal ketikkan pada terminal
python --version.
________________________________________________________________________________________________________________________________

# 1. Cara Install Git di Linux
Instalasi Git pada Distro keluarga Debian dapat menggunakan perintah *apt*.
```sudo apt install git```
atau

```sudo apt-get install git```
Pada Fedora:

```yum install git```

Setelah itu, coba perika versi yang terinstal dengan perintah:

```$ git --version```

Pada komputer saya, versi yang terinstal adalah versi 2.7.4.

# 2. Cara Install Git di Windows

Instalasi Git di Windows memang tidak seperti di Linux yang ketik perintah langsung terinstal.

Kita harus men-download dulu, kemudian melakukan ritual next>next>finish.

Tapi dalam ritual tersebut, ada pilihan yang harus diperhatikan agar perintah git dapat dikenali di CMD.

Download Git
Silahkan buka website resminya Git  >> https://git-scm.com/downloads Kemudian unduh Git sesuai dengan arsitektur komputer kita. Kalau menggunakan 64bit, unduh yang 64bit. Begitu juga kalau menggunakan 32bit.

Langkah-langkah Install Git di Windows
Baiklah, mari kita mulai ritual instalnya. Silahkan klik 2x file instaler Git yang sudah diunduh.

1. Buka file instalator Git

2. Maka akan muncul infomasi lisensi Git, klik Next > untuk melanjutkan.

3. Informasi tentang Git

4. Selanjutnya menentukan lokasi instalasi. Biarkan saja apa adanya, kemudian klik Next >.

5. Lokasi instalasi Git

6. Selanjutnya pemilihan komoponen, biarkan saja seperti ini kemudian klik Next >.

7. Pemilihan Komponen untuk diinstal

8. Selanjutnya pemlilihan direktori start menu, klik Next >.

9. Pembuatan start menu

10. Selanjutnya pengaturan PATH Environment. Pilih yang tengah agar perintah git dapat di kenali di Command Prompt (CMD). Setelah itu klik Next >.

11. Menentukan Path Environment

12. Selanjutnya konversi line ending. Biarkan saja seperti ini, kemudian klik Next >.

13. Konversi line ending yang akan digunakan

14. Selanjutnya pemilihan emulator terminal. Pilih saja yang bawah, kemudian klik Next >.

15. Pemilihan Terminal Emulator

16. Selanjutnya pemilihan opsi ekstra. Klik saja Next >.

17. Pemilihan Opsi Ekstra

18. Selanjutnya pemilihan opsi ekspreimental, langsung saja klik Install untuk memaulai instalasi.

19. Opsi Eksperimental

20. Tunggu beberapa saat, instalasi sedang dilakukan.

Sedang Menginstall Git

Setelah selesai, kita bisa langsung klik Finish.

Instalasi Git Selesai

Selamat, Git sudah terinstal di Windows. Untuk mencobanya, silahkan buka CMD atau PowerShell, 
kemudian ketik perintah ```git --version``` lalu klik enter.


 
3. Konfigurasi Awal yang Harus Dilakukan
Ada beberapa konfigurasi yang harus dupersiapakan sebelum mulai menggunakan Git, seperti name dan email.

Silahkan lakukan konfigurasi dengan perintah berikut ini.

```git config --global user.name``` 
```git config --global user.email pebythalia@gmail.com```
Kemudian periksa konfigurasinya dengan perintah:

```git config --list```
Apabila berhasil tampil seperti gambar berikut ini, berarti konfigurasi berhasil.

konfigurasi git

Konfigurasi core.editor bersifat opsional. Sedangkan name dan email wajib.

Jika kamu memiliki akun Github, Gitlab, Bitbucket atau yang lainnya…
maka username dan email harus mengikuti akun tersebut agar mudah diintegrasikan.# amcc-desktop-pebytha
projek pelatihan member amcc 2019/2020
________________________________________________________________________________________________________________________________
* Let's TRY !! *

# amcc-desktop-apthalie
projek pelatihan phyton dan github amcc desktop

# 1. Pelatihan desktop amcc menggunakan tools git 
- pertama pastikan sudah mendaftar github
- pastikan telah menginstall git bash

# bagaimana clone repository ini ? 
1. pastikan anda membuat repository yang baru dengan mengeklik profil anda
   dibagian github.com 
2. lalu klik your repositories
3. lalu klik tombol new
4. lalu masukkan nama repositori yang baru 
5. setelah itu klik initialize 
6. trus add gitignore pilih python 
setelah itu done
7. setelah memiliki repositori klik tombol clone or download lalu ingin menggunakan HTTPS atau SSH 
8. lalu buka git bash nya
9. terus membuat folder nya mkdir python example 
10. lalu mulai git clone trus pastekan SSH atau HTTPS
11. trus di enter deh,

## bagaimana cara commit dan push
1. kita membuat file atau mengubah isi sebuah file dulu
2. save file tersebut dengan ctrl+x
3. setelah itu git status dlu, nah apabila ada informasi tentang perubahan dari file yang kamu kerjakan tadi pastinya
4. nah, setelah itu langsung aja deh ketikkan 
$ git commit -am "pesan mu"
 disini saya jelasin dikit, nah -am itu sebenernya dua perintah loh
yaitu add + massage 
manualnya tuh harus nya
$ git add namafile gitu, tapi ribet mending langsung -am yakkan. 
6. setelah itu git status dlu, pastikan working tree clean
7. nah, kalau sudah begitu lgsg aja 
$ git push. 
8. so, ini masih di repository mu ya, 

eh bakal ada istilah repository dan branch loh.... 
nah, lets go

### kenapa clone lewat ssh daripada https ?
==> because is , harus login terus untuk masuk ke git.hub nya. jadi mending pake ssh aja deh 

#### alasan menggunakan bahasa phyton
=> karena kita telah memasuki dunia IT itu untuk bekerja di perusahan, dan you should know ! dunia perusahaan sekarang lebih memilih menggunakan python loh
lebih efektif dan lebih multiplatform dan juga top 3 di dunia. dengan bahasa penggunaan terbanyak. bersaing dengan java dan PHP. 

# MEMULAI DENGAN PYTHON 
- Pastikan phyton sudah terinstall di Kompumter anda. 
- nah untuk mengecek nya itu ketikkan pada git bash nya
```$ python --version``` terus enter deh 
- nah akan muncul 
python 3.7.5 atau sesuai versi yang anda download

## bagaimana jika python belum terinstall 
ikuti tautan berikut ini : https://www.dicoding.com/academies/86/tutorials/4738?from=4736 
_tapi sebelum itu coba kamu daftar dikoding dulu ya gaess :)_


## Alasan menggunakan bahasa python
Efektifitas Python cukup terbukti dengan banyaknya jumlah pengguna Bahasa ini. Berbagai survei memasukkan Python dalam top-3 sebagai bahasa dengan penggunaan terbanyak, bersaing dengan Java dan PHP. Python dapat digunakan dalam mengakomodasi berbagai gaya pemrograman, termasuk structured, prosedural, berorientasi-objek, maupun fungsional. Python juga dapat berjalan pada berbagai sistem operasi yang tersedia. Beberapa pemanfaatan bahasa Python di antaranya:

1. Web development (server-side),
2. Software development,
3. Mathematics & data science,
4. Machine learning,
5. System scripting.

## Memulai dengan Python
Pastikan anda sudah mengisntal Python, dengan cara tulis "python --version" pada cmd/ git bash anda

## Bagaimana jika python belum ter-instal ?
Maka ikuti tautan berikut ini : https://www.dicoding.com/academies/86/tutorials/4738?from=4736 (Dengan syarat harus daftar akun dicoding terlebih dahulu)

## Hello World dengan python
Masuk ke direktori folder repository ini dengan cara:
```bash
cd /path/nama-direktori
```
catatan : path disini merupakan nama-nama direktori diatas direktori repositori ini, seperti misalnya Document
1. buat sebuah file baru dengan nama main.py, caranya seperti berikut
```
nano main.py
```
2. Masukkan code berikut di dalam main.py
```python
print('Hello world')
```
3. Jalankan file tersebut dengan cara
```bash
python main.py
```
4. Hasil output harusnya sesuai dengan inputannya, yaitu:
```
Hello world
```

# python interpreter
1. intrepreter merupakan program yang dibaca dan dieksekusi pada sebuah sesi pada command line, uuntuk masuk ke intrepeter caranya sebagai berikut :
- buka cmd (windows) / terminal (linux/macos) >> ketikkan 'python'

```python 
py
Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 14 2019, 23:09:19) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
```
# menggunakan modul
module merupakan set program yang sudah disediakan oleh python yang tiinggal pakai contohnya adakah seperti in : 
```python
>>> import datetime 
>>> datetime.datetime.now()
datetime.datetime(2019, 12, 1, 21, 39, 54, 301054)
formatnya itu 
(tahun,bulan,tanggal,jam,menit,detik,milidetik)

``` python 
>>> import random
>>> import string 
>>> def randomword(length):
...     letters = string.ascii_lowercase
...     return ''.join(random.choice(letters) for i in range(length))
...
>>> random_name(2)
'fd'
>>> random_name(29)
'rvkigvbureidixobtylqowqhuqvtm'
```
lalu kita bakal membuat program untuk mengacak nama dari seluruh pelatihan desktop programming amcc dengan contoh kode berikut ini :
``` python
>>> import random
>>> import string 
>>> def randomword(length):
...     name = ('david','sabil','peby','agung','yanuar')
...     return ''.join(random.choice(name) for i in range(1))
...
>>> random_name
>>> 'david'
```
# fungsion 
cirikhasnya menggunakan keyword 
def nama fungsi(param):
    identasi 
return adalah nilai kembalian. 
pemanggilannya hanya menggunakan namafungsi(isi parameternya)
def foo(x):
    if len(x)<8:
        print("password anda kurang dari 8")
        print("jumlah karakternya",len(x))
    else:
        print('password anda berhasil')
        print("jumlah karakternya",len(x))

print(foo("agnespebythalia"))

### control flow
angka=24
run=True
while run:
    x=int(input('masukkan angka:'))  
    if x == angka:
        print("angka yang benar")
        run=False
    elif x < angka:
        print("angka lebih besar sedikit")
    elif x > angka :
        print("angka lebih kecil lagi")
    else:
        print("angka yg anda masukkan kejauhan ")

#ini untuk fungsi memanggil tipe data tupple dan dict
def total (*size, **nilai):
    for i in size:
        print('ukuran sepatunya :',i)
        
    for key, value in nilai.items():
        print(key.capitalize(),value)
total(42, 43, 39, 36, david=70, sabil=80, yanuar=78, peby=81)
// output
ukuran sepatunya : 42
ukuran sepatunya : 43
ukuran sepatunya : 39
ukuran sepatunya : 36
David 70
Sabil 80
Yanuar 78
Peby 81

angka=24
x=int(input('masukkan angka:'))
    
if x == angka:
    print("angka yang benar")
elif x < angka:
    print("angka lebih besar sedikit")
elif x > angka :
    print("angka lebih kecil lagi")
else:
    print("angka yg anda masukkan kejauhan ")

    run=True
while run:
        s = input('ketikkan nama :')        
        if s=='keluar':
            print('selesai')
            run=False
        else:
            print('panjang karakter :',len(s))