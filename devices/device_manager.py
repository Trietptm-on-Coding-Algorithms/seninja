class DeviceManager(object):
    def __init__(self, state):
        self.state  = state
        self.stdin  = list()
        self.stdout = list()

    def copy(self, state):
        new_dm = DeviceManager(state)
        new_dm.stdin = list(new_dm.stdin)
        new_dm.stdout = list(new_dm.stdout)
        return new_dm
