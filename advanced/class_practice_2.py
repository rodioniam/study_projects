# here i will create Forum with users, who can create posts

class User:
    def __init__(self, username: str, email: str):  # expected type
        self.username = username
        self.email = email


class Post:
    def __init__(self, title: str, content: str, author: User):
        self.title = title
        self.content = content
        self.author = author


class Forum:
    def __init__(self):
        # this lists will contain User class and Post class objects with access to theis methods
        self.users = []
        self.posts = []

    def register_user(self, username: str, email: str):
        # this function inside 'Forum' will create User class object
        user = User(username, email)
        self.users.append(user)
        # adding this gave me opportunity to assign it to the variable (?)
        return user

    def create_post(self, title: str, content: str, author: User):
        post = Post(title, content, author)
        self.posts.append(post)
        return post

    def find_user_by_username(self, username: str):
        # because this list contains User class objects i can use its methods like 'user.username'
        for user in self.users:
            if user.username == username:
                return user

    def find_user_by_email(self, email: str):
        for user in self.users:
            if user.email == email:
                return user

    def find_post_by_user(self, user: User):
        user_posts = []
        for post in self.posts:
            if post.author == user:
                user_posts.append(post)
        return user_posts

    def delete_user(self, user: User):
        pass


forum = Forum()

u1 = forum.register_user(username='user_1', email='user_1@mail.com')
u2 = forum.register_user('user_2', 'u2@u2.com')

forum.users
# [<__main__.User object at 0x104a37fb0>, <__main__.User object at 0x104a37ec0>]

p1 = forum.create_post(title='name', content='First post', author=u1)
p2 = forum.create_post(title='name_2', content='Second post', author=u2)

forum.posts
# [<__main__.Post object at 0x105114650>, <__main__.Post object at 0x105114680>]

forum.posts[0].title  # name
forum.posts[0].content  # First post
forum.posts[0].author  # <__main__.User object at 0x102c04830>
forum.posts[0].author.username  # user_1
forum.posts[0].author.email  # user_1@mail.com
forum.find_user_by_username('admin1234')  # None
forum.find_user_by_username('user_1')  # <__main__.User object at 0x102fe4e30>
forum.find_user_by_username('user_1').email  # user_1@mail.com
forum.find_user_by_email('u2@u2.com')  # <__main__.User object at 0x104f0d250>
forum.find_user_by_email('u2@u2.com').username  # user_2

forum.create_post('post_vvv', 'some text in the post', u1)

forum.find_post_by_user(u1)
# [<__main__.Post object at 0x10313d9d0>, <__main__.Post object at 0x10313da00>]
forum.find_post_by_user(u2)
# [<__main__.Post object at 0x104b49940>]

post_titles = [post.title for post in forum.find_post_by_user(u1)]

post_titles  # ['name', 'post_vvv']


user_email = 'user_1@mail.com'

forum.find_post_by_user((forum.find_user_by_email(user_email)))
# [<__main__.Post object at 0x104845d60>, <__main__.Post object at 0x104845dc0>]

post_titles_2 = [post.title for post in forum.find_post_by_user(
    (forum.find_user_by_email(user_email)))]

post_titles_2  # ['name', 'post_vvv']
