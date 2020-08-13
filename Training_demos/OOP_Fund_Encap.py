class ForceUser(): 
    def __init__(self):
        #Private Vars cannot be accesses without getters and setters.
        self.__name = "" #private attribute
        self.__forceSide = "" #private attribute

    def setName(self, name):
        self.__name = name
        
    def setforceSide(self, forceSide):
        self.__forceSide = forceSide

    def getName(self):
        return self.__name

    def getforceSide(self):
        return self.__forceSide


jedi = ForceUser()
sith = ForceUser()

#set members
jedi.setName("Anakin")
jedi.setforceSide("Light")
sith.setName("Darth Sidious")
sith.setforceSide("Dark")

#get members
print (jedi.getName())
print (jedi.getforceSide())
print (sith.getName())
print (sith.getforceSide())

