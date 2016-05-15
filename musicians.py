class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds
        self.name = self #Kyle: how can I make this be the musician's name taken from the object name?

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")
        
class Drummer(Musician):
    def __init__(self):
        super().__init__(["Ba","Doom","Chi"])
    
    def count(self):
        print("1, 2, 3, 4")
        
    def combust(self):
        print("I'm so hot I'm on fire!")
        
class Band(object):
    def __init__(self):
        self.members = []
        self.name = self  #Kyle: how can I make this be the band's name taken from the object name?
        
    def hire(self,member):
        self.members.append(member)
        print("Welcome to the band {}".format(member.name))
        
    def fire(self,member):
        self.members.remove(member)
        print("Sad news, they voted you out of the band {}".format(member.name))
        
    def play(self):
        canPlay = False
        for member in self.members:
            if isinstance(member,Drummer) == True:
                member.count()
                canPlay = True
                for member in self.members:
                    member.solo(6)
        if canPlay == False:
            print("No drummer...the band can't play")
        
nigel = Drummer()
tyler = Guitarist()
lila = Bassist()
theBand = Band()
theBand.hire(tyler)
theBand.hire(lila)
theBand.hire(nigel)
theBand.fire(lila)

theBand.play()

