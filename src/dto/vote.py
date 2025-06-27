from src.dto import BaseDTO


class VoteShortInfoResponseDTO(BaseDTO):
    poll_id: int
    option_id: int
    voter_id: int
