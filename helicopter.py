from aircraft import Aircraft

class Helicopter(Aircraft):
    def __init__(self, name):
        super().__init__()
        self.helicopter_name = name
