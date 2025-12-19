import random


class Walker:
    def __init__(self, items):  # event and its probability
        if not items:
            raise ValueError("No events")

        events, probs = zip(*items)
        n = len(events)
        # checking invariants
        if any(p < 0 for p in probs):
            raise ValueError("Probabilities must be positive ")
        s = sum(probs)
        if not ((s - 1.0) == 0):
            raise ValueError("Sum of probabilities must be equels 1")

        self.events = list(events)
        self.n = n
        self.prob = [0.0] * n
        self.alias = [0] * n

        # make column of large and column of small(by definiton of classical walker method)
        scaled = [p * n for p in probs]

        small = []  # provbability less then 1/n
        large = []

        for i, sp in enumerate(scaled):
            if sp < 1.0:
                small.append(i)
            else:
                large.append(i)
        # make table
        while small and large:
            s_idx = small.pop()
            l_idx = large.pop()

            self.prob[s_idx] = scaled[s_idx]
            self.alias[s_idx] = l_idx

            scaled[l_idx] = scaled[l_idx] - (1.0 - scaled[s_idx])

            if scaled[l_idx] < 1.0:
                small.append(l_idx)
            else:
                large.append(l_idx)

        # make leftovers equals 1 for correct local probability in table
        for idx in small + large:
            self.prob[idx] = 1.0
            self.alias[idx] = idx

    def get_random(self):  # method for return 1 random event
        i = random.randrange(self.n)
        u = random.random()
        if u < self.prob[i]:
            return self.events[i]
        else:
            return self.events[self.alias[i]]
