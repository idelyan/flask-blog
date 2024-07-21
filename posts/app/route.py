from flask import Blueprint, request, jsonify
from .service import PostService
from .messages import get_message
from .utils import handle_response, handle_exceptions

posts_bp = Blueprint('posts', __name__)

@posts_bp.route('/', methods=['GET'])
@handle_exceptions
def get_posts():
    response = PostService.get_all_posts()
    return handle_response(response)

@posts_bp.route('/<int:post_id>', methods=['GET'])
@handle_exceptions
def get_post(post_id):
    response = PostService.get_post_by_id(post_id)
    return handle_response(response)

@posts_bp.route('/', methods=['POST'])
@handle_exceptions
def create_post():
    data = request.get_json(force=True)
    if not data or not data.get('title') or not data.get('body'):
        return jsonify({'error': 'Title and body are required'}), 400
    response = PostService.create_post(data['title'], data['body'])
    return handle_response(response)

@posts_bp.route('/<int:post_id>', methods=['PUT'])
@handle_exceptions
def update_post(post_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    response = PostService.update_post(post_id, data)
    return handle_response(response)

@posts_bp.route('/<int:post_id>', methods=['DELETE'])
@handle_exceptions
def delete_post(post_id):
    response = PostService.delete_post(post_id)
    return handle_response(response)
