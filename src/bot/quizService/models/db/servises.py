from .repositories import QuizRepository


class QuizRepositoryService(QuizRepository):
    def select_leaders_quiz(self) -> list:
        return self._select_leaders_quiz()
    
    def insert(self, user_id: int, username: str, good_answ_c: int, bad_anss_c: int, time):
        return self._insert(user_id=user_id, username=username, good_answ_c=good_answ_c, bad_answ_c=bad_anss_c, time=time)
    
    def check_quiz(self, user_id: int):
        return self._check_quiz(user_id=user_id)
    
    def get_user_quiz_info(self, user_id):
        select = self.select_leaders_quiz()
        check = self.check_quiz(user_id)
        for index, value in enumerate(select):
            if value == check:
                return [index + 1, *check]
            
