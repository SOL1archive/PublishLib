class Action:
    def __init__(self, actions=None, action_lambda=None):
        self.init_cond = False
        self.end_cond = False
        
        if actions != None:
            for action in actions:
                if type(action) != Action:
                    raise RuntimeError('One element in actions is not type Action')
        self.actions = actions

        if not callable(action_lambda):
            raise RuntimeError('action_lambda is not callable')
        self.action_lambda = action_lambda


        self.actions = actions

    def append_str(self, str):
        pass

    def __call__(self, i, doc):
        if self.actions != None:
            for action in self.actions:
                doc = action(doc)

        return doc