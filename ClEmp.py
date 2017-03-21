class Emp:
    def __init__(self, name, surname, pos=None):
        self.name = name
        self.surname = surname
        self.pos = pos

    def set_name(self, name, surname):
        self.name = name
        self.surname = surname

    def set_pos(self, pos):
        self.pos = pos

    def full_name(self):
        return self.name + ' ' + self.surname
