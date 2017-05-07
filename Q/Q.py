class Q:

    def __init__(self):
        # Dict of lists
        # i.e. 2d array of state
        self.table = {}

    def get(self, a, s):
        return self.get_actions[a]

    def get_actions(self, s):
        if s not in self.table:
            self.table[s] = [0, 0, 0]
        return self.table[s]

    def set(self, a, s, val):
        self.table[s][a] = val
