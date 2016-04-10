#!/usr/bin/python
def loadfmap( fname ):
    fmap = {}
    nmap = {}

    for l in open( fname ):
        arr = l.split()
        if arr[0].find('.') != -1:
            idx = int( arr[0].strip('.') )
            assert idx not in fmap
            fmap[ idx ] = {}
            ftype = arr[1].strip(':')
            content = arr[2]
        else:
            content = arr[0]
# such as that: 1. cap-shape:          bell=b,conical=c,convex=x
# idx=1, ftype="cap-shape", content="bell=b,conical=c,convex=x"
# k="bell" -> v="b"
        for it in content.split(','):
            if it.strip() == '':
                continue
            k , v = it.split('=')
            fmap[ idx ][ v ] = len(nmap)	#Ë«ÖØ×Öµä
            nmap[ len(nmap) ] = ftype+'='+k
            print fmap,nmap
    return fmap, nmap
'''
	1. cap-shape:                bell=b,conical=c,convex=x,flat=f,knobbed=k,sunken=s
    2. cap-surface:              fibrous=f,grooves=g,scaly=y,smooth=s
    3. cap-color:                brown=n,buff=b,cinnamon=c,gray=g,green=r,pink=p,purple=u,red=e,white=w,yellow=y
    4. bruises?:                 bruises=t,no=f
    5. odor:                     almond=a,anise=l,creosote=c,fishy=y,foul=f,
                                 musty=m,none=n,pungent=p,spicy=s
fmap:
{1: {'c': 1, 'b': 0, 'f': 3, 'k': 4, 's': 5, 'x': 2}, 2: {'y': 8, 's': 9, 'g':
7, 'f': 6}, 3: {'c': 12, 'b': 11, 'e': 17, 'g': 13, 'n': 10, 'p': 15, 'r': 14, '
u': 16, 'w': 18, 'y': 19}, 4: {'t': 20, 'f': 21}, 5: {'a': 22, 'c': 24, 'f': 26,
 'm': 27, 'l': 23, 'n': 28, 'p': 29, 's': 30, 'y': 25}}
nmap:
{0: 'cap-shape=bell', 1: 'cap-shape=conical', 2: 'cap-shape=convex', 3: 'cap-shape=flat', 4: 'cap-shape
=knobbed', 5: 'cap-shape=sunken', 6: 'cap-surface=fibrous', 7: 'cap-surface=groo
ves', 8: 'cap-surface=scaly', 9: 'cap-surface=smooth', 10: 'cap-color=brown', 11
: 'cap-color=buff', 12: 'cap-color=cinnamon', 13: 'cap-color=gray', 14: 'cap-col
or=green', 15: 'cap-color=pink', 16: 'cap-color=purple', 17: 'cap-color=red', 18
: 'cap-color=white', 19: 'cap-color=yellow', 20: 'bruises?=bruises', 21: 'bruise
s?=no', 22: 'odor=almond', 23: 'odor=anise', 24: 'odor=creosote', 25: 'odor=fish
y', 26: 'odor=foul', 27: 'odor=musty', 28: 'odor=none', 29: 'odor=pungent', 30:
'odor=spicy'}
'''

