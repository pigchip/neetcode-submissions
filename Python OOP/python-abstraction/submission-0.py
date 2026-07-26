class Superhero:
    def __init__(self, name: str):
       self._name = name
       self._power_level = 40

    def fly(self):
        if self._power_level >= 20:
            print("Up up and away!")
        else:
            print("Too tired to fly...")
    
# Do not modify the code below
hero = Superhero("Superman")
print(hero.fly())  
print(hero.fly())
print(hero.fly())  
