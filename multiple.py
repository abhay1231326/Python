class Parent1:
    def greet(self):
        print("hello from parent 1 ")
    
class parent2:
    def hello(self):
        print("hello from parent 2")
            
class child(Parent1,parent2):
    def hi(self):
        print("hello from child")
            
children=child()
children.greet()
children.hello()
children.hi()

