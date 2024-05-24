from .quetionNodeList import QuestionNodeList
from .questions.parse_questions import Questions
from .types import Question, QuestionNode
from datetime import datetime
from aiogram.types import Message


class QuestionList(QuestionNodeList):
    # эту функцию можно было написать и в базовом классе.
    def next(self):
        """
        :return: если не выполняется первое условие, то функция вернёт
        следующий вопросб, предыдущий вопрос, индекс + 1 следующего вопроса
        """
        # если в QuestionNodeList есть вопросы и следующего впороса нет, то выходим
        if self.head and self.tail.index == len(Questions) - 1:
            return False

        # если в QuestionNodeList нет элементов, то берём первый вопрос
        if not self.head:
            question = Questions[0]
            return self.insert_end(
                *question.attrs
            ), question, 1

        # если есть элементы, то берём вопрос по индексу последнего элемента в QuetionNodeList
        else:
            question: Question = Questions[self.tail.index + 1]
            return self.insert_end(
                *question.attrs
            ), Questions[self.tail.index - 1], self.tail.index + 1

    def back(self):
        if self.tail.index == 0:
            return False
        prevQ = self.tail.prevQuestion
        self.tail = prevQ
        # заново определить state, ответив на вопрос
        self.tail.state = None
        self.tail.nextQuestion = None
        self.tail.prevQuestion = prevQ.prevQuestion
        return Question(self.tail.question, self.tail.bad_answers,
                        self.tail.good_answer), self.tail.index + 1

    def check_right_answer(self, message: Message, question: Question):
        if message.text == question.good_answer:
            self.tail.prevQuestion.status = 1
        else:
            self.tail.prevQuestion.status = 0

    def check_last_answer(self, message: Message):
        if message.text == Questions[-1].good_answer:
            self.tail.status = 1
        else:
            self.tail.status = 0

    def count_right_answers(self):
        counter = self.head.status
        this = self.head
        for _ in range(self.tail.index):
            this = this.nextQuestion
            counter += this.status
        return counter
    
    def get_data_for_bd(self, start_quiz_time):
        good_answ_c = self.head.status
        this = self.head
        for _ in range(self.tail.index):
            this = this.nextQuestion
            good_answ_c += this.status
        bad_answ_c = self.tail.index - good_answ_c + 1
        time = datetime.now() - start_quiz_time

        return good_answ_c, bad_answ_c, str(time)
