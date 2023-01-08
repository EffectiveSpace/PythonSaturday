import random
def create():
    with open('test1.txt', 'w') as data:
        for i in range(5):
            data.write(f'{random.randint(1, 100)}\n')