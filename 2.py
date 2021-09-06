input_array = input('Masukan angka yang akan di reverse array, pisahkan dengan spasi: ')
print('\n')
arr = input_array.split()
#Print list
print('Array awal:', arr)

#Reversing dengan list slicing
res = arr[::-1]
print('Array akhir:', res)