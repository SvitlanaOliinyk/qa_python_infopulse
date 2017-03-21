import ClEmp


class ItEmp(ClEmp.Emp):
    def __init__(self, name, surname, pos=None):
        self.name = name
        self.surname = surname
        self.pos = pos
        self.skills = []

    def add_skills(self, new_skill):
        if new_skill != '':
            self.skills.append(new_skill)

if __name__ == "__main__":
    print('555')