from flask import render_template, request, Flask

from coursework2_source.api.views import api_blueprint
from logs import loggings
import utils

app = Flask(__name__, template_folder='templates')
app.config['JSON_AS_ASCII'] = False

loggings.create_logger()

app.register_blueprint(api_blueprint)


@app.route('/')
def main_page():
    posts = utils.get_all_posts()

    return render_template('index.html', posts=posts)


@app.route('/post/<int:pk>')
def post_page(pk):
    post = utils.get_post_by_pk(pk)
    comments = utils.get_comments_by_post_id(pk)
    lenght = len(comments)
    return render_template('post.html', post=post, comments=comments, leng=lenght)


@app.route('/search/')
def search_page():
    search_words = request.args.get('s', '')
    posts = utils.search_for_posts(search_words)
    lenght = len(posts)
    return render_template('search.html', posts=posts, search_words=search_words, leng=lenght)


@app.route('/users/<user_name>')
def username_posts(user_name):
    posts = utils.get_posts_by_user(user_name)
    return render_template('user-feed.html', posts=posts, user_name=user_name)


@app.errorhandler(404)
def page_error_404(error):
    return f"Такой страницы нет {error}", 404


@app.errorhandler(500)
def page_error_500(error):
    return f"На сервере ошибка - {error}", 500


if __name__ == "__main__":
    app.run()
