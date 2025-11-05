class animal:
    def __init__(self, name):
        self.name = name
        
class dog(animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age 

class cat(animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age 
             
dog=dog("marco",10)
cat=cat("alice",12)

print(dog.name)
print(dog.age)

print(cat.name)
print(cat.age)
        
        