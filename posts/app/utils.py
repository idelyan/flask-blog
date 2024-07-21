from flask import jsonify
from functools import wraps
from .messages import get_message

def handle_response(response):
    if 'error' in response:
        return jsonify({'error': response['error']}), response['status']
    return jsonify({'data': response.get('data'), 'message': response.get('message')}), response['status']

def handle_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return jsonify(get_message('INTERNAL_SERVER_ERROR', {'error_detail': str(e)})), 500
    return wrapper