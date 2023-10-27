from .audition import Audition

class Role:
    
    all = []

    def __init__(self, character_name):
        self.character_name = character_name
        Role.all.append(self)

    def __repr__(self):
        return f"<Role name={self.character_name}>"