from gempa import *
# membuat objek gempa dengan lokasi dan skala

gempa1 = gempa('banten', 1.2)
gempa2 = gempa('palu', 6.1)
gempa3 = gempa('cianjur', 5.6)
gempa4 = gempa('jayapura', 3.3)
gempa5 = gempa('garut', 4.0)

# info gempa
print("## gempa bumi info maseh ##")
print()
gempa1.dampak() # memanggil method

print("## gempa bumi info maseh ##")
print()
gempa2.dampak() # memanggil method

print("## gempa bumi info maseh ##")
print()
gempa3.dampak() # memanggil method

print("## gempa bumi info maseh ##")
print()
gempa4.dampak() # memanggil method

print("## gempa bumi info maseh ##")
print()
gempa5.dampak() # memanggil method