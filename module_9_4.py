import random

first = 'Мама мыла раму'
second = 'Рамена мало было'

word_1 = list(map(lambda x, y: x == y, first, second))
print(word_1)


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        file = open(file_name, 'w', encoding='utf-8')
        for i in data_set:
            file.write(f'{str(i)}\n')
        file.close()

    return write_everything


write = get_advanced_writer('test.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self, *args, **kwargs):
        return random.choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
