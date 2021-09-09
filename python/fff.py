class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.num_of_dogs += 1
        self.birth_of_dogs += 1
        
    
    def bark():
        print('왈왈!')
        
    @classmethod
    def get_status(cls):
        print(f'Birth: {cls.birth_of_dogs}, Current: {cls.num_of_dogs}')
    # 아래에 코드를 작성하시오.

d1 = Doggy('초코', '푸들')
d2 = Doggy('꽁이', '말티즈')
d3 = Doggy('별이', '시츄')

Doggy.get_status()