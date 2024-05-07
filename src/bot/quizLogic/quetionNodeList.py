
class QuestionNode:
    def __init__(self, question, bad_answers, good_answer, prevNode, nextNode, index):
        self.question = question
        self.bad_answers = bad_answers
        self.good_answer= good_answer
        self.prevQuetion = prevNode
        self.nextQuetion = nextNode
        self.index = index


class QuestionNodeList:
    #head - первый узел; tall - последний узел
    head = None
    tail = None

    def insert_end(self, question, bad_answers, good_answer):
        if self.tail is None:
            node = QuestionNode(
                question, bad_answers, good_answer, prevNode=None, nextNode=None, index=0
            )
            self.tail = node
            self.head = node
        else:
            node = QuestionNode(
                question, bad_answers, good_answer, prevNode=self.tail, nextNode=None, index=self.tail.index + 1
            )
            self.tail.nextQuetion = node
            self.tail = node
        return {'question': node.question, 'bad_answers': node.bad_answers, 'good_answer': node.good_answer}
    