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
        self.neutralCross = options.get('neutralCross', "E")
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

        return winner;

    def chooseCase(self):
        choosen = "";
        plate = self.platify();
        lignes = [];
        numbers = "012 120 345 453 678 786 036 147 258 360 471 582 048 246 642 840 175 354 084 021 354 087 063 285 048 687 084";

        arrays = numbers.split(' ');
        for x in arrays:
            array = [x[0], x[1], x[2]];
            lignes.append(array);

        for x in lignes:
            if plate[x[2]] != self.neutralCross:
                index = lignes.index(x)
                lignes.splice(index, 1);

        for cases in lignes:
            state = plate[cases[0]];
            if plate[cases[2]] != self.neutralCross:
                return;
            if plate[cases[1]] == state && state === this.bot_piece) choosen = cases[2];
        });
        if (!choosen) {
            lignes.forEach((cases) => {
                let state = this.matrix[cases[0]];
                if (this.matrix[cases[2]] !== this.neutral) return;
                if (this.matrix[cases[1]] === state && state === this.user_piece) choosen = cases[2];
            });
        };
        if (!choosen) {
            const props = [0,2,4,6,8].filter(x => this.matrix[x] === this.neutral);
            if (props.length > 0) {
                choosen = props[functions.random(props.length, 0)];
            } else {
                const subs = [1,3,5,7].filter(x => this.matrix[x] === this.neutral);
                if (subs.length > 0) {
                    choosen = subs[functions.random(subs.length, 0)];
                };
            };
        };
        if (!choosen) {
            const poss = [0, 1, 2, 3, 4, 5, 6, 7, 8].filter((x) => this.matrix[x] === this.neutral);
            if (poss.length === 0) return;
            choosen = poss[functions.random(poss.length, 0)];
        }
        return choosen;

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
                    plate = plate + ' '
                plate = plate + self.cords(x, y)
            if not x == 2:
                plate = plate + '\n-|-|-\n'
            else:
                plate = plate + '\n'
        plate = plate.replace(' ', '|')
        return plate
        
morpion = Morpion()
print(morpion.stringifyPlate())