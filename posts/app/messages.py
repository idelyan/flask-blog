# POST_NOT_FOUND = {'error': 'Post not found', 'status': 404}
# INTERNAL_SERVER_ERROR = {'data': None, 'message': 'Internal Server Error', 'status': 500}
# NOT_FOUND = {'error': 'Not Found'}, 404
# POST_DELETED = {'message': 'Post was deleted', 'status': 200}

MESSAGES = {
    'POST_NOT_FOUND': {'error': 'Post not found', 'status': 404, 'data': None},
    'INTERNAL_SERVER_ERROR': {'error': 'Internal Server Error', 'status': 500, 'data': None},
    'NOT_FOUND': {'error': 'Not Found', 'status': 404, 'data': None},
    'POST_DELETED': {'message': 'Post was deleted', 'status': 200, 'data': None},
    'POST_CREATED': {'message': 'Post created successfully', 'status': 201, 'data': None},
    'POST_UPDATED': {'message': 'Post updated successfully', 'status': 200, 'data': None},
    'POST_FETCHED': {'message': 'Post fetched successfully', 'status': 200, 'data': None}
}

def get_message(key, data=None):
    message = MESSAGES.get(key, {}).copy()
    if data is not None:
        message['data'] = data
    return message


# MESSAGES = {
#     'POST_NOT_FOUND': {'error': 'Post not found', 'status': 404},
#     'INTERNAL_SERVER_ERROR': {'error': 'Internal Server Error', 'status': 500},
#     'NOT_FOUND': {'error': 'Not Found', 'status': 404},
#     'POST_DELETED': {'message': 'Post was deleted', 'status': 200},
#     'POST_CREATED': {'message': 'Post created successfully', 'status': 201},
#     'POST_UPDATED': {'message': 'Post updated successfully', 'status': 200}
# }

# def get_message(key, additional_data=None):
#     message = MESSAGES.get(key, {}).copy()
#     if additional_data:
#         message.update(additional_data)
#     return message
