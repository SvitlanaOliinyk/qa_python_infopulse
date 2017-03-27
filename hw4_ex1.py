fir_file = open("file1.txt", "w+")
sec_file = open("file2.txt", "w")
fir_file.write("Первая строка.\nВторая строка.\nТретья строка.")

fir_file.seek(0)
k = 0
for i in fir_file:
    print(str(k) + ':' + i, file=sec_file)
    k += 1


fir_file.close()
sec_file.close()