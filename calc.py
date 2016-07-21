import sys
import os
import json
import getopt
import argparse

print "Daryl's PokemonGo Lucky Egg Evolution calculator"


def main(argv):
    pokeName = "False"
    numPoke = False
    numEvolv = False
    numCandy = False
    numPokeNew = False
    numCandyNew = False
    numEvolvcount = False
    with open('pokedex.json', 'r') as f:
        pokedex = json.load(f)
    parser = argparse.ArgumentParser(description='calc.py -p <pokemon> -n <number of pokemon> -c <number of pokemon candy>')
    parser.add_argument('-p',help='Input Pokemon name',required=False)
    parser.add_argument('-n',help='Input number of pokemon',required=False)
    parser.add_argument('-c',help='Input number of candy',required=False)
    args = parser.parse_args()
    # If you later architect the script to run on a loop overall, I'd suggest 
    # packing the whole script into a loop that iterates on command line arguments
    
    try:
	if pokedex[args.p]:
	    pokeName = str(args.p).lower()
	else:
	    pokeName = str(raw_input("Enter the name of your Pokemon: ").lower())
    except:
	print "Either you've spelled your Poke's name wrong, or your Poke cannot be evolved."
	exit(1)
    numEvolv = pokedex[pokeName]
    try:
	if args.n:
	    numPoke = int(args.n)
	else:
	    numPoke = int(input("How many " + pokeName + " do you have? "))
	numPoke >=0
    except:
	print "Please enter a number"
	exit(2)
    try:
	if args.c:
	    numCandy = int(args.c)
	else:
	    numCandy = int(input("How many " + pokeName + " candy do you have? "))
	numCandy >= 0
    except:
	print "Please enter a number"
	exit(3)
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



if __name__ == "__main__":
    main(sys.argv[1:])
