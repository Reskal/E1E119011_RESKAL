"""C-1.13

Tulis deskripsi pseudo-code dari suatu fungsi yang membalik daftar n bilangan bulat,
sehingga nomor-nomor tersebut didaftarkan dengan urutan berlawanan dari sebelumnya, dan bandingkan
metode ini ke fungsi Python yang setara untuk melakukan hal yang sama."""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def reverse(data):
    temp = []
    n = len(data) - 1
    for thing in range(n, -1, -1):
        temp.append(data[thing])
    return temp


print(my_list)

print(reverse(my_list))
