class Cond:
    def __init__(self, cond=None, init_cond=False, end_cond=False):
        self.init_cond = init_cond
        self.end_cond = end_cond

        if type(cond) == str:
            import re
            self.cond = lambda string: len(re.findall(cond, string)) != 0
        elif callable(cond):
            self.cond = cond

    def __call__(self, i, doc):
        return self.cond(doc[i][1])
