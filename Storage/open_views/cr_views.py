from random import randint
from typing import List, Any

"""
    defines crosswords classes

    classes:
    CrossWord - base crossword class store field, answers
    CrossAnswer - class store word coordinates and direction


"""


class CrossAnswer:
    """
    A class used to represent a word in crossword
    this class only use in Crossword
    please dont use this anyone

    fields:
        word - str
        direction - bool
        x - int
        y - int

    methods:
        calc_cor - calculate coordinate in crossword
        recalc_cor - calculate coordinate in optimize crossword



    """

    def __init__(self, word, cross_x, cross_y, direction, letter='0'):
        self.word = word
        self.direction = direction
        self.x, self.y = self.calc_cor(cross_x, cross_y, letter)

    def calc_cor(self, cross_x, cross_y, letter):
        try:
            letter_index = self.word.index(letter)
            if self.direction:
                x = cross_x - letter_index
                y = cross_y
            else:
                x = cross_x
                y = cross_y - letter_index
            return x, y
        except ValueError:
            x = cross_x
            y = cross_y
            return x, y

    def recalc_cor(self, _x, _y):
        self.x = self.x - _x
        self.y = self.y - _y


class Crossword:
    """
    A class represent crossword
    all methods use this class
    dont use this anyone
        fields:
            questions - list of questions input
            answers -   list of answers input
            field - matrix with 0 and letters
            using_words - list of words in crossword
            using_answers - list of classes object (CrossAnswer) in crossword
            using_crossing - list of unique number crossing in crossword
            resolution - fields length,height (dict)

        methods:
            gen_field - generate non optimize field
            find_cross - search crossing with word on the field
            push_word - pushing word into field
            check_proximity - check word collision
            streamline_field - optimizing field
            print_crossword - print crossword in console (can call)



    """

    def __init__(self, QUESTIONS_TO_ANSWERS):
        """
        :param QUESTIONS_TO_ANSWERS: store question: answer (dict)
        """
        self.questions = list(QUESTIONS_TO_ANSWERS.keys())
        self.answers = list(QUESTIONS_TO_ANSWERS.values())

        for i in range(len(self.answers)):
            self.answers[i] = self.answers[i].upper()

        self.answers.sort(key=lambda x: len(x), reverse=True)
        self.field, self.resolution = self.gen_field()
        self.using_words = []
        self.using_crossing = []
        self.using_answers = []
        answer = CrossAnswer(self.answers[0], randint(len(self.answers[0]), self.resolution - len(self.answers[0])),
                             randint(len(self.answers[0]), self.resolution - len(self.answers[0])), randint(0, 1))

        self.push_word(answer)
        self.using_words.append(answer.word)

        for i in range(len(self.answers)):
            word, cross_x, cross_y, letter = self.find_cross()
            direction = self.check_proximity(word, cross_x, cross_y)
            if direction is None:
                continue
            answer = CrossAnswer(word, cross_x, cross_y, direction, letter=letter)
            self.push_word(answer)
            self.using_words.append(answer.word)
            self.using_answers.append(answer)
        _x, _y = self.streamline_field()  # _x, _y - begin coordinate new optimize field

        for i in range(len(self.using_answers)):
            self.using_answers[i].recalc_cor(_x, _y)

    def gen_field(self):
        """
        generate new not optimize field
        :return:
            field - matrix
            length - int (field is square) 
        """
        length = len(self.answers[0]) ** 2
        field = []
        for i in range(length):
            field.append([0] * length)
        return field, length

    def find_cross(self):
        """
        search crossing with word on the field

        :return:
            word - str
            cross_x - int
            cross_y - int
            letter - str
        """
        for answer in self.answers:
            if answer in self.using_words:
                continue
            cross_x = -1
            cross_y = -1
            for _y_ in range(self.resolution):
                for _x_ in range(self.resolution):
                    for i in range(len(answer)):
                        if answer[i] == self.field[_y_][_x_] and _x_ * _y_ not in self.using_crossing:
                            cross_x = _x_
                            cross_y = _y_
                            letter = answer[i]
                            word = answer
                            self.using_crossing.append(cross_x * cross_y)
                            return word, cross_x, cross_y, letter
            if cross_x == -1 or cross_y == -1:
                continue

    def push_word(self, answer):
        """
        pushing word into field
        :param answer: class object CrossAnswer
        """
        word = answer.word
        x = answer.x
        y = answer.y
        direction = answer.direction
        if direction:
            for letter in range(len(word)):
                self.field[y][x + letter] = word[letter]
        else:
            for letter in range(len(word)):
                self.field[y + letter][x] = word[letter]

    def check_proximity(self, word, cross_x, cross_y):
        """
        check word collision
        :param word: str
        :param cross_x: int
        :param cross_y: int
        :return: direction - bool can be None  
        """
        offset = word.index(self.field[cross_y][cross_x])
        _x = cross_x - offset
        _y = cross_y - offset
        if self.field[cross_y][cross_x - 1] == 0 and self.field[cross_y][cross_x + 1] == 0:
            for x in range(_x, _x + len(word)):
                if self.field[cross_y][x] != 0 and self.field[cross_y][x] != word[x - _x]:
                    return None
            return True
        elif self.field[cross_y - 1][cross_x] == 0 and self.field[cross_y + 1][cross_x] == 0:
            for y in range(_y, _y + len(word)):
                if self.field[y][cross_x] != 0 and self.field[y][cross_x] != word[y - _y]:
                    return None
            return False
        else:
            return None

    def streamline_field(self):
        """
        optimizing field
        :return: 
                _x - begin x of optimize field int
                _y - begin x of optimize field int
        """
        data_x = []
        data_y = []
        for x in range(self.resolution):
            for y in range(self.resolution):
                if self.field[y][x] != 0:
                    data_x.append(x)
                    data_y.append(y)
        temp = []
        _x = min(data_x)
        _y = min(data_y)
        x_ = max(data_x)
        y_ = max(data_y)
        for y in range(_y, y_ + 1):
            temp.append([])
            for x in range(_x, x_ + 1):
                temp[y - _y].append(self.field[y][x])
        self.field = temp
        self.resolution = {'length': len(self.field[0]), 'height': len(self.field)}
        return _x, _y

    def print_crossword(self):
        for row in self.field:
            print(*row)
