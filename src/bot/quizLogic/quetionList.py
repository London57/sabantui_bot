from .quetionNodeList import QuestionNodeList
from .questions.parse_questions import Questions
from .types import Question


class QuestionList(QuestionNodeList):
    # эту функцию можно было написать и в базовом классе.
    def next(self):
        # если в QuestionNodeList есть вопросы и следующего впороса нет, то выходим
        if self.head and self.tail.index == len(Questions) - 1:
            return False

        # если в QuestionNodeList нет элементов, то берём первый вопрос
        if not self.head:
            question = Questions[0]
            return self.insert_end(
                *question.attrs
            ), question

        # если есть элементы, то берём вопрос по индексу последнего элемента в QuetionNodeList
        else:
            question = Questions[self.tail.index + 1]
            return self.insert_end(
                *question.attrs
            ), Questions[self.tail.index - 1]

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
                        self.tail.good_answer)

    def check_right_answer(self, message, question):
        QuestionsState = dict()
        if message.text == question['good_answer']:
            self.tail.prevQuestion.state = 1
        else:
            self.tail.prevQuestion.state = 0
        QuestionsState[self.tail.prevQuestion.question] = self.tail.prevQuestion.state
        return QuestionsState
