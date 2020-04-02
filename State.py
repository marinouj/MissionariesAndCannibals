class State(object):

    def __init__(self, missionaries, cannibals,boat, max_m, max_c, capacity, moves):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
        self.max_m = max_m
        self.max_c = max_c
        self.moves = moves

        global MAX_M
        global MAX_C
        global CAP_BOAT

        MAX_M = max_m
        MAX_C = max_c
        CAP_BOAT = capacity

    def move(self):
        stateList = []
        if self.isGoal():
            return
        sign = 1
        if self.boat:
            sign = -1
        for i in range(len(self.moves)):
            (m, c) = self.moves[i]
            stateList = self.nextValidState(m, c, sign, stateList)
        return stateList



    def nextValidState(self, m, c, sign, list):
        temp = State(self.missionaries + sign*m, self.cannibals + sign*c, not self.boat, MAX_M, MAX_C, CAP_BOAT, self.moves)
        if temp.isValid():
            #self.cannibals += sign*c
            #self.missionaries += sign*m
            #self.boat = not self.boat
            list.append(temp)
        return list

    def isValid(self):
        if self.missionaries > MAX_M or self.missionaries < 0 or self.cannibals > MAX_C or self.cannibals < 0:
            return False
        if (self.missionaries >= self.cannibals or self.missionaries == 0) and (MAX_M - self.missionaries >= MAX_C - self.cannibals or MAX_M - self.missionaries == 0):
            return True
        return False

    def isGoal(self):
        if (not self.boat) and self.missionaries == 0 and self.cannibals == 0:
            return True
        return False

    def __eq__(self, other):
        if self.missionaries == other.missionaries and self.cannibals == other.cannibals and self.boat == other.boat:
            return True
        return False

