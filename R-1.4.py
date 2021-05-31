"""R-1.4
  Tulis fungsi Python singkat yang mengambil bilangan bulat positif n dan mengembalikan jumlah kuadrat
  dari semua bilangan bulat positif lebih kecil dari n."""


def sum_of_squares(n):
    i=0
    total = 0
    while i < n:
        total += i**2
        i += 1
    return total


print('sum of squares')
print(sum_of_squares(3))
