class ForceUser(): 
    #default constructor
    def __init__(self):
        #Private Vars cannot be accesses without getters and setters.
        self.__name = ""
        self.__forceSide = ""
    def setName(self, name):
        self.__name = name
        
    def setforceSide(self, forceSide):
        self.__forceSide = forceSide

    def getName(self):
        return self.__name

    def getforceSide(self):
        return self.__forceSide


class Jedi(ForceUser):
    #parameterized constructor
    def __init__(self, force):
        self.setforceSide(force)
    

class Sith(ForceUser):
    #parameterized constructor
    def __init__(self, force):
        self.setforceSide(force)


anakin = Jedi("light")
obi_wan = Jedi("light")
vader = Sith("dark")

anakin.setName("Anakin")
obi_wan.setName("Obi-Wan")
#anakin.setforceSide("Light")
vader.setName("Darth Vader")
#vader.setforceSide("Dark")

print ("Jedi Info \nName: {}\nForceSide: {}".format(anakin.getName(), anakin.getforceSide()))
print()
print ("Jedi Info \nName: {}\nForceSide: {}".format(obi_wan.getName(), obi_wan.getforceSide()))
print()
print ("Sith Info \nName: {}\nForceSide: {}".format(vader.getName(), vader.getforceSide()))

