""" R-1.3
Tulis fungsi Python singkat, minmax (data), yang mengambil urutan satu atau lebih angka,
dan mengembalikan angka terkecil dan terbesar, dalam bentuk tupel dengan panjang dua.
Jangan gunakan fungsi bawaan min atau maks dalam mengimplementasikan solusi Anda. """

def minmax(data):
    largest = data[0]
    smallest = data[0]
    for item in data:
        if item > largest:
            largest = item
        elif item < smallest:
            smallest = item
    return smallest, largest


alpha = [2, 2, 3, 4, 5, 6, 7, 8, 99]

print(minmax(alpha))
