class dog :
    def sound(self):
        return"bark"
    
class cat :
    def sound(self):
        return"meow"
    
def makesound(animal):
    print(animal.sound())
    
d=dog()
c=cat()

makesound(d)
makesound(c)