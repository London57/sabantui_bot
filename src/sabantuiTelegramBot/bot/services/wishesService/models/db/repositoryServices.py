from .repositories import WishesRepository


class WishesRepositoryService(WishesRepository):
    def insert(self, user_id: int, username: str, wishes: str, time):
        return self._insert(user_id=user_id, username=username, wishes=wishes, time=time)
    

            
