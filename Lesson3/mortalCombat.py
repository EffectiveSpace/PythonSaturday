import random
import time
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

    def super_attack(self, enemy):
        enemy.health-=random.randint(6,10)
        self.mana-=10
        ulta = random.choice(self.ultimate)
        print(f'{self.name} атакует {enemy.name}, используя {ulta}, у него {enemy.health} hp')
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

#Логика поединка
hit = 0
while True:
    hit+=1
    print(f'\nУдар {hit}')
    if random.randint(1,5) in [1,2,3]:
        if enemy1.mana > 7:
            enemy2.health = enemy1.super_attack(enemy2)
        else:
            enemy2.health = enemy1.attack(enemy2)
    else:
        print(f'{enemy1.name} промахнулся')
    time.sleep(1)
    if random.randint(1,2) == 1:
        if enemy2.mana > 7:
            enemy1.health = enemy2.super_attack(enemy1)
        else:
            enemy1.health = enemy2.attack(enemy1)
    else:
        print(f'{enemy2.name} промахнулся')
    time.sleep(2)
    if enemy2.health <= 0 and enemy1.health <= 0:
        print('Ничья')
        break
    elif enemy1.health <= 0:
        print(f'Победа игрока {enemy2.name}')
        break
    elif enemy2.health <= 0:
        print(f'Победа игрока {enemy1.name}')
        break