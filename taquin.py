import time
from tkinter import *
import random
import operator


# initialisation du taquin
t = [0,0,0,0,0,0,0,0,0] 
print(t)


# etat du depart - melanger
def melanger() :
    test=[]
    taq = [0,0,0,0,0,0,0,0,0] 
    for i in range(9):
            n = random.randint(0,8)
            while n in test:
                n = random.randint(0,8)
            test.append(n)
            taq[i]=n 
    return taq
    
# afficher la taquin
def affiche(taq):
    print(taq)
    print("\n --- --- ---")
    i=0
    while i<9:
        print("| {} | {} | {} |".format(taq[i],taq[i+1],taq[i+2]))
        print(" --- --- ---")
        i=i+3


# test etat final
def etat_final(taq):
    final=[1,2,3,4,5,6,7,8,0] 
    return taq == final   


# determiner les etats voisins d'unt etat donné
def voisins(taq):
    i=case_vide(taq)
    if i==2:
        l=[1,5]
    elif i==5:
        l=[4,2,8]
    elif i==3:
        l=[0,4,6]
    elif i==6:
        l=[3,7]
    else:
        l=[i+1,i-1,i+3,i-3]
        for x in l:
            if x not in range(9):
                l.remove(x)

    ll=[numero(t,x) for x in l]
    return l   


# retourner les coordonnées dec  la case vide
def case_vide(taq) :
    for i in range(9):
        if taq[i] == 0:
            return i


# retourna un case choisie
def numero(taq,x):
    return taq[x]


# permuter deux cases    
def permuter(taq,c1,c2):
    aux=taq[c1]
    taq[c1]= taq[c2]
    taq[c2]=aux  
    return taq



t=[1,2,3,4,5,6,0,7,8]
affiche(t)
print(etat_final(t)) 
print(case_vide(t))
print(voisins(t))


""""
def algolarg():
    puzz=t
    queue=[]
    visited=set()
    nodes=[]
    queue.append(puzz)
    coups=0
    #while(queue[0]!=etat_final):
    while(queue):

        for i in voisins(puzz):
            permuter(puzz,case_vide(puzz),i)
            print(puzz)
            if str(puzz) not in visited:
                queue.append(puzz)
                visited.add(str(puzz))
                nodes.append(puzz)
                if etat_final(puzz):
                    print(puzz)
                    break
                coups+=1
        
    print(queue)
    print(nodes)
    print(coups)
    return visited
        
"""

def algolarg():
    puzz=t
    print("Recherche de solution en largeur")
    print(puzz)
    queue = []
    queue.insert(0,puzz)
    seen = []
    seen.insert(0,puzz)
    while queue:
        node = queue.pop(0)
        if etat_final(node):
            print("solution trouvée en", len(seen), " coups")
            seen.append(node)
            break
        for i in voisins(node):
            child=node.copy()
            aux=child[i]
            child[i]=child[case_vide(node)]
            child[case_vide(node)]=aux
            if etat_final(child):
                if str(child) not in seen:
                    queue.append(child)
                break
            if str(child) not in seen:
                queue.append(child)
                seen.append(child)
    print('Time spent:%0.2fs'%(time.time())) 
    return seen

queue=[] 
seen=[] 
success=False   
def algoprof(node):
  global success
  if (success==False and node not in seen):
    if etat_final(node):
      queue.append(node)
      success=True
    queue.append(node)
    seen.append(node)
    index=voisins(node)
    tab=[]
    for i in index:
        child=permuter(node,i,case_vide(node))
        tab.append(child)
    for w in tab:
      if w not in seen and success==False:
         algoprof(w)
  print('Time spent:%0.2fs'%(time.time())) 
  return seen  

def malplace(node):
    tf=[1,2,3,4,5,6,7,8,0]
    nb=0
    for i in range(9):
        if node[i] == tf[i]:
            nb+=1
    return nb+1
def aetoile():
    puzz=t
    print(puzz)
    global j
    queue = []
    queue.append(puzz)
    closed = [] #ensemble contenant les noeuds developpés: "closed"
    closed.append(puzz)
    heur=[]    
    heur.append(malplace(puzz))
    while queue:
        opened= []
        node = queue.pop(0) # on developpe la téte de la file ayant heuristic minimal
        if etat_final(node):
            print("solution trouvée en", len(closed) , " coups")
            closed.append(node)
            break
        for i in voisins(node):
            child=node.copy()
            aux=child[i]
            child[i]=child[case_vide(node)]
            child[case_vide(node)]=aux
            heur.append(malplace(child))
            if str(child) not in closed:
                opened.append(child) # create childs list: "opened"
        heur, opened = (list(t) for t in zip(*sorted(zip(heur, opened))))
        #opened.sort(key = malplace) # file triée selon l'heuristique
        for ch in opened:
            queue.append(ch)
            closed.append(ch)
    return closed


fenetre = Tk()


photos=[]
for i in range(0,9):
	photos.append(PhotoImage(file="./images/"+str(i)+".png"))
Lph = photos[0:9]

can=Canvas( width=180*3,height=180*3,bg='white')
can.pack( side =TOP, padx =20, pady =20)
fenetre['bg']='white'
fenetre.title ('Taquin 3x3')

def mel():
    puzz = melanger()
    print(t)
    for k in range(len(Lph)) :
        eff = can.create_image((30+ 150*(k % 3)), 30+(150*( k // 3)), anchor=NW, image=Lph[0])
        aff = can.create_image((30+ 150*(k % 3)), 30+(150*( k // 3)), anchor=NW ,image = Lph[puzz[k]])

   
def larg():
    l=algolarg()
    for tt in l:
        time.sleep(1)
        print(tt)
        for k in range(len(Lph)) :
            eff = can.create_image((30+ 150*(k % 3)), 30+(150*( k // 3)), anchor=NW, image=Lph[0])
            aff = can.create_image((30+ 150*(k % 3)), 30+(150*( k // 3)), anchor=NW ,image = Lph[tt[k]])


def prof():
    algoprof(t)
    for k in queue:
        print(k)
    
def star():
    l=aetoile()
    for tt in l:
        time.sleep(1)
        print(tt)
        for k in range(len(Lph)) :
            eff = can.create_image((30+ 150*(k % 3)), 30+(150*( k // 3)), anchor=NW, image=Lph[0])
            aff = can.create_image((30+ 150*(k % 3)), 30+(150*( k // 3)), anchor=NW ,image = Lph[tt[k]])

Button(text='Melanger',command=mel).pack(side=LEFT)
Button(text='Largeur',command=larg).pack(side=LEFT)
Button(text='Profondeur',command=prof).pack(side=LEFT)
Button(text='A*',command=star).pack(side=LEFT)
Button(text='Quitter',command=fenetre.quit).pack(side=RIGHT)

for k in range(len(Lph)) :
    eff = can.create_image((30+ 150*(k % 3)), 30+(150*( k // 3)), anchor=NW, image=Lph[0])
    aff = can.create_image((30+ 150*(k % 3)), 30+(150*( k // 3)), anchor=NW ,image = Lph[t[k]])



can.pack()
fenetre.mainloop()
  

