from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from server.models.episode import Episode
from server.app import db

episode_bp = Blueprint('episodes', __name__)


@episode_bp.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([{"id": e.id, "date": e.date, "number": e.number} for e in episodes]), 200


@episode_bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if episode:
        return jsonify(episode.to_dict()), 200
    return {"error": "Episode not found"}, 404


@episode_bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return {"error": "Episode not found"}, 404

    db.session.delete(episode)
    db.session.commit()
    return {"message": "Episode deleted"}, 200
