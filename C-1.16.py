'''C-1.16

 Dalam implementasi fungsi skala (halaman 25), badan perulangan
mengeksekusi data perintah [j] = faktor. Kami telah membahas numerik itu
tipe tidak dapat diubah, dan penggunaan operator = dalam konteks ini menyebabkan
pembuatan instance baru (bukan mutasi dari instance yang sudah ada).
Lalu, bagaimana mungkin penerapan skala kita mengubah
parameter sebenarnya yang dikirim oleh pemanggil?'''

answer:

Alasan mengapa parameter aktual yang dikirim oleh pemanggil fungsi diubah adalah karena parameternya adalah daftar (larik)
dan elemen tertentu dari larik tersebut ditetapkan ke objek numerik baru.
