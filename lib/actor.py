from .audition import Audition

class Actor:
    
    all = []

    def __init__(self, name):
        self.name = name
        Actor.all.append(self)

    def __repr__(self):
        return f"<Actor name={self.name}>"

    @property
    def auditions(self):
        return [audition for audition in Audition.all if audition.actor == self]
    
    @property
    def roles(self):
        return [audition.role for audition in self.auditions]

    @property
    def characters(self):
        return [role.character_name for role in self.roles]
    
    @property
    def paychecks(self):
        return [audition.role.character_name for audition in self.auditions if audition.hired == True]