''' C-1.15
Menulis fungsi Python yang mengambil urutan angka dan menentukan
jika semua angka berbeda satu sama lain (yaitu, mereka berbeda).'''

def are_distinct(data):
    count = 0
    for k in data:
        for j in range(1, len(data) - 1):
            if k == j:
                count += 1
                if count == 2:
                    return False
    return True
evens = [2, 4, 6, 8]
alpha = [2, 2, 3, 4, 5, 6, 7, 8, 99]
print(are_distinct(evens))
print(are_distinct(alpha))
