from flask import Blueprint, request, jsonify
from .models import db, Chore, Assignment
from datetime import datetime

chores_bp = Blueprint('chores_bp', __name__)

@chores_bp.route('/chores', methods=['POST'])
def create_chore():
    data = request.get_json()

    name = data.get('name')
    description = data.get('description')
    due_date = data.get('due_date')
    group_id = data.get('group_id')
    created_by_user_id = data.get('created_by_user_id')
    assigned_user_ids = data.get('assigned_user_ids', [])  # List of user_ids

    if not all([name, due_date, group_id, created_by_user_id]):
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        # Create the chore object
        chore = Chore(
            name=name,
            description=description,
            due_date=datetime.strptime(due_date, '%Y-%m-%d'),
            group_id=group_id,
            created_by_user_id=created_by_user_id
        )

        db.session.add(chore)
        db.session.flush()  # Get the chore_id before committing

        # Create assignment entries
        for user_id in assigned_user_ids:
            assignment = Assignment(user_id=user_id, chore_id=chore.chore_id)
            db.session.add(assignment)

        db.session.commit()

        return jsonify({
            'message': 'Chore created successfully',
            'chore_id': chore.chore_id
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    
@chores_bp.route('/')
def index():
    return jsonify({'message': 'Flask server is running'})

