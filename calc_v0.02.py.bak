import sys
import os
from pokedex import pokedex

numPoke = 0
numEvolv = 0
numCandy = -1
numPokeNew = 0
numCandyNew = 0
numEvolvcount = 0

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
