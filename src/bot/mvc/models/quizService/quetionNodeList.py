from .types import QuestionNode, Question


class QuestionNodeList:
    # head - первый узел; tall - последний узел
    head: QuestionNode = None
    tail: QuestionNode = None

    def insert_end(self, question, bad_answers, good_answer):
        if not self.tail:
            node = QuestionNode(
                question, bad_answers, good_answer, prevQuestion=None, nextQuestion=None, index=0
            )
            self.tail = node
            self.head = node
        else:
            node = QuestionNode(
                question, bad_answers, good_answer, prevQuestion=self.tail, nextQuestion=None, index=self.tail.index + 1
            )
            self.tail.nextQuestion = node
            self.tail = node
        return Question(node.question, node.bad_answers, node.good_answer)
