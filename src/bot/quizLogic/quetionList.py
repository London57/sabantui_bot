from .quetionNodeList import QuestionNodeList
from .questions.parse_questions import Questions


class QuestionList(QuestionNodeList):
    # эту функцию можно было написать и в базовом классе.
    def next(self, *values, **kw_values):
        # если в QuestionNodeList есть вопросы и следующего впороса нет, то выходим
        if self.head and self.tail.index == len(Questions) - 1:
            return False
        
        # если в QuestionNodeList нет элементов, то берём первый вопрос
        if not self.head:
            Question = Questions[0]
            return self.insert_end(
                question=Question['question'],
                bad_answers=Question['bad_answers'],
                good_answer=Question['good_answer'],
            ), {
                'question': Questions[0]['question'],
                'bad_answers': Questions[0]['bad_answers'],
                'good_answer': Questions[0]['good_answer'],
                }
        
        # если есть элементы, то берём вопрос по индексу последнего элемента в QuetionNodeList
        else:
            Question = Questions[self.tail.index + 1]
            return self.insert_end(
                question=Question['question'],
                bad_answers=Question['bad_answers'],
                good_answer=Question['good_answer'],
            ), {
                'question': Questions[self.tail.index-1]['question'],
                'bad_answers': Questions[self.tail.index-1]['bad_answers'],
                'good_answer': Questions[self.tail.index-1]['good_answer'],
                }
    
    