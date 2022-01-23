'''
Szavak.
A program kérjen be két szót a felhasználótól, majd írja ki, hogy melyik a hosszabb! 
A program üzeneteinek megfogalmazásában kövesse az alábbi mintát:
-----
Adj meg egy szót! kelkáposzta
Adj meg egy másik szót! kisegér
A hosszabb szó: kelkáposzta
---- 
Adj meg egy szót! kelkáposzta
Adj meg egy másik szót! káposztafej
A két szó egyforma hosszú.
----- 
Adj meg egy szót! árvíztűrő
Adj meg egy másik szót! tükörfúrógép
A hosszabb szó: tükörfúrógép
'''

szavak1 = input("Adj meg egy szót!: ")
szavak2 = input("Adj meg egy másik szót!: ")

if len(szavak1) > len(szavak2):
  print(f"A hosszabb szó:{szavak1}")
elif len(szavak1) < len(szavak2):
  print(f"A hosszab szó:{szavak2}")
else:
  print("A két szó egyforma hosszú.")