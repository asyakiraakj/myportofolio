Nama : Khadijah Asy Syakira

NPM : 2506610595

Kelas : PBP E

### Tugas 1
1. Ya, saya menggunakan elemen semantik html5 yaitu `<section>` untuk bagian "Experience". Elemen ini membantu saya untuk membagi-bagi halaman portofolio menjadi beberapa bagian spesifik.
2. Saya menggunakan grid di *section* "Experience". Di mana grid di desktop terdiri dari 3 kolom dengan ukuran yang berbeda. Sedangkan di mobile saya menggantinya menjadi 1 kolom dengan 3 baris. Saya memutuskan untuk mengubah tata letak di mobile menjadi 3 baris karena menurut saya itu lebih terlihat rapi untuk layar yang cenderung panjang (secara vertikal). Sedangkan untuk layar lebar (secara horizontal) akan lebih cocok jika kontennya juga melebar. Posisi konten yang tadinya kiri-tengah-kanan saya ubah menjadi atas-tengah-bawah, dengan begitu urutan konten tidak berubah, hanya posisinya saja sehingga informasi yang saya sampaikan akan tetap sama di device mana pun.
3. Sejauh ini saya belum merasakan batasan yang sangat mengganngu dan saya rasa informasi yang ingin saya sampaikan sudah cukup optimal. Untuk iterasi proyek selanjutnya, mungkin saya akan menambahkan animasi sederhana seperti fade-in untuk *section heading*.

#### AI Disclosure
Saya menggunakan bantuan generative AI yaitu Gemini untuk hal-hal sebagai berikut:
- Meminta membuatkan paragraf untuk section experience di bagian 'paragraph'.
- Meminta rekomendasi *commit message*.
- Debugging saat terjadi bug/error, meminta saran/rekomendasi:
    - [css styling (grid)](https://share.gemini.google/DpLEh1Rx7fTM)
    - [lag/hang saat `runserver`](https://share.gemini.google/mAqFOTsetMGC)


### Tugas 2
1. Awalnya server menerima *request* dari user. *Request* ini ini diterima pertama kali oleh `urls.py` proyek (`portfolio/urls.py`). Kemudian diteruskan ke `urls.py` aplikasi (`main/urls.py`). Setelah itu, `urls.py` aplikasi memilih *view* mana yang cocok untuk setiap halaman (di `views.py`). Kemudian, `views.py` menerima permintaan tersebut, mengambil data dari *model*, dan mengirimkannya ke *template*. `models.py` mengelola data dalam sebuah aplikasi. `template/` berisi dokumen template kerangka html yang mengatur tampilan web. Setelah *view* memproses datannya menjadi dokumen html, dokumen ini akan dikirimkan kembali dan ditampilkan ke user.
2. Berdasarkan aturan *separation of concerns*, data sebaiknya disimpan pada *model* dan tidak langsung ditulis pada *template*. *Models* bertugas menyimpan data dan tidak perlu memikirkan bagaimana data tersebut ditampilkan. *Template* bertugas menampilkan data dan tidak perlu memikirkan bagaimana data tersebut disimpan. Selain itu, memisahkan *models* dan *template* (lalu menghubngkan *models* *template* dengan *view*) juga akan mempermudah kita jika ingin pelakukan perubahan data. Contohnya jika ingin menambah data, kita hanya perlu menambahkannya melalui python shell tanpa perlu memikirkan bagaimana data baru tersebut ditampilkan, tanpa perlu mengedit html code. Selain itu, models juga memudahkan kita jika ingin mencari, memfilter, atau mengurutkan data. Contohnya di section skills, saya memfilter skills berdasarkan tipe (hard/soft) agar nantinya dapat ditampilkan secara terpisah.
3. `makemigrations` bertugas mendeteksi perubahan pada `models.py`, instruksi ini menghasilkan file baru di dalam folder `main/migrations/`. `migrate` bertugas mengeksekusi file-file instruksi migrasi. Contoh: di section skills, saya menambahkan field baru yaitu `type` yang berisi soft/hard.

#### AI Disclosure
Saya menggunakan bantuan generative AI yaitu Gemini dan Github untuk hal-hal sebagai berikut:
- css:
    - menanyakan penyebab error/bug: hard skills tidak dapat ditampilkan: [Copilot](https://drive.google.com/file/d/1_hy4obdOcOQjk4TfjTlYeCfD5zw5XNjV/view?usp=sharing) [Gemini](https://share.gemini.google/feMBJMqdnu5c)
    - [menanyakan penyebab gap di bawah heading soft skills](https://drive.google.com/file/d/17sE_m8cvdkKkgIB8CxP9LkpxRj4rF2JQ/view?usp=sharing)
- [bertanya bagaimana cara *update* object di django models.](https://share.gemini.google/FKoXm6pgSmWl)
- [meminta membuatkan to-do list detail dengan estimasi waktu untuk tugas 2, meminta saran terkait pemisahan/kategorisasi skill, update/delete object di django models](https://share.gemini.google/lx4jBmD5XRsU)

### Tugas 3
1. `ModelForm` dipakai karena `ModelFrom` bisa otomatis membuat form berdasarkan model yang sudah ada, sehingga kita tidak perlu menulis tag input HTML manual dan data bisa langsung disimpan ke database lewat `form.save()`. Tag `{% csrf_token %}` wajib ada untuk mengamankan form dari request palsu (CSRF).
2. Alasan JSON lebih disukai dalam pengembangan aplikasi web modern dibandingkan XML adalah karena penulisannya yang lebih ringkas dan mudah dibaca/dipahami. JSON menggunakan struktur key-value. JSON juga tidak membutuhkan tag pembuka dan penutup seperti XML.
3. Alurnya dimulai saat ada request ke URL terkait, lalu fungsi *view* mengambil data dari database, mengubahnya ke format JSON dengan `serializers.serialize('json', data)`, dan mengirimkannya lewat `HttpResponse(...,content_type="application/json")`. Proses serialisasi ini penting dilakukan karena objek model bawaan Python tidak bisa langsung dikirim atau dibaca oleh browser/*frontend*, sehingga harus diubah dulu menjadi teks standar (JSON).
#### AI Disclosure
[Lampiran AI Chat Log (Github Copilot)](https://drive.google.com/drive/folders/1IFRRSKI-UDp6Rf7H0ZeQG8ITOfM7LIEG?usp=sharing)
[Lampiran AI Chat Log (Gemini)](https://share.gemini.google/cCGaGx1z0Wcf)
<br>**Analisis Kekurangan AI**
- Saat diminta untuk memperbaiki *button alignment* di experience card hasilnya masih kurang memuaskan. Jadi saya menganalisis kembali file `style.css` dan memperbaikinya sebisa saya.

### Tugas 4
#### AI Disclosure
Saya menggunakan bantuan generative AI yaitu Gemini untuk hal-hal berikut:
- [authorization, fitur star, keamanan data](https://share.gemini.google/Eh6St2vIRKW6)
- [fix css not updated](https://share.gemini.google/iFMlAfztH5HN)
<br>**Analisis Kekurangan AI**
Ketika saya meminta bantuan AI untuk memperbaiki CSS yang tidak ter-*update* di skills card, AI tidak meng*suggest* solusi untuk mengecek penulisan nama class di `style.css`, padahal setelah saya coba-coba dan cek kembali, ternyata di situlah letak kesalahan yang membuat CSS saya tidak ter-*update*.

### Tugas 5
1. Jelaskan apa itu debouncing dan mengapa teknik ini penting diterapkan pada fitur pencarian yang menggunakan AJAX!<br>
Debouncing adalah teknik untuk menunda eksekusi sebuah fungsi sampai user berhenti melakukan sesuatu (misalnya mengetik) setelah jeda waktu tertentu. Debouncing penting diterapkan di fitur pencarian karena jika tidak diterapkan, AJAX akan mengirimkan request ke server setiap user mengetikkan satu hurug di fitur pencarian.
2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?<br>
`await` berguna untuk menyuruh JavaScript agar menunggu sampai proses pengambilan data (*fetch*) selesai dari server, baru lanjut eksekusi baris kode di bawahnya. Jika tidak menggunakan `await`, JavaScript akan langsung lanjut mengeksekusi baris-baris kode selanjutnya padahal datanya belum sampai. Akibatnya, variabel (yang dibuat untuk menampung hasil `fetch()`) hanya akan berisi `Promise` yang statusnya *pending*.
3. Jelaskan apa itu serangan XSS (Cross-Site Scripting) dan mengapa data yang ditampilkan melalui AJAX/JavaScript lebih rentan terhadap serangan ini daripada data yang ditampilkan langsung melalui template Django!<br>
*XSS (Cross-Site Scripting)* adalah serangan dimana ketika seseorang menyelipkan script ke dalam input web kita yang mana script tersebut ikut tereksekusi di browser. AJAX/JavaScript lebih rentan terhadap serangan ini karena jika kita mengambil dan menampilkan data menggunakan AJAX/JavaScript, data tersebut langsung dimasukkan mentah-mentah. Berbeda jika menggunakan Django, Django akan otomatis melakukan *auto-escaping*.
#### AI Disclosure
Saya menggunakan bantuan generative AI yaitu Gemini.<br>
[Lampiran AI chat log Tugas 5](https://share.gemini.google/PxOBsvTnaVs8)
<br>**Analisis Kekurangan AI**<br>
Pada awalnya experience cards saya tidak ter render sama sekali. Ketika saya mencoba menanyakan kepada AI penyebabnya apa, dia tidak menemukan kesalahannya dimana atau perbaikan yang dia sebutkan belum sepenuhnya menyelesaikan masalah tersebut. Setelah itu saya coba perhatikan kembali dan saya curiga masalahnya terdapat di *url path*, lalu saya *suggest* apakah mungkin masalahnya berada di *url path* dan ternyata benar.

### Tugas 6
**1. Jelaskan apa yang dimaksud dengan REST dan mengapa mengembalikan JSON saja belum cukup untuk menyebut sebuah API sebagai RESTful! Jelaskan pula perbedaan PUT dan PATCH beserta contoh kapan masing-masing sebaiknya digunakan!<br>**
REST (Representational State Transfer) adalah arsitektur untuk merancang web API. Di REST API, data diperlakukan sebagai resource. URL menunjuk ke data, misalnya /api/v1/skills/ untuk kumpulan skill dan /api/v1/skills/<uuid>/ untuk satu skill. Selain itu, HTTP method menyatakan tindakan. GET untuk membaca, POST untuk membuat, PUT/PATCH untuk mengubah, DELETE untuk menghapus. Jadi tindakan tidak perlu ditulis di URL (contoh lama: /projects/add-ajax/). Selain itu, di RESTful API, klien dan server bertukar representasi data, yaitu JSON, bukan objek Python atau baris database.<br>
Mengapa JSON saja belum cukup disebut RESTful? Karena yang menentukan RESTful atau tidak adalah cara API itu diatur, bukan format datanya. Endpoint buatan sendiri seperti /skills/add-ajax/ memang mengembalikan JSON, tetapi tindakannya ditulis di URL dan memakai method yang tidak sesuai. Jadi API itu belum bisa disebut RESTful.<br>
Perbedaan PUT dan PATCH: PUT mengirmkan representasi pengganti, semua field wajib dikirim. Sedangkan PATCH hanya mengirimkan field yang ingin diubah

**2. Jelaskan peran serializer pada Django REST Framework! Apa keuntungannya dibandingkan merakit dictionary secara manual dengan JsonResponse seperti pada Tutorial 05?**<br>
Peran serializer:
- Serializaition (GET): mengubah objek model menjadi tipe data Python yang bisa dirender menjadi JSON.
- Deserialization (POST/PATCH): mengubah input dari klien menjadi data yang sudah divalidasi dan siap disimpan (`.is_valid()` lalu `.save()`).
Selain itu, serializer juga menentukan field apa saja yang dikirim dan field mana yang hanya bisa dibaca. Adapun keuntungan dibanding menggunakan `JsonResponse` manual di antaranya:
- Tidak perlu merakit dictionary satu per satu dalam loop.
- Validasi input ada di satu tempat (`validate_title`, validasi URL otomatis dari model)
- ModelSerializer sudah menyediakan `create()` dan `update()`.
- Field hasil perhitungan (`star_count`, `is_starred`) mudah dibuat dan tidak bisa diisi klien.
- Tidak mengulang pola yang sama ketika Model atau section lain juga butuh API.

**3. Jelaskan perbedaan autentikasi dan otorisasi pada Django REST Framework! Mengapa hak akses harus diperiksa dengan permission class di server, bukan hanya dengan menyembunyikan tombol di template?**<br>
Autentikasi berkaitan dengan *role* user atau "siapa". Di DRF, *authentication class* (di sini `SessionAuthentication`) mengisi `request.user`. Sedangkan otorisasi berkaitan dengan apa saja yang dapat dilakukan oleh user dengan role terstentu. Di DRF, permission class (di sini `IsPortfolioOwnerOrReadOnly`) memutuskan apakah request boleh diteruskan.
Hak akses harus diperiksa dengan permission class karena menyembunyikan tombol hanya mengatur tampilan, bukan izin sesungguhnya. Orang tetap bisa mengirim request langsung ke API, misalnya lewat Console browser atau Browsable API, tanpa memakai tombol itu.<br>

**4. Jelaskan mengapa permintaan yang mengubah data tetap memerlukan token CSRF ketika API memakai SessionAuthentication! Mengapa test yang memakai force_authenticate tidak cukup untuk membuktikan bahwa perlindungan CSRF berjalan?**<br>
Token CSRF tetap diperlukan karena `SessionAuthentication` mengenali pengguna lewat cookie session, dan browser mengirim cookie itu secara otomatis. Karena itu, untuk akun yang terautentikasi lewat session, request yang mengubah data harus menyertakan token CSRF. Jika token tidak ada atau salah, hasilnya 403. <br>`force_authenticate` saja tidak cukup karena tidak menguji proses login maupun CSRF. Karena itu kita perlu menambah dua test khusus memakai `APIClient(enforce_csrf_checks=True)` dan `.login()` yang membuat session sungguhan:
- POST tanpa token CSRF harus ditolak (403) dan data tidak tersimpan.
- POST dengan token CSRF (diambil dari Browsable API) harus berhasil (201).
<br>
#### AI Disclosure
Saya menggunakan Generative AI yaitu Claude dan ChatGPT (Codex)
AI Chat Log:
- https://chatgpt.com/s/cx_6af1c9aaada08191a37004ad351317ed
- https://chatgpt.com/s/cx_6af1ca445fcc8191b865eb84b8272092
- https://claude.ai/share/e70637d8-2b86-4169-aab2-b385c6f388c8
**Analisis Kekurangan AI**<br>
AI sering kali memberikan solusi yang cukup rumit dan banyak menambah fungsi atau kode yang kurang penting atau redundan sehingga harus diperbaiki dan disesuaikan lagi.