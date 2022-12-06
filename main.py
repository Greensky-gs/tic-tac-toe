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
        lignes = [];
        numbers = "012 120 345 453 678 786 036 147 258 360 471 582 048 246 642 840 175 354 084 021 354 087 063 285 048 687 084";

        arrays = numbers.split(' ');
        for x in arrays:
            array = [x[0], x[1], x[2]];
            lignes.append(array);

        for x in lignes:
            if plate[int(x[2])] != self.neutralCross:
                lignes.remove(x)

        for cases in lignes:
            state = plate[int(cases[0])];
            if plate[int(cases[2])] == self.neutralCross and plate[int(cases[1])] == state and state == self.machineCross:
                choosen = cases[2];

        if not choosen:
            for cases in lignes:
                state = plate[int(cases[0])];
                if plate[int(cases[1])] == state and state == self.userCross:
                    choosen = cases[2];
        if not choosen:
            props = list(filter(lambda x: plate[x] == self.neutralCross, [ 0, 2, 4, 6, 8 ]))

            if len(props) > 0:
                choosen = props[randint(0, len(props) - 1)];
            else:
                subs = list(filter(lambda x: plate[x] == self.neutralCross, [1,3,5,7]))

                if len(subs) > 0:
                    choosen = subs[randint(0, len(subs) - 1)];
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
        
# morpion = Morpion()

# print(morpion.stringifyPlate());
# while morpion.ended == False:
#     x = int(input("X: "))
#     y = int(input('Y: '))
    
#     morpion.play(x, y);
#     if morpion.winner == 'user':
#         print("You won")
#     elif morpion.winner == 'bot':
#         print("I won")
#     else:
#         morpion.botPlay();
#         if morpion.winner == 'user':
#             print("You won")
#         elif morpion.winner == 'bot':
#             print("I won")
#     system('cls')
#     print(morpion.stringifyPlate())
    

# if not morpion.winner:
#     print("No one's won")