class Parrot:
    
    def fly(self):
        print('parrot can fly')
        
    def swim(self):
        print("parrot can't swim")
        
class Penguin:
       
    def fly(self):
        print("penguin can't fly")
        
    def swim(self):
        print("penguin can swim")
        
    
def flyingTest(bird):
    bird.fly()    
    
    
prt = Parrot()
pg = Penguin()

flyingTest(prt)
flyingTest(pg)