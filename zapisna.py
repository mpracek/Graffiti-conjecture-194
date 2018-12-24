#115 120
#V tej datoteki bo zapisan celoten genetski algoritem, ki bo izvedel naš program. Zapisan je v jeziku Sage.
#Želimo dokazati, da obstaja graf G, za katerega ne velja, da zadošča neenakosti 
#neodvistnostno število(G) =< 1 + povprečna lokalna neodvistnost(G)
#in nima Hamiltonove poti.

def nasi_grafi(stevilo_vozlisc):
    """
    Funkcija, ki nam vrne enostavne povezane grafe na dolocenem stevilu vozlisc.
    """
    grafi = list(graphs.nauty_geng(str(stevilo_vozlisc)+" -c"))
    return grafi

def neodvistnostno_stevilo(G):
    """
Vrne neodvistno število grafa G
    """
    if len(G.vertices()) == 1:
     	return 1
    p = MixedIntegerLinearProgram(maximization = True)
    b = p.new_variable(binary = True)
    p.set_objective( sum([b[v] for v in G]) )
    for u,v in g.edges(labels = False):
    	p.add_constraint( b[u] + b[v] <= 1 )
    p.solve()
    b = p.get_values(b)
    print [v for v,i in b.items() if i]

def naredi_podgraf(G, seznam):
    """
    Funkcija, ki nam za dan seznam vozlišč vrne podgraf, definiran na le teh
    Seznam je tukaj nabor vozlišč, ki nas zanimajo.
    """
    nov_graf = dict()
    for vozlisce in G:
	if vozlisce not in seznam:
	    G.pop(vozlisce)
	else:
	    for sosed in G[vozlisce]:
		    sosedi = G[vozlisce]
		    if sosed not in seznam:
		    	sosedi.remove(sosed)
	    nov_graf[sosed] = sosedi
    return nov_graf
				
	
def lokalna_neodvistnost(G, vozlisce):
    """
    Vrne lokalno neodvistnost grafa G v vozliscu v.
    Lokalna neodvistnost je neodvistnost podgrafa, ki ga določajo sosedi vozlišča v,
    za nek v iz množice vozlišč.
    """
    mnozica = G[vozlisce]
    novGraf = naredi_podgraf(G, mnozica)
    lokalna_neodvistnost = neodvisnost(novGraf)
    return lokalna

def povprecna(G):
    """
    Vrne povprečno lokalno neodvisnost grafa G
    """
    povprecje =  0
    for vozlisce in G:
	povprecje += lokalna_neodvisnost(G, vozlisce)
    povprecna_vrednost  = povprecje/ len(G) 
    return povprecna_vrednost

def preverjanje(stevilo_vozlisc):
    for G in nasi_grafi(stevilo_vozlisc):
	if neodvisnostno_stevilo(G) =< 1 + povprecna(G):
	    if hamiltonian.path(G) == None:
		graf = str(G)
		return "Ovrgli smo domnevo in izjema je" + graf
	else:
		return "Izjeme nismo ovrgli"

##Genetski algoritem 
import random
import operator
import math
##Initalization -> izbira števila začetnega vzorca
def poisson(t = 1, lambd = 1/2):
    """
    S to funkcijo določimo začetno število vozlišč
    """
    stevilo_vozlisc = 0
    racunalo = 0
    while racunalo < t:
        stevilo_vozlisc += 1
        racunalo += random.expovariate(lambd)
    return stevilo_vozlisc
		
#Zanimajo nas zgolj enostavni, povezani grafi, zato bomo definirali začetno množico.
def zacetna_populacija():
    """
    Ta funkcija nam da grafe, na katerih bo opravljen prvi test.
    """	
    stevilo_vozlisc = poisson(t = 1, lambd = 1/2)
    return preverjanje(stevilo_vozlisc)
    
