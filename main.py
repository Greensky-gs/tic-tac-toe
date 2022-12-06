from random import randint
from os import system

class Morpion:
    plate = []
    turn = "user"
    ended = False
    winner = "None"
    userCross = "X"
    machineCross = "O"
    neutralCross = "E"

    def __init__(self, options = {}):
        self.machineCross = options.get("machineCross", "O")
        self.neutralCross = options.get('neutralCross', " ")
        self.userCross = options.get('userCross', 'X')

        for i in range(3):
            self.plate.append([])
            for _ in range(3):
                self.plate[i].append(self.neutralCross)
    
    def validCords(self, x, y):
        if not x in range(3) or not y in range(3):
            return False
        return True

    def cords(self, x, y):
        if not self.validCords(x, y):
            return None
        return self.plate[x][y]

    def dataType(self, data):
        if data == self.machineCross:
            return 'm'
        elif data == self.userCross:
            return 'u'
        else:
            return 'n'
    
    def pawnType(self, data):
        if data == 'm':
            return self.machineCross
        elif data == 'u':
            return self.userCross
        else:
            return self.neutralCross

    def platify(self):
        plate = []
        for layer in self.plate:
            for x in layer:
                plate.append(x)
        return plate

    def check(self):
        winner = "none";
        toCheck = ( (0, 1, 2), (0, 3, 6), (0, 4, 8), (3, 4, 5), (1, 4, 7), (2, 4, 6), (6, 7, 8), (2, 5, 8) );

        plate = self.platify()

        for check in toCheck:
            state = plate[check[0]];
            isValid = True;
            for x in check:
                if plate[x] != state:
                    isValid = False;
                if plate[x] == self.neutralCross:
                    isValid = False;

            if isValid:
                winner = ('machine', 'user')[state == self.userCross];
                self.winner = winner
                self.ended = True

        return winner;

    def chooseCase(self):
        choosen = None;
        plate = self.platify();

        numbers = "012 120 345 453 678 786 036 147 258 360 471 582 048 246 642 840 175 354 084 021 354 087 063 285 048 687 084";
        # Define play order. First tuple will be checked, because it gives the bot a win,
        # Then check the second tuple, the defensive one
        # If this do not provide a play, the bot will choose an available case inside of the 3 tuple
        # In case of no case in the third tuple, use a case from fourth tuple
        # And in the extrem case of no cases provided, take a random one
        # In the inner tuples, if the two are occupied by the bot, play the third if it is available
        # The fourth is the filling method, default is 0
        # if it's 0 it means that if 1 and 2 are bot, play third
        # If it's 1, it means that if 1 is bot and 2 is player, play third
        # If it's 2, it means that if both are player, play third
        # If it's 3, it means that if 1 is bot and don't care about 2, play third
        # If it's 4, it means that if 2 is player and don't care about 2, play third
        priorities = (
            ( "012", "021", "120", "048", "084", "840", '480', "345", "435", "453", "543", "354", "534", "246", "264", "462", "642", "624", "678", "768", "687", "867", "786", "876" ),
            ( "0212", "0632", "0842", "2642", "2852", "8672", "0482", "2462", "8402", "6422", "0122", "0212", "2102", "3452", "5432", "3542", "5342", "6782", "6872", "8762", "8672", "0362", "0632", "3602", "1472", "1742", "7412", "2582", "2852", "8522" ),
            ( "4003", "4023", "4083", "4063", "0443", "2443", "6443", "8443" ),
            ( "4013", "4033", "4373", "4453" )
        )

        for priority in priorities:
            for item in priority:
                fillMode = "2"
                if len(item) == 4:
                    fillMode = item[3]
                
                

        
        if not choosen:
            poss = (lambda x: plate[x] == self.neutralCross, [0, 1, 2, 3, 4, 5, 6, 7, 8])

            if not len(poss) == 0:
                choosen = poss[randint(0, len(poss) - 1)];
        if choosen is not None:
            if isinstance(choosen, list):
                choosen = choosen[0]
            if isinstance(choosen, str):
                choosen = int(choosen)

            if choosen < 3:
                return {
                    'x': 0,
                    'y': choosen
                }
            elif choosen < 6:
                return { 'x': 1, 'y': choosen - 3 }
            else:
                return { 'x': 2, 'y': choosen - 6}
        return choosen;

    def botPlay(self):
        case = self.chooseCase();
        if not case is None:
            self.setCord(case.get('x'), case.get('y'), 'm')
        self.check()
    
    def play(self, x, y):
        if self.ended:
            return "Already ended"

        if not self.turn == "user":
            return "This isn't your turn"

        if not self.validCords(x, y):
            return 'Invalid coordinates'
        if not self.cords(x, y) == self.neutralCross:
            return 'Case not empty'

        self.setCord(x, y, 'u')
        self.check();
        return "Played"

    def setCord(self, x, y, type):
        if not self.validCords(x, y):
            return 'Invalid coordinates'
        self.plate[x][y] = self.pawnType(type)

    def stringifyPlate(self):
        plate = ""
        for x in range(3):
            for y in range(3):
                if not y == 0:
                    plate = plate + '|'
                plate = plate + self.cords(x, y)
            if not x == 2:
                plate = plate + '\n-|-|-\n'
            else:
                plate = plate + '\n'
        return plate
        
morpion = Morpion()

print(morpion.stringifyPlate());
while morpion.ended == False:
    x = int(input("X: ")) - 1
    y = int(input('Y: ')) - 1
    
    morpion.play(x, y);
    if morpion.winner == 'user':
        print("You won")
    elif morpion.winner == 'bot':
        print("I won")
    else:
        morpion.botPlay();
        if morpion.winner == 'user':
            print("You won")
        elif morpion.winner == 'bot':
            print("I won")
    system('cls')
    print(morpion.stringifyPlate())
    

if not morpion.winner:
    print("No one's won")