from .audition import Audition

class Role:
    
    all = []

    def __init__(self, character_name):
        self.character_name = character_name
        Role.all.append(self)

    def __repr__(self):
        return f"<Role name={self.character_name}>"

    @property
    def auditions(self):
        return [audition for audition in Audition.all if audition.role == self]

    @property
    def actors(self):
        return [audition.actor.name for audition in self.auditions]

    @property
    def locations(self):
        location_list = []
        for audition in self.auditions:
            if audition.location not in location_list:
                location_list.append(audition.location)
        return location_list

    @classmethod
    def silver_screen(cls):
        filled_roles = []
        for audition in Audition.all:
            if (audition.role.character_name not in filled_roles) and (audition.hired == True):
                filled_roles.append(audition.role.character_name)
        return filled_roles