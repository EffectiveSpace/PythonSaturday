import random
#Создание класса героя со свойствами и методами
class Character:
    def __init__(self, name, ultimate):
        self.name = name
        self.health = 100
        self.mana = 0
        self.ultimate = ultimate

    def attack(self, enemy):
        enemy.health-=random.randint(1,5)
        self.mana+=random.randint(1,5)
        print(f'{self.name} атакует {enemy.name}, у него {enemy.health} hp')
        return enemy.health

#Создание экземпляров класса Character каждый со своими свойствами
scorpion = Character('Скорпион', ['GET OVER HEAR', 'Атака цепью'])
sub_zero = Character('Саб-зиро', ['Охладуся', 'Замерзайка'])
predator = Character('Хищник', ['Прыскать ядом', 'Удар неведимки'])
jackson = Character('Джексон', ['Удар бензопилой', 'Удар ногой'])

#Создание списка созданных экземпляров
enemies = [scorpion, sub_zero, predator, jackson]

#Выбор случайным образом противников и вывод их в консоль
enemy1 = random.choice(enemies)
enemies.remove(enemy1)
enemy2 = random.choice(enemies)
print(f'{enemy1.name} VS {enemy2.name}')