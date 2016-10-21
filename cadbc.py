import os

kosong = ["kosong"]
file = raw_input("Sebutkan file yang memuat kunci dan jawaban: ")
with open(file) as baca_file:
	file_list = baca_file.read().splitlines()
	kunci = file_list[0]
	kunci_list = list(kunci)
	kunci_list = kosong + kunci_list
	file_output = file[:-4] + " output.txt"
	with open(file_output, "w") as tulis_file_output:
		for x in range(2, len(file_list)):
			bagi_jawaban = file_list[x].split(": ")
			tulis_file_output.write("Nama siswa:\n%r\n\n" % bagi_jawaban[0])
			bagi_jawaban_list = list(bagi_jawaban[1])
			bagi_jawaban_list = kosong + bagi_jawaban_list
			tulis_file_output.write("Jawaban:\n%r\n\n" % bagi_jawaban_list)
			jawaban_benar = []
			jawaban_salah = []
			for x in range(len(bagi_jawaban_list)):
				if kunci_list[x] == bagi_jawaban_list[x]:
					jawaban_benar.append(x)
				else:
					jawaban_salah.append(x)
			nilai = float(len(jawaban_benar) - 1) / (len(jawaban_benar) - 1 + len(jawaban_salah)) * 100
			tulis_file_output.write("Aitem jawaban benar:\n%r\n\n" % jawaban_benar)
			tulis_file_output.write("Aitem jawaban salah:\n%r\n\n" % jawaban_salah)
			tulis_file_output.write("Jawaban benar:\n%r aitem\n\n" % (len(jawaban_benar) - 1))
			tulis_file_output.write("Jawaban salah:\n%r aitem\n\n" % len(jawaban_salah))
			tulis_file_output.write("Nilai:\n%r\n\n" % nilai)
			tulis_file_output.write("-" * 100)
			tulis_file_output.write("\n\n")
os.system("subl 'matematika output.txt'")