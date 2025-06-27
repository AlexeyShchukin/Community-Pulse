from http import HTTPStatus

from flask import jsonify

from src.core.exceptions import CustomBaseException, VoteDatabaseException
from src.services.vote import VoteService


class VoteController:

    vote_service = VoteService()

    def _handle_vote_exception(self, error: CustomBaseException):
        if isinstance(error, VoteDatabaseException):
            return jsonify({
                'status': 'error',
                'message': error.message,
                'code': error.code
            }), HTTPStatus.INTERNAL_SERVER_ERROR

        else:
            return jsonify({
                'status': 'error',
                'message': error.message,
                'code': error.code
            }), HTTPStatus.INTERNAL_SERVER_ERROR

    def get_votes(self):
        try:
            result = self.vote_service.get_all_votes()

            if isinstance(result, CustomBaseException):
                return self._handle_vote_exception(result)

            return jsonify({
                'status': 'success',
                'data': result,
            }), HTTPStatus.OK
        except CustomBaseException as e:
            return self._handle_vote_exception(e)
