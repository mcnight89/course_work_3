import json
import pprint


def get_all_posts():
    with open('posts.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def get_all_comments():
    with open('comments.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def get_posts_by_user(user_name):
    """ Возвращает кандидата по имени из posts.json """
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
    return results


def search_for_posts(search_word):
    """Тянем несколько постов по ключу из posts.json"""
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
    return 'Not Found'


#print('---')
#print(get_posts_by_user('hank'))
#print('___')
#pprint.pp(get_comments_by_post_id(3))
#print("___")
#print(search_for_posts('я'))
#print("___")
#print(get_post_by_pk(3))
