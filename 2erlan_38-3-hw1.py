class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def __str__(self):
        return f'Nick: {self.nickname}, Super: {self.superpower}, Health: {self.health_points}'

    def Hi(self):
        print(f'Name: {self.name}')

    def Hi1(self):
        print(self.health_points * 2)

    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero(name="Bruce Wayne", nickname="Batman", superpower="money", health_points=100,
                 catchphrase="Up, up, and away!")
print(str(hero))
hero.Hi()
hero.Hi1()
print(len(hero))