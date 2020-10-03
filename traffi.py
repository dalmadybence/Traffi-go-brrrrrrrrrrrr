'''D22.txt
10,135,208
H,PMJ-758,A,sz,126,10:01:02
orszag, rendszam, mérőhely, tipus, sebesseg, idő, idő_bontott
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
        self.idő_bontott = 3600 * int(idő[:2]) + 60 * int(idő[3:5]) + int(idő[6:])
        
       
        limit = {'sz' : 130, 'm': 130, 'b': 100, 't': 80, 'mk':float('inf')}
        self.limit    = limit[tipus]
        self.túllépés = self.sebesseg - self.limit
        
        
        
with open('D22.txt', 'r', encoding='UTF-8') as f:
    elso_sor = f.readline().strip().split(',')
    lista = [Traffi(sor) for sor in f]
         
#1.feladat
        

 
kuki = [sor for sor in lista if sor.mérőhely == "A" and sor.tipus == "m" and sor.sebesseg > 130 ]
msz = len(kuki)
print( f'1. feladat:')
print( f'{msz}')

#2.feladat

anyad = [sor for sor in lista if sor.mérőhely == "B" and sor.tipus in {"sz" , "t", "b"} and sor.túllépés > 0]

if anyad :
    for sor in anyad:
        print(f'2.feladat:')
        print(f'{sor.tipus} {sor.orszag} {sor.rendszam} {sor.túllépés}')
else:
    print(f'2.feladat:')
    print("go brrrrrr")

#3.feladat

sebességek   = [sor.sebesseg for sor in lista if sor.mérőhely == 'C']
max_sebesseg = max(sebességek)


XD = [sor for sor in lista if sor.mérőhely == 'C' and sor.sebesseg == max_sebesseg]
üzenet = "túllépte"
üzenet2 = "nem_lépte_túl"

for sor in XD:
    if sor.túllépés > 0 :
        print(f'3.feladat:')
        print(f'{ sor.sebesseg} {üzenet} {sor.tipus} {sor.orszag} {sor.rendszam} {sor.idő}')
    else:
        print(f'3.feladat')
        print(f'{sor.sebesseg} {üzenet2} {sor.tipus} {sor.orszag} {sor.rendszam} {sor.idő}')
        
#4.feladat
# Még nem jó BRRRR

brr = [sor for sor in lista if sor.orszag == "H" and sor.mérőhely in ("A","B","C")]
brrrr = len(brr)

print(f'4.feladat:')
print(f'{brrrr}')


#5.feladat
óto_összidő = [sor for sor in lista if sor.mérőhely == 'C' and 110 < sor.sebesseg <= 130 and sor.tipus == 'sz']

if óto_összidő:
    for sor in óto_összidő:
        print(f'5.feladat:')
        print(f'{sor.orszag} {sor.rendszam} {sor.sebesseg} {sor.idő}')
else:
    print(f'nincsen semmi információ')


#6.feladat


print(f'6.feladat:')

#Ehez lusta voltam.     -Bence


#7.feladat
rszek = {sor.rendszam for sor in lista}

print(f'7.feladat:')

#Ezt nem akartam megcsinálni, csak a 8-ashoz kell nekünk a változója.      -Bence


#8.feladat
rsz = 'NKP-730'         #7. feladatnak eredménye.       -Bence

print(f'8.feladat:')

if rsz in rszek:
    mugli = [sor for sor in lista if sor.rendszam == rszek and sor.sebesseg > 130]

    if mugli:
        print(f'szerepel, túl lépte')
    else:
        print(f'szerepel, nem lépte túl')

else:
    print(f'nem szerepel')
