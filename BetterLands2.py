import os
import sys,getopt
import configparser as cp

infile = None
outfile = None
resetConf = False

class DeckEntry:
    def __init__(self, name, set, number, quantity=1, sideboard=False):
        self.name = name
        self.set = set
        self.number = number
        self.quantity = quantity
        self.sideboard = sideboard

    def getXMageDeckEntryString(self, end=''):
        return f'{"SB: " if self.sideboard else ""}{self.quantity} [{self.set}:{self.number}] {self.name}{end}'


def help():
    print('BetterLands.py')
    sys.exit(2)

try:
    opts, args = getopt.getopt(sys.argv[1:],'hi:o:',['help','resetconfig','input=','output='])
except getopt.GetoptError:
    print('Error: ', end='')
    help()
for opt, arg in opts:
    if opt in ('-h','--help'):
        help()
    elif opt in ('-i','--input'):
        infile = arg
    elif opt in ('-o','--output'):
        outfile = arg
    elif opt in ('--resetconfig'):
        resetConf = True

if resetConf or not os.path.isfile('BetterLands.cfg'):
    config = cp.ConfigParser()

    config['Preferred Basic Lands'] = {}
    config['Preferred Basic Lands']['Island'] = 'THB:251'
    config['Preferred Basic Lands']['Mountain'] = 'THB:253'
    config['Preferred Basic Lands']['Swamp'] = 'THB:252'
    config['Preferred Basic Lands']['Forest'] = 'THB:254'
    config['Preferred Basic Lands']['Plains'] = 'THB:250'

    config['Other Preferences'] = {}
    config['Other Preferences']['Storm Crow'] = '6ED:101'

    with open('BetterLands.cfg', 'w') as configFile:
        config.write(configFile)

if infile is None:
    help()

config = cp.ConfigParser()
config.read('BetterLands.cfg')

if outfile is None:
    outfile = infile.split('.')[0] + 'BL.dck'

deck = []
with open(infile, 'r') as inputFile:
    for line in inputFile.read().split('\n'):
        split_line = line.split(' ')

        if len(split_line) < 3 or split_line[0]=='LAYOUT':
            continue

        if split_line[0] == "SB:":
            card_name = ' '.join(split_line[3:])
            card_set = split_line[2][1:4]
            card_number = split_line[2][5:-1]
            card_qty = split_line[1]
            card_sideboard = True
        else:
            card_name = ' '.join(split_line[2:])
            card_set = split_line[1][1:4]
            card_number = split_line[1][5:-1]
            card_qty = split_line[0]
            card_sideboard = False
        deck.append(DeckEntry(card_name, card_set, card_number, card_qty, card_sideboard))

    for card in deck:
        if card.name in config['Preferred Basic Lands']:
            card.set = config['Preferred Basic Lands'][card.name][0:3]
            card.number = config['Preferred Basic Lands'][card.name][4:]
        elif card.name in config['Other Preferences']:
            card.set = config['Other Preferences'][card.name][0:3]
            card.number = config['Other Preferences'][card.name][4:]

with open(outfile, 'w') as outputFile:
    for card in deck:
        outputFile.write(card.getXMageDeckEntryString(end='\n'))




























# end of file
