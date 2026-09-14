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

### Tugas 3
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