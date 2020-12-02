import pickle

from pathlib import Path


class State:
    def __init__(self, state_file="out/state.pickle"):
        self.state = {}
        self.save_location = Path(state_file)
        if self.save_location.is_file():
            self.load_state()

    def update_state(self, key, value):
        self.state[key] = value

    def run_if_state_empty(self, key, func, args=None, force=False):
        if args is None:
            args = []
        if key not in self.state or force:
            self.state['key'] = func(*args)
            self.save_state()

    def save_state(self):
        pickle.dump(self.state, open(self.save_location, "wb"))

    def load_state(self):
        self.state = pickle.load(open(self.save_location, "rb"))
        if not isinstance(self.state, dict):
            raise Exception("State must be a `dict` instance")
