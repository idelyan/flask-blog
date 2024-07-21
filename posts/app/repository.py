import logging
from .model import db, Post

class PostRepository:

    @staticmethod
    def _get_post(post_id):
        return Post.query.get(post_id)
    
    @staticmethod
    def get_all():
        return Post.query.all()

    @staticmethod
    def get_by_id(post_id):
        return PostRepository._get_post(post_id)

    @staticmethod
    def create(title, body):
        try:
            new_post = Post(title=title, body=body)
            db.session.add(new_post)
            db.session.commit()
            return new_post
        except Exception as e:
            logging.error(f"Error creating post: {e}")
            db.session.rollback()
            return None

    @staticmethod
    def update(post_id, data):
        try:
            post = PostRepository._get_post(post_id)
            if post:
                post.title = data.get('title', post.title)
                post.body = data.get('body', post.body)
                db.session.commit()
                return post
            return None
        except Exception as e:
            logging.error(f"Error updating post: {e}")
            db.session.rollback()
            return None

    @staticmethod
    def delete(post_id):
        try:
            post = PostRepository._get_post(post_id)
            if post:
                db.session.delete(post)
                db.session.commit()
                return True
            return False
        except Exception as e:
            logging.error(f"Error deleting post: {e}")
            db.session.rollback()
            return False
