import os
try:
	import random
except:
    os.system("pip install random2")
try:	
	from colorama import Fore, Style
except:
    os.system("pip install colorama")

print("\n==============")
print("Tools Menghafal")
print("Rumus Refleksi dan Rotasi")
print("By eskaerpe")
print("============================")
print("Ketik 00 untuk mengakhiri\n")
materi = {
	"Rotasi 90" : "-y,x",
	"Rotasi 180" : "-x,-y",
	"Rotasi 270" : "y,-x",
	"Rotasi 360" : "x,y",
	
	"Refleksi sumbu x" : "x,-y",
	"Refleksi sumbu y" : "-x,y",
	"Refleksi titik pusat O(0,0)" : "-x,-y",
	"Refleksi y=x" : "y,x",
	"Refleksi y=-x" : "-y,-x",
	"Refleksi x=a" : "2a-x,y",
	"Refleksi y=b" : "x,2b-y"
}

while 1:
	random_key = random.choice(list(materi.keys()))
	soal = f"{random_key} -> "
	jawaban = str(input(soal))

	if jawaban == materi[random_key]:
		print(Fore.GREEN+"Benar"+Style.RESET_ALL)
	elif jawaban == "00":
		exit(0)
	else:
		print(Fore.RED+"Salah"+Style.RESET_ALL+f" yang benar adalah {Fore.GREEN}{materi[random_key]}{Style.RESET_ALL}")
