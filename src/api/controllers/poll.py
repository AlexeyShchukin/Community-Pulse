from http import HTTPStatus

from flask import jsonify, request

from src.services.poll import PollService

data = [
    {
        "id": 1,
        "title": "QUESTION 1",
        "description": "POLL 1 DESCRIPTION"
    },
    {
        "id": 2,
        "title": "QUESTION 2",
        "description": "POLL 2 DESCRIPTION"
    },
    {
        "id": 3,
        "title": "QUESTION 3",
        "description": "POLL 3 DESCRIPTION"
    },
    {
        "id": 4,
        "title": "QUESTION 4",
        "description": "POLL 4 DESCRIPTION"
    },
]


class PollController:
    # CRUD for Poll

    def __init__(self):
        self.poll_service = PollService()

    @staticmethod
    def get_polls():
        return jsonify({
            "status": "success",
            "data": data
        }), HTTPStatus.OK

    def get_poll_by_id(self, poll_id: int):
        obj, err = self.poll_service.get_poll_by_id(poll_id)
        if obj:
            return jsonify({
                "status": "success",
                "data": obj
            }), HTTPStatus.OK

        return jsonify({
            "status": "Error",
            "message": err
        }), HTTPStatus.NOT_FOUND  # 404

    @staticmethod
    def create_poll(self):
        data = request.get_json()

        return jsonify({
            "status": "success",
            "data": data
        }), HTTPStatus.CREATED

    @staticmethod
    def update_poll(poll_id: int):
        data = request.get_json()
        obj = next(filter(lambda x: x.get("id") == poll_id, data))
        obj.update(data)

        return jsonify({
            "status": "success",
            "data": obj
        }), HTTPStatus.OK

    @staticmethod
    def delete_poll(poll_id: int):
        data = request.get_json()
        obj = next(filter(lambda x: x.get("id") == poll_id, data))

        del obj

        return jsonify({
            "status": "success",
        }), HTTPStatus.NO_CONTENT  # 204
