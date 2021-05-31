"""R-1.2
Tulis fungsi Python singkat, genap (k), yang mengambil nilai integer dan mengembalikan True jika k genap,
dan False sebaliknya. Namun, fungsi Anda tidak dapat menggunakan operator perkalian, modulo, atau pembagian."""

def is_even(k):
    return False if k & 1 else True

print(is_even(2))
print(is_even(3))
