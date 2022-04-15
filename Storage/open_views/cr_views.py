import random


class Word:
    def __init__(self, word, cross_x, cross_y, letter, direction):
        self.word = word
        self.direction = direction
        self.x, self.y = self.calc_cor(cross_x, cross_y, letter)

    def calc_cor(self, cross_x, cross_y, letter):
        letter_index = self.word.index(letter)
        if self.direction:
            x = cross_x - letter_index
            y = cross_y
        else:
            x = cross_x
            y = cross_y - letter_index
        return x, y


class Crossword:
    def __init__(self, QUESTIONS_TO_ANSWERS):
        self.questions = list(QUESTIONS_TO_ANSWERS.keys())
        self.answers = list(QUESTIONS_TO_ANSWERS.values())
        self.answers.sort(key=lambda x: len(x), reverse=True)
        self.field, self.length_field = self.gen_field()
        for answer in self.answers:

    def gen_field(self):
        length = len(self.answers[0])
        field = []
        for i in range(length):
            field.append([0] * length)
        return field, length

    def push_word(self, answer):
        word = answer.word
        x = answer.x
        y = answer.y
        direction = answer.direction
        if direction:
            for letter in range(len(word)):
                self.field[y][x] = word[x + letter]
        else:
            for letter in range(len(word)):
                self.field[y][x] = word[y + letter]

    def check_crosses(self, prev_answer):
        continue_index = self.answers.index(prev_answer.word)
        for answer in self.answers:
            if answer == self.answers[continue_index]:
                continue
            cross_x = -1
            cross_y = -1
            for _y_ in range(self.length_field):
                for _x_ in range(self.length_field):
                    for i in range(len(answer)):
                        if answer[i] == self.field[_y_][_x_]:
                            cross_x = _x_
                            cross_y = _y_
                            letter = answer[i]
                            return answer, cross_x, cross_y, letter
            if cross_x == -1 or cross_y == -1:
                continue

    def print_crossword():
        for row in self.field:
            print(*row)


def main():
    QUESTIONS_TO_ANSWERS = {
        "Кто переворачивает табличку?": "Кирилл",
        "Как называется этот символ: –": "Тире",
        "Как зовут животное с большими рогами": "Лось",
        "Ночью": "Сон"
    }
    cross = Crossword(QUESTIONS_TO_ANSWERS)
    cross.print_crossword()


if __name__ == '__main__':
    main()