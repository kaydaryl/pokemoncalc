import sys
import os
import json

numPoke = False
numEvolv = False
numCandy = False
numPokeNew = False
numCandyNew = False
numEvolvcount = False
with open('pokedex.json', 'r') as f:
	pokedex = json.load(f)

#command to use an .ini file for settings
#settings=ReadSettings(os.path.dirname(sys.argv[0]), "autoProcess.ini", logger=log)
#then just use settings.variable


print "Daryl's PokemonGo Lucky Egg Evolution calculator"

# I'd suggest avoiding while loops when you don't actually need to loop through 
# anything. Your script is currently written to run once and query its 
# parameters manually. 
# I'd suggest replacing this whole block with:
# try:
#     pokeName = str(raw_input("Enter the name of your Pokemon: ").lower())
#     numEvolv = pokedex[pokeName]
# except:
#     print 'Invalid or unclassified Pokemon name entered'
#     exit(1)
#
# If you later architect the script to run on a loop overall, I'd suggest 
# packing the whole script into a loop that iterates on command line arguments

try:
	pokeName = str(raw_input("Enter the name of your Pokemon: ").lower())
	numEvolv = pokedex[pokeName]
except:
	print "Either you've spelled your Poke's name wrong, or your Poke cannot be evolved."
	exit(1)
# See above note about loops. In this case, you're trying to use a loop to 
# replace a conditional, though the conditional doesn't need to be there 
# anyway. What you really want is a try-except clause to take corrective
# action if the input doesn't match what is expected.
try:
	numPoke = int(input("How many " + pokeName + " do you have? "))
	numPoke >= 0
except:
	print "Please enter a number"
	exit(2)
try:
	numCandy = int(input("How many " + pokeName + " candy do you have? "))
	numCandy >= 0
except:
	print "Please enter a number"
	exit(3)
# I don't see anything that really needs improvement past here, except for the
# best practices mentioned above regarding variable declaration. 
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
