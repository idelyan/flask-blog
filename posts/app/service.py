from .repository import PostRepository
from .messages import get_message

class PostService:
    @staticmethod
    def get_all_posts():
        posts = PostRepository.get_all()
        return get_message('POST_FETCHED', [post.to_dict() for post in posts])

    @staticmethod
    def get_post_by_id(post_id):
        post = PostRepository.get_by_id(post_id)
        if post is None:
            return get_message('POST_NOT_FOUND')
        return get_message('POST_FETCHED', post.to_dict())

    @staticmethod
    def create_post(title, body):
        new_post = PostRepository.create(title, body)
        if new_post is None:
            return get_message('INTERNAL_SERVER_ERROR')
        return get_message('POST_CREATED', new_post.to_dict())

    @staticmethod
    def update_post(post_id, data):
        post = PostRepository.update(post_id, data)
        if post is None:
            return get_message('POST_NOT_FOUND' if PostRepository.get_by_id(post_id) is None else 'INTERNAL_SERVER_ERROR')
        return get_message('POST_UPDATED', post.to_dict())

    @staticmethod
    def delete_post(post_id):
        post = PostRepository.delete(post_id)
        if not post:
            return get_message('POST_NOT_FOUND' if PostRepository.get_by_id(post_id) is None else 'INTERNAL_SERVER_ERROR')
        return get_message('POST_DELETED')