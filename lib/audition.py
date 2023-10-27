
class Audition:
    
    all = []

    def __init__(self, location, role_instance, actor_instance):
        self.location = location
        self.hired = False
        self.role = role_instance
        self.actor = actor_instance
        Audition.all.append(self)

    def __repr__(self):
        return f"<Audition actor={self.actor.name}, role={self.role.character_name}>"

    def call_back(self):
        self.hired = True