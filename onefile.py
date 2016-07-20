import sys
import os

numPoke = 0
numEvolv = 0
numCandy = -1
numPokeNew = 0
numCandyNew = 0
numEvolvcount = 0
pokedex = { 'bulbasaur' : 25, 'ivysaur' :  100, 'charmander' : 25, 'charmeleon' : 100, 'squirtle' : 25, 'wartortle' : 100, 'caterpie' : 12, 'metapod' : 50, 'weedle' : 12, 'kakuna' : 50, 'pidgey' : 12, 'pidgeotto' : 50, 'rattata' : 25, 'spearow' : 50, 'ekans' : 50, 'pikachu' : 50, 'sandshrew' : 50, 'nidoranf' : 25, 'nidorina' : 100, 'nidoran' : 25, 'nidorino' : 100, 'clefairy' : 50, 'vulpix' : 50, 'jigglypuff' : 50, 'zubat' : 50, 'oddish' : 25, 'gloom' : 100, 'paras' : 50, 'venonat' : 50, 'diglett' : 50, 'meowth' : 50, 'psyduck' : 50, 'mankey' : 50, 'growlithe' : 50, 'poliwag' : 25, 'poliwhirl' : 100, 'abra' : 25, 'kadabra' : 100, 'machop' : 25, 'machoke' : 100, 'bellsprout' : 25, 'weepinbell' : 100, 'tentacool' : 50, 'geodude' : 25, 'graveler' : 100, 'ponyta' : 50, 'slowpoke' : 50, 'magnemite' : 50, 'doduo' : 50, 'seel' : 50, 'grimer' : 50, 'shellder' : 50, 'gastly' : 25, 'haunter' : 100, 'drowzee' : 50, 'krabby' : 50, 'voltorb' : 50, 'exeggcute' : 50, 'cubone' : 50, 'koffing' : 50, 'rhyhorn' : 50, 'horsea' : 50, 'goldeen' : 50, 'staryu' : 50, 'magikarp' : 400, 'eevee' : 25, 'omanyte' : 50, 'kabuto' : 50, 'dratini' : 25, 'dragonair' : 100 }



#command to use an .ini file for settings
#settings=ReadSettings(os.path.dirname(sys.argv[0]), "autoProcess.ini", logger=log)
#then just use settings.variable


print "Daryl's PokemonGo Lucky Egg Evolution calculator"

while numEvolv == 0:
        pokeName = str(raw_input("Enter the name of your Pokemon: ").lower())
	for key in pokedex:
                if str(key) == pokeName:
                        numEvolv = pokedex[pokeName]
while numPoke <= 0:
	numPoke = int(input("How many " + pokeName + " do you have? "))
while numCandy < 0:
	numCandy = int(input("How many " + pokeName + " candy do you have? "))


if (numCandy % numEvolv) != 0:
	while ((numCandy + numCandyNew) % numEvolv) != 0:
		numPokeNew += 1
		numCandyNew += 3
		if numPokeNew >= 10:
			break
	if numPokeNew < 10:
		print "You can currently evolve %d %s" % ((numCandy / numEvolv), pokeName)
		print "You should hunt %d more %s to evolve %d" % (numPokeNew, pokeName, (numCandy / numEvolv) + 1)
	else:
		numPokeNew = 0
		numCandyNew = 0
		while ((numCandy % numEvolv) + numCandyNew) < numEvolv:
			numPokeNew += 1
			numCandyNew += 3
		print "You can currently evolve %d %s" % ((numCandy / numEvolv), pokeName)
		print "You will need to hunt %d more %s to evolve %d" % (numPokeNew, pokeName, (numCandy / numEvolv) + 1)
elif numCandy == 0:
	numPokeNew = 0
	numCandyNew = 0
        while ((numCandy % numEvolv) + numCandyNew) < numEvolv:
                numPokeNew += 1
                numCandyNew += 3
        print "You should hunt %d more %s to evolve %d" % (numPokeNew, pokeName, (numCandy / numEvolv) + 1)
else:
	print "You do not need any more %s to use all of your candy" % pokeName
