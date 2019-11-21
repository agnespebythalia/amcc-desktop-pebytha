
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


