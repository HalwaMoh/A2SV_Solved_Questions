class BrowserHistory(object):

    def __init__(self, homepage):
        self.history = [homepage]
        self.curr_ind = 0

    def visit(self, url):
        self.history = self.history[:self.curr_ind + 1]
        self.history.append(url)
        self.curr_ind += 1

    def back(self, steps):
        self.curr_ind = max(0, self.curr_ind - steps)
        return self.history[self.curr_ind]

    def forward(self, steps):
        self.curr_ind = min(len(self.history) - 1, self.curr_ind + steps)
        return self.history[self.curr_ind]