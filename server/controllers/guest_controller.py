from flask import Blueprint, jsonify, request
from server.models.guest import Guest
from server.app import db

guest_bp = Blueprint('guests', __name__)

# GET all guests
@guest_bp.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([guest.to_dict() for guest in guests]), 200

# ✅ POST a new guest with validation
@guest_bp.route('/guests', methods=['POST'])
def create_guest():
    data = request.get_json()

    if not data.get('name') or not data.get('occupation'):
        return jsonify({'error': 'Missing guest name or occupation'}), 400

    new_guest = Guest(name=data['name'], occupation=data['occupation'])
    db.session.add(new_guest)
    db.session.commit()

    return jsonify(new_guest.to_dict()), 201

