from src.core.exceptions import VoteDatabaseException
from src.dto.vote import VoteShortInfoResponseDTO
from src.repositories.vote import VoteRepository


class VoteService:
    vote_repository = VoteRepository()

    def get_all_votes(self):
        try:
            result = self.vote_repository.get_all()

            votes_list = [
                VoteShortInfoResponseDTO.model_validate(vote).model_dump(
                    mode='json',
                    exclude_none=True
                ) for vote in result
            ]
            return votes_list
        except VoteDatabaseException:
            return VoteDatabaseException("Problem with DataBase")
