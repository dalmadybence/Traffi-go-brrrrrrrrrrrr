'''D22.txt
10,135,208
H,PMJ-758,A,sz,126,10:01:02
orszag, rendszam, mérőhely, tipus, sebesseg, idő
'''
class Traffi:
    def __init__(self, sor):
        orszag, rendszam, mérőhely, tipus, sebesseg, idő= sor.strip().split(',')
        self.orszag  = orszag
        self.rendszam  = rendszam
        self.mérőhely  = mérőhely
        self.tipus  = tipus
        self.sebesseg  = int(sebesseg)
        self.idő  = idő
        
       
        limit = {'sz' : 130, 'm': 130, 'b': 100, 't': 80, 'mk':float('inf')}
        self.limit    = limit[tipus]
        self.túllépés = self.sebesseg - self.limit
        
        
        
with open('D22.txt', 'r', encoding='UTF-8') as f:
    elso_sor = f.readline().strip().split(',')
    lista = [Traffi(sor) for sor in f]
         
#1.feladat
        

 
kuki = [sor for sor in lista if sor.mérőhely == "A" and sor.tipus == "m" and sor.sebesseg > 130 ]
msz = len(kuki)
print( f'1. feladat')
print( f'{msz}')

#2.feladat

anyad = [sor for sor in lista if sor.mérőhely == "B" and sor.tipus in {"sz" , "t", "b"} and sor.túllépés > 0]

if anyad :
    for sor in anyad:
        print(f'2.feladat')
        print(f'{sor.tipus} {sor.orszag} {sor.rendszam} {sor.túllépés}')
else:
    print(f'2.feladat')
    print("go brrrrrr")

#3.feladat

sebességek   = [sor.sebesseg for sor in lista if sor.mérőhely == 'C']
max_sebesseg = max(sebességek)


XD = [sor for sor in lista if sor.mérőhely == 'C' and sor.sebesseg == max_sebesseg]
üzenet = "túllépte"
üzenet2 = "nem_lépte_túl"

for sor in XD:
    if sor.túllépés > 0 :
        print(f'3.feladat')
        print(f'{ sor.sebesseg} {üzenet} {sor.tipus} {sor.orszag} {sor.rendszam} {sor.idő}')
    else:
        print(f'3.feladat')
        print(f'{sor.sebesseg} {üzenet2} {sor.tipus} {sor.orszag} {sor.rendszam} {sor.idő}')
        
#4.feladat
# Még nem jó BRRRR

brr = [sor for sor in lista if sor.orszag == "H" and sor.mérőhely in ("A","B","C")]
brrrr = len(brr)

print(f'4.feladat')
print(f'{brrrr}')
    
   