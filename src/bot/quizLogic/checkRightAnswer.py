from .quetionNodeList import QuestionNodeList

QuestionsState = dict()


def check_right_answer(message, question, Qlist: QuestionNodeList):
    print(question['good_answer'])
    if message == question['good_answer']:
        Qlist.tail.prevQuetion.state = 1
    else:
        Qlist.tail.prevQuetion.state = 0

    QuestionsState[Qlist.tail.prevQuetion] = Qlist.tail.prevQuetion.state
    return QuestionsState
