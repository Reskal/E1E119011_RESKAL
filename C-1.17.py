'''
C-1.17
Seandainya kita mengimplementasikan fungsi skala (halaman 25) sebagai berikut, apakah itu berhasil
tepat?

def scale(data, factor):
for val in data:
val = factor
Explain why or why not. '''


''' Ini tidak akan berhasil. val adalah alias ke elemen aktual dalam data dan menugaskan objek baru ke dalamnya hanya akan mengubah nilai val. '''
