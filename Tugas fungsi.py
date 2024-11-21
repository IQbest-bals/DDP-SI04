def celcius_ke_farenheit(celcius):
    print(celcius * 9/5 + 32) 
celcius_ke_farenheit(0)

print('\n---- Mencari bilangan genap ----')
def is_genap(genap):
  print(genap %2 == 0)
is_genap(4)  
is_genap(7)

print('\n---- Mencari keterangan lulus tidak lulus ----')
def skor(nilai):
  if nilai >= 80:
    print("lulus")
  else:
    print('gagal')
skor(60)


def bil_ganjil(ganjil):
  for i in range(1,ganjil+1, 2):
    print(i, end=' ')
bil_ganjil(30)    


     