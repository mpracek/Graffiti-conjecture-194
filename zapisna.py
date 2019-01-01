#115 120
#V tej datoteki bo zapisan celoten genetski algoritem, ki bo izvedel na� program. Zapisan je v jeziku Sage.
#�elimo dokazati, da obstaja graf G, za katerega ne velja, da zado��a neenakosti 
#neodvistnostno �tevilo(G) =< 1 + povpre�na lokalna neodvistnost(G)
#in nima Hamiltonove poti.

import random
import operator
import math

def nasi_grafi(stevilo_vozlisc):
    """
    Funkcija, ki nam vrne enostavne povezane grafe na dolocenem stevilu vozlisc.
    """
    grafi = list(graphs.nauty_geng(str(stevilo_vozlisc)+" -c"))
    return grafi

def neodvistnostno_stevilo(G):
    """
    Vrne neodvistno �tevilo grafa G
    Za pomo� uporabimo independet_set() iz modula neusmerjenih grafov.
    """
    neodvisno = G.independent_set()
    dolzina = len(neodvisno)
    return dolzina
    
    
def naredi_podgraf(G, seznam):
    """
    Funkcija, ki nam za dan seznam vozli�� vrne podgraf, definiran na le teh
    Seznam je tukaj nabor vozli��, ki nas zanimajo.
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
    Lokalna neodvistnost je neodvistnost podgrafa, ki ga dolo�ajo sosedi vozli��a v,
    za nek v iz mno�ice vozli��.
    """
    mnozica = G[vozlisce]
    novGraf = naredi_podgraf(G, mnozica)
    lokalna_neodvistnost = neodvisnost(novGraf)
    return lokalna

def povprecna(G):
    """
    Vrne povpre�no lokalno neodvisnost grafa G
    """
    povprecje =  0
    for vozlisce in G:
        povprecje += lokalna_neodvisnost(G, vozlisce)
    povprecna_vrednost  = povprecje/ len(G) 
    return povprecna_vrednost

def preverjanje_za_en_graf(G):
    """
    Preveri, ali za en graf velja, �e je ta graf izjema.
    """
    if neodvisnostno_stevilo(G) <= 1 + povprecna(G):
            if hamiltonian.path(G) == None:
                graf = str(G)
                return "Ovrgli smo domnevo in izjema je" + 	graf
    else:
        return "Izjeme nismo ovrgli"

def preverjanje(stevilo_vozlisc):
    """
    Preveri veljavnost konjekture za vse grafe na dolo�enem �tevilu vozli��.
    """
    for G in nasi_grafi(stevilo_vozlisc):
       if neodvisnostno_stevilo(G) <= 1 + povprecna(G):
            if hamiltonian.path(G) == None:
                graf = str(G)
                return "Ovrgli smo domnevo in izjema je" + 	graf
    else:
        return "Izjeme nismo ovrgli"

##Genetski algoritem 

##Initalization -> izbira �tevila za�etnega vzorca
def poisson(t = 1, lambd = 1/2):
    """
    S to funkcijo dolo�imo za�etno �tevilo vozli��
    """
    stevilo_vozlisc = 0
    racunalo = 0
    while racunalo < t:
        stevilo_vozlisc += 1
        racunalo += random.expovariate(lambd)
    return stevilo_vozlisc
		
#Zanimajo nas zgolj enostavni, povezani grafi, zato bomo definirali za�etno mno�ico.
def zacetna_populacija():
    """
    Ta funkcija nam da grafe, na katerih bo opravljen prvi test.
    """	
    stevilo_vozlisc = poisson(t = 1, lambd = 1/2)
    return nasi_grafi(stevilo_vozlisc)
    
#V tem koraku moramo dolo�iti primerno za�etno mno�ico grafov
# Dolo�iti moramo primeren kriterij,
#po katerem bomo grafe iz na�e za�etne mno�ice razporedili

#Odlo�imo se za �im manj�e neodvisnostno �tevilo

def kriterij():
    """"
    Izra�una kriterij, po katerem vse elemente razporedimo.
    """
    populacija = zacetna_populacija()
    slovar = dict()
    for element in populacija:
        racun = neodvisnostno_stevilo(element)
        slovar[element] = racun
    return slovar

def razporedi():
    """
    Razporedi elemente za�etne populacije.
    """
    populacija = kriterij()
    razporejena_populacija = sorted(slovar.items(), key = operator.itemgetter(1))
    nasa_populacija = []
    for osebek in razporejena_populacija:
        nasa_populacija.append(populacija[osebek[0]])
    return nasa_populacija
    
def zacetna_testna_populacija():
    """
    Za za�etni parameter izberemo zacetna_populacija(), ki nam bo vrnila
    vse grafe za�etne velikosti.
    Najprej moramo dolo�iti, kolik�en del za�etne populacije bomo testirali
    V genetiki velja, da ostanejo zgolj najbolj�i, zato bomo vzeli le najbolj�e,
    torej tiste, z minimalnim neodvistnostnim �tevilom.
    """
    populacija = zacetna_populacija()
    delez = random.uniform(0,1)
    odstotek = math.floor( 100 * delez)/100
    dolzina = len(zacetna_populacija())

    vrednost = math.floor(odsotek * dolzina)
    testna_populacija = populacija[:vrednost]
    return testna_populacija

def zacetni_test()
    """
    Funkcija izvede test za na�o za�etno testno populacijo.
    """
    zanima_nas = zacetna_testna_populacija()
    for graf in zanima_nas:
        preverjanje_za_en_graf(graf)

        
#Ko smo opravili za�etni test sledi priprava nove generacije,
#kjer nove testne primerke pripravimo skozi rekombinacijo in mutacijo.

def doda_povezavo(graf):
    """
    Spremeni graf tako, da mu doda povezavo
    """
     	vozlisca = list(graf.keys())
    	vozlisce1 = random.choice(vozlisca)
    	seznam_vseh_vozlisc = list(graf.keys())
	seznam_sosedov =  graf[vozlisce1]
	for element in seznam_vseh_vozlisc:
		if element in seznam_sosedov:
			seznam_sosedov.remove(element)
	nabor = seznam_sosedov
    	nabor = list(nabor)
	vozlisce2 = random.choice(nabor)
	graf.add_edge(vozlisce1, vozlisce2)
	return graf	

def odstrani_povezavo(graf):
	"""
	Odstrani naklju�no povezavo iz grafa;
	Pazimo, da mora graf, ki ga dobimo, biti povezan.
	"""
	vozlisca = list(graf.keys())
    	vozlisce1 = random.choice(vozlisca)
	seznam_sosedov =  graf[vozlisce1]
	vozlisce2 = random.choice(seznam_sosedov)
	graf.delete_edge(vozlisce1, vozlisce2)
	if graf.is_connected():
		return graf
		
	
def mutacija_vozlisce(graf):
	"""
	Doda vozlisce in mu nato doda nekaj povezav nanj.
	"""	
	dolzina = len(list(graf.keys()))
	graf.add_vertex(novo)
	stevilo = randint(0,dolzina)
	vozlisca = list(graf.keys())
	dodaj_vozlisca = random.sample(vozlisca, stevilo)
	for i in range(stevilo):
		graf.add_edge(novo, dodaj_vozlisca[i])
	return graf	

def odstrani_vozlisce(graf):
	vozlisca = list(graf.keys())
	vozlisce1 = random.choice(vozlisca)
	graf.delete_vertex(vozlisce1)
	if graf.is_connected():
		return graf
	
def mutacija(graf):
	"""
	Na grafu lahko odstranimo, dodamo povezavo, dodamo, 	odstranimo vozli��e in vsako kombinacijo le teh.
	"""
	p = random.uniform(0,1)
	if p <= 1/15:
		odstrani_vozlisce(graf)
	elif p > 1/15 and p <= 2/15:
		mutacija_vozlisce(graf)
	elif p > 2/15 and p <= 3/15:
		odstrani_povezavo(graf)
	elif p > 3/15 and p <= 4/15:
		doda_povezavo(graf)
	elif p > 4/15 and p <= 5/15:
		odstrani_vozlisce(graf) and mutacija_vozlisce()
			
	
	
	