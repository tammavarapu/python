
class Bird:
    
    def __init__(self):
        print('Bird is ready')
    
    def whoIsThis(self):
        print('Bird')
        
    def swim(self):
        print('swim faster')
        
class Parrot(Bird):
    
    def __init__(self):
        super().__init__()
        print('parrot is ready')
        
    def whoIsThis(self):
        print('parrot')
        
    def run(self):
        print('run faster')
        
        
p = Parrot()
p.whoIsThis()
p.swim()
p.run()

c = Bird()
c.whoIsThis()
c.swim()