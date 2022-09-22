import json


def get_all_posts():
    with open('data/posts.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def get_all_comments():
    with open('data/comments.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def get_posts_by_user(user_name):
    """ Возвращает кандидата по имени из posts.json """
    if type(user_name) != str:
        raise TypeError("search_word must be a string")
    results = []
    for post in get_all_posts():
        names = post['poster_name'].lower()
        if user_name in names:
            results.append(post)
    return results


def get_comments_by_post_id(post_id):
    """ Возвращает комментарии из comments.json"""
    results = []
    for comment in get_all_comments():
        if comment['post_id'] == post_id:
            results.append(comment)
        if type(post_id) != int:
            raise TypeError("pk must be integer")
    return results


def search_for_posts(search_word):
    """Тянем несколько постов по ключу из posts.json"""
    if type(search_word) != str:
        raise TypeError("search_word must be a string")
    result = []
    for post in get_all_posts():
        if search_word.lower() in post['content'].lower():
            result.append(post)
    return result


def get_post_by_pk(pk):
    """ Возвращает пост по id из posts.json"""
    for post in get_all_posts():
        if post['pk'] == pk:
            return post
        if type(pk) != int:
            raise TypeError("pk must be integer")
