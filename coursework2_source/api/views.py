from flask import jsonify, Blueprint

import logging

from coursework2_source import utils

logger = logging.getLogger("basic")

api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route('/api/')
def main_page():
    return "run API"


@api_blueprint.route('/api/posts')
def get_all_posts():
    all_posts = utils.get_all_posts()
    logger.info('Все посты')
    return jsonify(all_posts)


@api_blueprint.route('/api/posts/<int:post_id>')
def get_post_id(post_id):
    post = utils.get_post_by_pk(post_id)
    logger.info(f'Запрошен пост {post_id}')
    return jsonify(post)
