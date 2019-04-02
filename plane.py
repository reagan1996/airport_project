from aircraft import Aircraft


class Plane(Aircraft):
    def __init__(self, name):
        super().__init__()
        self.plane_name = name
