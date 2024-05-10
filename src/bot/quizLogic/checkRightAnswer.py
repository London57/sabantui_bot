from .quetionNodeList import QuestionNodeList

QuestionsState = dict()


def check_right_answer(message, question, Qlist: QuestionNodeList):
    if message.text == question['good_answer']:
        Qlist.tail.prevQuestion.state = 1
    else:
        Qlist.tail.prevQuestion.state = 0
    QuestionsState[Qlist.tail.prevQuestion.question] = Qlist.tail.prevQuestion.state
    return QuestionsState
