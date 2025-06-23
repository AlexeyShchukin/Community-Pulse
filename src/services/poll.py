from src.models import Poll
from src.services.database import DatabaseService


class PollService(DatabaseService):
    def get_poll_by_id(self, poll_id: int):
        poll, err = self.get_by_id(Poll, poll_id)
        if err:
            return None, err
        if not poll:
            return None, f"Poll with id {poll_id} not found"
        return poll.to_dict(), None