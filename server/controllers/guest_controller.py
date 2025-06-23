from flask import Blueprint, jsonify
from server.models.guest import Guest
from server.app import db

guest_bp = Blueprint('guests', __name__)

@guest_bp.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([guest.to_dict() for guest in guests]), 200
