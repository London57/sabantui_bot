from questions.result_questions import QUESTIONS




class QuestionNode:
    
    def __init__(self, question, bad_answers, good_answer, prevNode, nextNode):
        self.question = question
        self.bad_answers = bad_answers
        self.good_answer= good_answer
        self.prevQuetion = prevNode
        self.nextQuetion = nextNode


class QuestionNodeList:
    #head - первый узел; tall - последний узел
    head = None
    tail = None

    def insert_begin(self, *values, **kwgs_values):
        print(self)
        if self.head is None:
            node = QuestionNode(
                *values, *kwgs_values, prevNode=None, nextNode=None
            )
            self.head = node
            self.tail = node
        else:
            node = QuestionNode(
                *values, *kwgs_values, prevNode=None, nextNode=self.head
            )
            # head - ссылка на первый элемент(узел)
            self.head.prevQuetion = node
            self.head = node

    def insert_end(self, *value, **kwgs_values):
        if self.tail is None:
            node = QuestionNode(
                *value, *kwgs_values, prevNode=None, nextNode=None
            )
            self.tail = node
            self.head = node
        else:
            node = QuestionNode(
                *value, *kwgs_values, prevNode=self.tail, nextNode=None
            )
            self.tail.nextQuetion = node
            self.tail = node
    
    def list_of_Nodes(self):
        l = []
        current = self.head
        while current:
            l.append(current.question)
            current = current.nextQuetion
        return l

    

